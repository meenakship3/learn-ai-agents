# Social Media Content Generator

An AI agent that generates social media content from YouTube video transcripts using Google's Gemini AI model. Tutorial used - [](https://www.youtube.com/watch?v=zOFxHmjIhvY)

## Features

- Generates platform-specific content for Instagram and Linkedin from YouTube video transcripts
- Uses Gemini AI with web search capabilities for up-to-date content
- Asynchronous processing for efficient execution
- Error handling for YouTube transcript retrieval

## Project Structure

```
social-media-agent/
├── app.py
├── requirements.txt
└── social_media_agent.py
```

## Requirements

- Python 3.9+
- Google Gemini API key
- Required Python packages:
  - youtube_transcript_api
  - google-genai

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   ```

2. Install dependencies:
   ```bash
   pip install youtube_transcript_api google-genai
   ```

3. Set up Gemini API key:
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```
4. Run the agent:

```bash
python3 social-media-agent/social_media_agent.py
```
Note: Replace hard-coded video ID in the code with your own video ID


## Sample Output


