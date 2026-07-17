from services.ai_service import AIService


class ChatService:

    def __init__(self):
        self.ai = AIService()

    def ask(self, df, question):

        preview = df.head(10).to_markdown(index=False)

        prompt = f"""
You are an expert Data Scientist.

Below is the dataset preview.

{preview}

User Question:

{question}

Answer only using the information available in the dataset.

If the answer cannot be inferred from the preview, clearly say so.

Keep the answer concise and professional.
"""

        return self.ai.generate_insights(prompt)