# Team Packaging of ML Model

## Objectif

Packager un modèle de machine learning derrière une webapplication pour pouvoir la déployer sur le web et servir des prédictions à des utilisateurs

Le modèle: Un détecteur d'objets sur des photographies "standard" supposé marcher en temps réel, qui sort des "bounding boxes" autour des objets détecté dans des images

![image](cats_yolo.png)
 
Le papier vaut la lecture

https://pjreddie.com/media/files/papers/YOLOv3.pdf

On récupère la version disponible sur torchhub https://pytorch.org/hub/ultralytics_yolov5/ qui correspond à ceci https://github.com/ultralytics/yolov5

Voici une petite explication de l'historique https://medium.com/towards-artificial-intelligence/yolo-v5-is-here-custom-object-detection-tutorial-with-yolo-v5-12666ee1774e

On se propose ici de wrapper 3 versions du modèle (S,M,L) qui sont 3 versions +/- complexes du modèle YOLO-V5, afin de pouvoir comparer les performances et les résultats

![models](https://user-images.githubusercontent.com/26833433/97808084-edfcb100-1c64-11eb-83eb-ffed43a0859f.png)

## Déroulement

- Transformer un notebook de prédiction en “WebApp” en remplissant `app.stub.py` et en le renommant en `app.py`
- Tester sa webapp localement
- Packager l'application sous forme d'une image docker
- Tester son image docker localement
- Uploader le docker sur Google Container Registry

## Développement de app.py

Il y a deux fonctions à compléter en s'inspirant du notebook `inference.ipynb`. Grace au typage de python, vous avez les types d'entrée et de sortie des deux fonctions

La première prend un tableau de type (left, top, right, bottom, confidence, class_index) et une liste de noms de classes et créée une liste d'objets `Detection` (voir le code pour la création des objets détection)

La seconde fonction doit charger un modèle via torchhub en fonction de son nom (voir le docker)

```python
# !!!! FILL ME
def parse_predictions(predictions: np.ndarray, classes: [str]) -> List[Detection]:
    raise NotImplementedError


# !!!! FILL ME
def load_model(model_name: str):
    """"""
    raise NotImplementedError
```

Ensuite, vous pouvez executer les fonctions de chargement de modèle, par exemple

```python
# !!!! FILL ME
# This is a dictionnary that must contains a model for each key (model names), fill load model
# example: for model_name in MODEL_NAMES: MODELS[model_name] = load_model(model_name)
# You can also lazily load models only when they are called to avoid holding 3 models in memory
MODELS = {}
for model_name in MODEL_NAMES:
    MODELS[model_name] = load_model(model_name)
```

Enfin, il s'agit d'écrire un code qui effectue une prédiction à partir d'une image PIL et de mesurer le temps
(indice: `import time` et `t0 = time.time()` ...) de prédiction

```python
# RUN THE PREDICTION, TIME IT
predictions = ...
# Post processing
classes = predictions.names
predictions = predictions.xyxy[0].numpy()
```

Le résultat de predictions est un tableau numpy composé des colonnes `left, top, right, bottom, confidence, class_index`

Il s'agit ensuite de transformer ces predictions en `[Detection]`

```python
# Create a list of [DETECTIONS] objects that match the detection class above, using the parse_predictions method
detections = parse_predictions(predictions, classes)
```

## Tester son application

Dans un terminal, vous pouvez faire `uvicorn app:app --reload` pour lancer la webbapp FastAPI qui sert le modèle,

Ensuite vous pouvez lancer le notebook tests pour vérifier que tout fonctionne correctement

Ensuite vous pouvez passer à l'étape suivante

## Construire le docker

```bash
PROJECT_ID=$(gcloud config get-value project 2> /dev/null)
docker build -t eu.gcr.io/${PROJECT_ID}/{your app name}:{your version} -f Dockerfile . 
```

### Tester le docker

Au lieu de faire `uvicorn`, vous pouvez lancer le docker localement et le tester de la même façon avec le notebook

```bash
PROJECT_ID=$(gcloud config get-value project 2> /dev/null)
docker run --rm -p 8000:8000 eu.gcr.io/${PROJECT_ID}/{your-name}-{your app name}:{your version}
```

### Pusher le docker sur google container registry

```bash
gcloud auth configure-docker
docker push eu.gcr.io/${PROJECT_ID}/{your-name}-{your app name}:{your version}
```

Si vous devez mettre à jour le docker, il faut incrémenter la version pour le déploiement

## Liens Utiles

https://fastapi.tiangolo.com/
https://requests.readthedocs.io/en/master/
https://testdriven.io/blog/fastapi-streamlit/
