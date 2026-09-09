import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def ask_openai(question):
    response = client.responses.create(
        model="gpt-5-mini",
        input=question
    )

    return response.output_text
