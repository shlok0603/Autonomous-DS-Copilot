from services.ai_service import AIService

ai = AIService()

response = ai.generate_insights(
    "Explain what a CSV file is in two sentences."
)

print(response)