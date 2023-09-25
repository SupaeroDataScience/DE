import base64
import io
from pathlib import Path

import requests
from PIL import Image

url = "http://localhost:8000/{path}"

## Test de requêtes de bases

# On effectue des requêtes GET sur `/health` et `/models` pour vérifier que tout répond bien

response = requests.get(url.format(path="health"))

assert response.status_code == 200

print("TEST ALIVE PASSED")

response = requests.get(url.format(path="models"))

assert response.status_code == 200

response = response.json()

assert response == ["yolov5s", "yolov5m", "yolov5l"]

print("TEST MODELS PASSED")

## Requête de processing

# On effectue une requête de processing qui est une requête POST sur `/predict` qui contient le nom du modèle ainsi qu'une image à traiter encodée sous la forme de string (on utilise l'encodage base64)

# ```json
# {
#     "model":"yolov5s",
#     "image":"..."
# ```

path = Path("cats.jpg")

# ouverture de l'image
image = Image.open(path)

# encodage
with io.BytesIO() as buffer:
    image.save(buffer, format="PNG")
    buffer: str = base64.b64encode(buffer.getvalue()).decode("utf-8")

    # creation de la "payload" de la requête
    data = {"model": "yolov5s", "image": buffer}

    # envoi de la requête
    response = requests.post(url.format(path="predict"), json=data)

assert response.status_code == 200

response = response.json()

assert "time" in response

assert "model" in response

print(response)