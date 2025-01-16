#!/bin/bash

# Base URL of the API
BASE_URL="http://localhost:8000"

# Test texts in Spanish (simulating gym feedback)
declare -a TEST_TEXTS=(
    "El gimnasio está muy limpio y bien organizado. ¡Me encanta!"
    "Las máquinas de pesas están descompuestas y nadie las repara."
    "El entrenador fue muy grosero conmigo durante la sesión."
    "Hoy hace mucho calor afuera, no sé si ir al gimnasio."
    "Me encanta la nueva clase de spinning, el instructor es muy motivador."
    "El baño está sucio y no hay papel higiénico."
    "No me gusta cómo me miran los otros miembros del gimnasio."
    "El estacionamiento está lleno y no hay espacio para mi coche."
    "La música en el gimnasio es demasiado alta, no puedo concentrarme."
    "El gimnasio cierra muy temprano los fines de semana."
)

# # Function to test the /sentiment/ endpoint
# test_sentiment_endpoint() {
#     echo "Testing /sentiment/ endpoint..."
#     for text in "${TEST_TEXTS[@]}"; do
#         echo "Text: $text"
#         curl -s -G --data-urlencode "text=$text" "$BASE_URL/sentiment/"
#         echo -e "\n"
#     done
# }

# Function to test the /analyze/ endpoint
test_analyze_endpoint() {
    echo "Testing /analyze/ endpoint..."
    for text in "${TEST_TEXTS[@]}"; do
        echo "Text: $text"
        curl -s -G --data-urlencode "text=$text" "$BASE_URL/analyze/"
        echo -e "\n"
    done
}

# Run the tests
# test_sentiment_endpoint
test_analyze_endpoint

echo "All tests completed."