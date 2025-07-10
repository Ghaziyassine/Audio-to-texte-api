from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from faster_whisper import WhisperModel
import base64
import tempfile

app = FastAPI()
# model = WhisperModel("base", device="cuda", compute_type="float16")
model = WhisperModel("base", device="cpu", compute_type="float32")

class AudioPayload(BaseModel):
    audio_base64: str

@app.post("/transcribe/")
async def transcribe(payload: AudioPayload):
    try:
        # Strip base64 prefix if present (e.g., "data:audio/mp3;base64,...")
        if "," in payload.audio_base64:
            payload.audio_base64 = payload.audio_base64.split(",")[1]

        audio_data = base64.b64decode(payload.audio_base64)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            tmp.write(audio_data)
            tmp.flush()
            tmp_path = tmp.name

        segments, _ = model.transcribe(tmp_path)
        transcription = "".join([segment.text for segment in segments])
        return {"transcription": transcription}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
