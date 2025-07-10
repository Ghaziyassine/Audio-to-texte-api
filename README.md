# Audio Transcription API

A FastAPI-based web service that transcribes audio files using the Faster Whisper model.

## Overview

This API provides a simple endpoint to transcribe audio content that's sent as base64-encoded data. The service uses the Faster Whisper model, which is an optimized implementation of OpenAI's Whisper automatic speech recognition (ASR) model.

## Features

- Transcribe audio from base64-encoded strings
- Support for various audio formats
- Efficient transcription with Whisper ASR
- Simple REST API interface

## Requirements

- Python 3.8+
- FastAPI
- Faster Whisper
- See `requirements.txt` for complete dependencies

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment:

```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:

```bash
uvicorn api.index:app --reload
```

2. The API will be available at `http://127.0.0.1:8000`

3. Use the `/transcribe/` endpoint with a POST request containing JSON with an `audio_base64` field:

```json
{
  "audio_base64": "data:audio/mp3;base64,BASE64_ENCODED_AUDIO_DATA"
}
```

4. The response will contain the transcribed text:

```json
{
  "transcription": "The transcribed text will appear here."
}
```

## API Documentation

Once the server is running, you can access the automatically generated API documentation:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Example

### Using cURL:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/transcribe/' \
  -H 'Content-Type: application/json' \
  -d '{
    "audio_base64": "data:audio/mp3;base64,..."
  }'
```

### Using Python requests:

```python
import requests
import base64

# Read audio file and convert to base64
with open("audio.mp3", "rb") as audio_file:
    encoded_audio = base64.b64encode(audio_file.read()).decode('utf-8')

payload = {
    "audio_base64": f"data:audio/mp3;base64,{encoded_audio}"
}

response = requests.post("http://127.0.0.1:8000/transcribe/", json=payload)
print(response.json())
```

## Performance Notes

- The API uses the CPU for processing. If you have a compatible NVIDIA GPU with updated drivers, you can modify the code to use CUDA for faster processing.
- Transcription time depends on the audio length and the hardware capabilities.

## License

[Specify your license information here]

## Contact

[Your contact information]
