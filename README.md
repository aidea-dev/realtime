# OpenAI Realtime API python client

Integration of OpenAI Realtime API to chat in voice-to-voice mode

---

#### Setup

```bash
# Install ffmpeg to deal with audio input/output
sudo apt install ffmpeg
# Install llama pip package
pip install openai-realtime-client
```

Create a *.env* file and insert your OPENAI_API_KEY:
```bash
cp .env.example .env
```

#### Run

```bash
cd src
python app.py
```

Add your function calls in *functions.py*, then... just talk!
