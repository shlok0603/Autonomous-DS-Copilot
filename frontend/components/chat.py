import streamlit as st

from frontend.ui.hero import render as hero
from services.chat_service import ChatService


def render(df):

    # =====================================================
    # HERO
    # =====================================================

    hero(
        title="AI Dataset Assistant",
        subtitle="Chat with your dataset using Gemini AI.",
        icon="💬"
    )

    # =====================================================
    # SESSION
    # =====================================================

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # =====================================================
    # DATASET INFO
    # =====================================================

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Rows",
            f"{df.shape[0]:,}"
        )

    with c2:
        st.metric(
            "Columns",
            df.shape[1]
        )

    with c3:
        st.metric(
            "Memory",
            f"{round(df.memory_usage(deep=True).sum()/1024**2,2)} MB"
        )

    st.divider()

    # =====================================================
    # QUICK QUESTIONS
    # =====================================================

    st.markdown("### ⚡ Suggested Questions")

    q1, q2, q3 = st.columns(3)

    with q1:
        if st.button(
            "📊 Summarize Dataset",
            use_container_width=True
        ):
            st.session_state.question = "Summarize this dataset."

    with q2:
        if st.button(
            "❗ Missing Values",
            use_container_width=True
        ):
            st.session_state.question = (
                "Explain missing values."
            )

    with q3:
        if st.button(
            "📈 Best Insights",
            use_container_width=True
        ):
            st.session_state.question = (
                "Give important business insights."
            )

    st.divider()

    # =====================================================
    # INPUT
    # =====================================================

    default_question = st.session_state.get(
        "question",
        ""
    )

    question = st.text_input(
        "Ask anything about your dataset",
        value=default_question,
        placeholder="Example: Which feature is most important?"
    )

    left, right = st.columns([5, 1])

    with right:

        ask = st.button(
            "🚀 Ask",
            use_container_width=True
        )

    if ask:

        if question.strip():

            with st.spinner("🤖 Gemini is thinking..."):

                chat = ChatService()

                answer = chat.ask(
                    df,
                    question
                )

            st.session_state.chat_history.append(
                {
                    "question": question,
                    "answer": answer
                }
            )

            st.session_state.question = ""

            st.rerun()

    # =====================================================
    # CHAT HISTORY
    # =====================================================

    st.markdown("## 💬 Conversation")

    if len(st.session_state.chat_history) == 0:

        st.info(
            "Start chatting with your dataset."
        )

        return

    for item in reversed(
        st.session_state.chat_history
    ):

        with st.chat_message("user"):

            st.markdown(item["question"])

        with st.chat_message("assistant"):

            st.markdown(item["answer"])

    st.divider()

    # =====================================================
    # FOOTER
    # =====================================================

    st.caption(
        "🤖 Powered by Gemini AI • Dataset-aware conversational analytics"
    )