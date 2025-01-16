# app/main.py
from fastapi import FastAPI
from openai import OpenAI
import json
# from pysentimiento import create_analyzer

app = FastAPI()

# sentiment_analyzer = create_analyzer(task="sentiment", lang="es")
# # emotion_analyzer = create_analyzer(task="emotion", lang="es")
# @app.get("/sentiment/")
# def sentiment_analysis(text: str):
#     if not text:
#         return {"error": "Text input is empty"}

#     # Analyze the sentiment of the input text
#     result = sentiment_analyzer.predict(text)

#     # The result contains the predicted sentiment and probabilities
#     return {
#         "sentiment": result.output,
#         "probabilities": result.probas
#     }


# Initialize the OpenAI client
inferenceClient = OpenAI(
    api_key="sk-dummy",  # Replace with your actual API key or use environment variables
    base_url="http://alpine-llama:8080/v1"
    )
@app.get("/analyze/")
async def analyze_text(text: str):
    system_prompt = (
        "Eres un clasificador de texto para el sistema de comentarios de un gimnasio. "
        "Tu tarea es clasificar los comentarios de usuarios en categorías y determinar el sentimiento. "
        "Categorías: ['instalaciones', 'material', 'personal', 'sugerencia', 'dudas', 'no-relevante']\n"
        "Sentimiento: ['positivo', 'negativo', 'neutral']\n\n"
        "Definición de categorías:\n"
        "1. 'instalaciones': Comentarios sobre la infraestructura del gimnasio (ej., baños, vestidores, aire acondicionado, estacionamiento, limpieza, espacios).\n"
        "2. 'material': Comentarios sobre equipos y máquinas del gimnasio (ej., pesas, máquinas cardiovasculares, colchonetas, equipamiento en general).\n"
        "3. 'personal': Comentarios sobre el personal, entrenadores u otros miembros (ej., atención al cliente, interacciones con entrenadores o staff).\n"
        "4. 'sugerencia': Sugerencias específicas para mejorar cualquier aspecto del gimnasio (ej., nuevas clases, cambios de horario, nuevos servicios).\n"
        "5. 'dudas': Comentarios que expresan dudas, preguntas o incertidumbres sobre el gimnasio (ej., '¿A qué hora abren el fin de semana?', 'No sé si renovar mi membresía.').\n"
        "6. 'no-relevante': Comentarios que no son relevantes para la experiencia del gimnasio (ej., comentarios sobre el clima, temas no relacionados).\n\n"
        "Responde **únicamente** en formato JSON con dos claves: 'categoria' y 'sentimiento'. "
        "No incluyas texto o explicaciones adicionales. "
        "Aquí hay algunos ejemplos:\n"
        "- Input: 'Los baños están muy limpios y ordenados.'\n"
        "  Output: {'categoria': 'instalaciones', 'sentimiento': 'positivo'}\n"
        "- Input: 'Las máquinas de pesas están descompuestas.'\n"
        "  Output: {'categoria': 'material', 'sentimiento': 'negativo'}\n"
        "- Input: 'El entrenador es muy profesional y atento.'\n"
        "  Output: {'categoria': 'personal', 'sentimiento': 'positivo'}\n"
        "- Input: 'Me encantaría que agregaran más clases de yoga por la mañana.'\n"
        "  Output: {'categoria': 'sugerencia', 'sentimiento': 'positivo'}\n"
        "- Input: '¿A qué hora abren el fin de semana?'\n"
        "  Output: {'categoria': 'dudas', 'sentimiento': 'neutral'}\n"
        "- Input: 'Hoy hace mucho calor afuera.'\n"
        "  Output: {'categoria': 'no-relevante', 'sentimiento': 'neutral'}\n\n"
        "Ahora clasifica el siguiente comentario:"
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