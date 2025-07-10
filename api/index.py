from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from faster_whisper import WhisperModel
import base64
import io
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()
# If you have a GPU, change device to "cuda" for better performance
model = WhisperModel("base", device="cpu", compute_type="float32")

class AudioPayload(BaseModel):
    audio_base64: str

@app.post("/transcribe/")
async def transcribe(payload: AudioPayload):
    try:
        audio_b64 = payload.audio_base64.split(",")[-1] if "," in payload.audio_base64 else payload.audio_base64
        audio_data = base64.b64decode(audio_b64)
        audio_file = io.BytesIO(audio_data)
        # faster-whisper can accept file-like objects
        segments, _ = model.transcribe(audio_file)
        transcription = "".join([segment.text for segment in segments])
        return {"transcription": transcription}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def handler(request: Request):
    return app
