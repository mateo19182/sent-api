# Sentiment Api

This API provides sentiment analysis and text classification capabilities for Spanish text encapsulated in docker.

Uses <https://github.com/SamuelTallet/alpine-llama-cpp-server> for running a llm in cpu and <https://github.com/pysentimiento/pysentimiento>

## Todo

- secure api
- add vectordb for rag

## Endpoints

### GET /sentiment/

Analyzes the sentiment of Spanish text.

**Parameters:**

- `text` (string, required): The Spanish text to analyze

**Returns:**

```json
{
    "sentiment": "string",
    "probabilities": {
        "NEG": float,
        "NEU": float,
        "POS": float
    }
}
```

### GET /analyze/

Classifies gym-related feedback into predefined categories.

**Parameters:**

- `text` (string, required): The feedback text to analyze

**Returns:**

```json
{
    "category": "string"
}
```

Categories include:

- `queja-material`: Equipment/facility complaints
- `queja-personal`: Staff-related complaints
- `sugerencia`: Suggestions/positive feedback
- `dudas`: Questions/doubts
- `no-relevante`: Irrelevant feedback
