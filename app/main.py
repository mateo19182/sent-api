# app/main.py
from fastapi import FastAPI
from openai import OpenAI
import json
from pysentimiento import create_analyzer

app = FastAPI()

sentiment_analyzer = create_analyzer(task="sentiment", lang="es")
# emotion_analyzer = create_analyzer(task="emotion", lang="es")
@app.get("/sentiment/")
def sentiment_analysis(text: str):
    if not text:
        return {"error": "Text input is empty"}

    # Analyze the sentiment of the input text
    result = sentiment_analyzer.predict(text)

    # The result contains the predicted sentiment and probabilities
    return {
        "sentiment": result.output,
        "probabilities": result.probas
    }


# Initialize the OpenAI client
inferenceClient = OpenAI(
    api_key="sk-dummy",  # Replace with your actual API key or use environment variables
    base_url="http://alpine-llama:8080/v1"
    )
@app.get("/analyze/")
async def analyze_text(text: str):
    system_prompt = (
        "You are a text classifier for a gym's feedback system. "
        "Your task is to classify user feedback into one of the following categories: "
        "['queja-material', 'queja-personal', 'sugerencia', 'dudas', 'no-relevante']. "
        "Here is what each category means:\n"
        "1. 'queja-material': Complaints about gym equipment, facilities, or infrastructure (e.g., broken machines, dirty bathrooms, parking issues, operating hours).\n"
        "2. 'queja-personal': Complaints about staff behavior, trainers, or other members (e.g., rude trainers, uncomfortable interactions).\n"
        "3. 'sugerencia': Suggestions or positive feedback about the gym, classes, trainers, or facilities (e.g., great classes, friendly staff, ideas for improvement).\n"
        "4. 'dudas': Feedback that expresses doubts, questions, or uncertainties about the gym (e.g., '¿A qué hora abren el fin de semana?', 'No sé si renovar mi membresía.').\n"
        "5. 'no-relevante': Feedback that is irrelevant to the gym experience (e.g., comments about the weather, unrelated topics).\n\n"
        "Respond **only** in JSON format with the key 'category'. "
        "Do not include any additional text or explanations. "
        "Here are some examples:\n"
        "- Input: 'Las máquinas de pesas están descompuestas.'\n"
        "  Output: {'category': 'queja-material'}\n"
        "- Input: 'El entrenador fue muy grosero conmigo.'\n"
        "  Output: {'category': 'queja-personal'}\n"
        "- Input: 'Me encantaría que agregaran más clases de yoga por la mañana.'\n"
        "  Output: {'category': 'sugerencia'}\n"
        "- Input: '¿A qué hora abren el fin de semana?'\n"
        "  Output: {'category': 'dudas'}\n"
        "- Input: 'Hoy hace mucho calor afuera.'\n"
        "  Output: {'category': 'no-relevante'}\n\n"
        "Now classify the following input:"
    )

    try:
        response = inferenceClient.chat.completions.create(
            model="Llama-3.2-1B-Instruct",  # Replace with your actual model name
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ],
            temperature=0.5,
            max_tokens=50,
            response_format={"type": "json_object"},  # Enforce JSON response
        )
        print(inferenceClient.base_url)
        # Extract the generated content
        generated_text = response.choices[0].message.content

        # Parse the JSON response
        analysis = json.loads(generated_text)
        return analysis

    except Exception as e:
        return {"error": f"An error occurred: {e}"}