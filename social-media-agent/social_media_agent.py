import asyncio
import os
import sys
from youtube_transcript_api import YouTubeTranscriptApi
from google import genai
from google.genai import types
from dataclasses import dataclass

# Initialize Gemini client
try:
    GEMINI_API_KEY = os.environ['GEMINI_API_KEY']
except KeyError:
    print("API key not found")
    sys.exit(1)
else:
    client = genai.Client()

# Generate social media content tool
def generate_content_tool(video_transcript: str, social_media_platform: str):
    print(f"Generating social media content for {social_media_platform}...")

    model = "gemini-2.5-flash"
    prompt=f"Here is a new video transcript:\n{video_transcript}\n"
    f"Generate a social media post on my {social_media_platform} based on my provided video transcript. Make it engaging, informative and appropriate for the platform. You may search the web for up-to-date information on the topic and fill in useful details if necessary."
    
    grounding_tool = types.Tool(google_search=types.GoogleSearch())
    config = types.GenerateContentConfig(tools=[grounding_tool])

    response = client.models.generate_content(model=model, contents=prompt, config=config)

    return response.text

# Social media post dataclass
@dataclass
class Post:
    platform: str
    content: str

# Get video transcript
def get_transcript(video_id: str, languages: list = None) -> str:
    if languages is None:
        languages = ["en"]
    try:
        yt_api = YouTubeTranscriptApi()
        fetched_transcript = yt_api.fetch(video_id, languages=languages)
        transcript_text = " ".join(snippet.text for snippet in fetched_transcript)

        return transcript_text
    except Exception as e:
        from youtube_transcript_api._errors import (
            CouldNotRetrieveTranscript,
            VideoUnavailable,
            InvalidVideoId,
            NoTranscriptFound,
            TranscriptsDisabled
        )

        if isinstance(e, NoTranscriptFound):
            error_msg = f"No transcript found for video {video_id} in languages: {languages}"
        elif isinstance(e, VideoUnavailable):
            error_msg = f"Video {video_id} is unavailable"
        elif isinstance(e, InvalidVideoId):
            error_msg = f"Invalid video ID: {video_id}"
        elif isinstance(e, TranscriptsDisabled):
            error_msg = f"Transcripts are disabled for video {video_id}"
        elif isinstance(e, CouldNotRetrieveTranscript):
            error_msg = f"Could not retrieve transcript: {str(e)}"
        else:
            error_msg = f"An unexpected error occurred: {str(e)}"

        print(f"Error: {error_msg}")
        raise Exception(error_msg) from e

# Main function
async def main():
    video_id = "OZ5OZZZ2cvk"
    transcript = get_transcript(video_id)

    platforms = ["LinkedIn", "Instagram"]
    results = []

    for platform in platforms:
        content = generate_content_tool(transcript, platform)
        results.append(Post(platform=platform, content=content))

    print("\nGenerated Social Media Posts:\n")

    for post in results:
        print(f"[{post.platform}]\n{post.content}\n{'-'*60}")

if __name__ == "__main__":
    asyncio.run(main())