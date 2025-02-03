# Api

This API provides sentiment analysis and text classification capabilities for Spanish text encapsulated in docker.

Uses <https://github.com/SamuelTallet/alpine-llama-cpp-server> and <https://github.com/pysentimiento/pysentimiento>

## Todo

- secure api
- add chat with vectordb for timetables

## Openrouter

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

## Upload registry

docker build -t registry.innplay.site/sent-api:latest ./app
docker push registry.innplay.site/sent-api:latest

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
