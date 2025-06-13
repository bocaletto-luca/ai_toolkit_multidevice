# app.py
import argparse
import subprocess
import sys
import requests

__version__ = "1.0.0"

from tasks.summarizer      import summarize
from tasks.qa              import answer
from tasks.transcription   import transcribe
from tasks.image_caption   import caption_image

def self_update():
    data = requests.get("https://pypi.org/pypi/ai_toolkit/json", timeout=5).json()
    latest = data["info"]["version"]
    if latest != __version__:
        print(f"Updating ai_toolkit: {__version__} → {latest}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "ai_toolkit"])
        print("Aggiornato. Rilancia il comando.")
        sys.exit(0)
    print("Sei già alla versione più recente.")

def main():
    parser = argparse.ArgumentParser(prog="ai_toolkit", description="Local AI Toolkit")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("update", help="Self-update via PyPI")
    s = sub.add_parser("summarize", help="Summarize text")
    s.add_argument("file", help="Path to text file")
    q = sub.add_parser("qa", help="Question-answering")
    q.add_argument("question", help="Question to ask")
    q.add_argument("file", help="Context text file")
    t = sub.add_parser("transcribe", help="Transcribe audio")
    t.add_argument("audio", help="Path to audio file")
    c = sub.add_parser("caption", help="Caption image")
    c.add_argument("image", help="Path to image file")

    args = parser.parse_args()

    if args.cmd == "update":
        self_update()
    elif args.cmd == "summarize":
        text = open(args.file, encoding="utf-8").read()
        print(summarize(text))
    elif args.cmd == "qa":
        context = open(args.file, encoding="utf-8").read()
        print(answer(args.question, context))
    elif args.cmd == "transcribe":
        print(transcribe(args.audio))
    elif args.cmd == "caption":
        print(caption_image(args.image))

if __name__ == "__main__":
    main()
