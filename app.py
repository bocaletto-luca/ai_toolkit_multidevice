# app.py
import argparse, subprocess, sys, requests

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
        print("Updated. Rerun your command.")
        sys.exit(0)
    print("Already up-to-date.")

def main():
    p = argparse.ArgumentParser(prog="ai_toolkit", description="Local AI Toolkit")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("gui", help="Launch GUI")
    sub.add_parser("update", help="Self-update via PyPI")

    s = sub.add_parser("summarize");    s.add_argument("file")
    q = sub.add_parser("qa");           q.add_argument("question"); q.add_argument("file")
    t = sub.add_parser("transcribe");   t.add_argument("audio")
    c = sub.add_parser("caption");      c.add_argument("image")

    args = p.parse_args()

    if args.cmd == "gui":
        from gui import run_gui
        run_gui()
    elif args.cmd == "update":
        self_update()
    elif args.cmd == "summarize":
        print(summarize(open(args.file, encoding='utf-8').read()))
    elif args.cmd == "qa":
        print(answer(args.question, open(args.file, encoding='utf-8').read()))
    elif args.cmd == "transcribe":
        print(transcribe(args.audio))
    elif args.cmd == "caption":
        print(caption_image(args.image))

if __name__ == "__main__":
    main()
