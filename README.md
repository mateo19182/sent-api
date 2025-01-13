# Api

## Sentiment Analysis

The sentiment analysis endpoint provides emotional and subjective analysis of text:

```http
GET http://100.83.166.6:8000/sentiment/?text=your_text_here
```

Returns a JSON response with two metrics:

```json
{
    "polarity": -0.5,
    "subjectivity": 1.0
}
```

Where:

- `polarity`: Score from -1.0 (negative) to 1.0 (positive) indicating the emotional tone
- `subjectivity`: Score from 0.0 (factual) to 1.0 (opinionated) indicating how subjective the text is
