import os
from dotenv import load_dotenv
from providers.openai import ask_openai

load_dotenv()

print("================================")
print("          AI HUB")
print("================================")
print("Введите вопрос для AI.")
print("Для выхода напишите: exit")
print()

while True:
    question = input("Вы: ")

    if question.lower() == "exit":
        print("AI HUB завершён.")
        break

    if not question.strip():
        continue

    try:
        answer = ask_openai(question)
        print()
        print("AI:", answer)
        print()
    except Exception as e:
        print("Ошибка:", e)
