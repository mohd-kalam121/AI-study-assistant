import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import APIError

load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("GEMINI_API_KEY not found.")
    sys.exit(1)

client = genai.Client(api_key=api_key)

system_prompt = """
You are a study assistant.

- Create structured study plans.
- Keep answers concise.
- Explain concepts clearly.
- Guide students with hints instead of directly solving homework.
"""

MODEL = "gemini-2.5-flash-lite"


def main():
    print("=== AI Study Assistant ===")

    topic = input("Enter a topic: ").strip()

    if not topic:
        print("No topic entered.")
        return

    config = types.GenerateContentConfig(
        system_instruction=system_prompt
    )

    chat = client.chats.create(
        model=MODEL,
        config=config
    )

    try:
        print(f"\nGenerating study plan for {topic}...\n")

        response = chat.send_message(
            f"""
            Create a beginner-to-interview roadmap for {topic}.

            Include:
            1. Learning order
            2. Key topics
            3. Short description of each topic
            4. Important interview areas
            """
        )

        print(response.text)

    except APIError as e:
        print(f"\nAPI Error: {e}")
        return

    questions_asked = 0

    while True:
        user_input = input(
            "\nAsk a question (or type 'exit'): "
        ).strip()

        if user_input.lower() in ("exit", "quit"):
            print("\n=== Session Summary ===")
            print(f"Topic: {topic}")
            print(f"Questions Asked: {questions_asked}")
            print("Good luck with your studies!")
            break

        if not user_input:
            continue

        try:
            response = chat.send_message(user_input)

            print("\n" + response.text)

            questions_asked += 1

        except APIError as e:
            print(f"\nAPI Error: {e}")

        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()