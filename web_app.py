import streamlit as st
from providers.openai import ask_openai

st.set_page_config(
    page_title="AI HUB",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI HUB")
st.subheader("Все ИИ в одном месте")

st.divider()

model = st.selectbox(
    "Выберите AI",
    [
        "GPT",
        "Claude",
        "Gemini",
        "DeepSeek"
    ]
)

question = st.text_area(
    "Ваш вопрос",
    placeholder="Напишите свой вопрос..."
)

if st.button("🚀 Отправить", use_container_width=True):

    if not question.strip():
        st.warning("Введите вопрос.")
    else:

        with st.spinner("AI думает..."):

            if model == "GPT":
                answer = ask_openai(question)
            else:
                answer = f"{model} пока не подключён."

        st.divider()
        st.subheader("Ответ AI")
        st.write(answer)
