# Team Companion UX webapp

## Objectif

Créer une application "compagnon" qui permet de faire des requêtes à un modèle de façon ergonomique et de visualiser les résultats

## Déroulement

- Remplir `app.stub.py`, le renommer en `app.py` en remplissant les bons champs (s'aider des notebooks dans `app/`) et en créant des jolies visualisations
- Tester sa webapp localement (il y a un mode test)
- Packager l'application sous forme d'une image docker
- Tester son image docker localement
- Uploader le docker sur Google Container Registry

## Guide de développement

La majorité des fonctions de requête sont déjà implémentées, il reste à faire les fonctions d'entrées utilisateurs et la visualisation

- Entrée: Utilisation de `st.radio` et `st.file_uploader`: 

https://docs.streamlit.io/en/stable/getting_started.html

https://docs.streamlit.io/en/stable/api.html#streamlit.radio
 
https://docs.streamlit.io/en/stable/api.html#streamlit.file_uploader

```python
st.markdown("## Inputs")
st.markdown("Select your model (Small, Medium or Large)")

model_name = st.radio(label="Model Name", options=["yolov5s", "yolov5m", "yolov5l"])

st.markdown("Upload an image")

image_file = st.file_uploader(label="Image File", type=["png", "jpg", "tif"])
```

- Visualisations

Exemple de code qui imite le notebook de prédiction pour dessiner sur une image PIL

```python
def draw_preds(image: Image, detections: [Detection]):

    class_names = list(set([detection.class_name for detection in detections]))

    image_with_preds = image.copy()

    # Define colors
    colors = plt.cm.get_cmap("viridis", len(class_names)).colors
    colors = (colors[:, :3] * 255.0).astype(np.uint8)

    # Define font
    font = list(Path("/usr/share/fonts").glob("**/*.ttf"))[0].name
    font = ImageFont.truetype(font=font, size=np.floor(3e-2 * image_with_preds.size[1] + 0.5).astype("int32"))
    thickness = (image_with_preds.size[0] + image_with_preds.size[1]) // 300

    # Draw detections
    for detection in detections:
        left, top, right, bottom = detection.x_min, detection.y_min, detection.x_max, detection.y_max
        score = float(detection.confidence)
        predicted_class = detection.class_name
        class_idx = class_names.index(predicted_class)

        label = "{} {:.2f}".format(predicted_class, score)

        draw = ImageDraw.Draw(image_with_preds)
        label_size = draw.textsize(label, font)

        top = max(0, np.floor(top + 0.5).astype("int32"))
        left = max(0, np.floor(left + 0.5).astype("int32"))
        bottom = min(image_with_preds.size[1], np.floor(bottom + 0.5).astype("int32"))
        right = min(image_with_preds.size[0], np.floor(right + 0.5).astype("int32"))
        print(label, (left, top), (right, bottom))

        if top - label_size[1] >= 0:
            text_origin = np.array([left, top - label_size[1]])
        else:
            text_origin = np.array([left, top + 1])

        # My kingdom for a good redistributable image drawing library.
        for r in range(thickness):
            draw.rectangle([left + r, top + r, right - r, bottom - r], outline=tuple(colors[class_idx]))
        draw.rectangle([tuple(text_origin), tuple(text_origin + label_size)], fill=tuple(colors[class_idx]))
        draw.text(text_origin, label, fill=(0, 0, 0), font=font)

        del draw

    return image_with_preds
```

Utilisation (exemple)

```python
    if test_mode_on:
        st.warning("Simulating a dummy request to {}".format(model_url))
        result = ...  # call the proper function
    else:
        result = ...  # call the proper function

    st.balloons()

    st.markdown("## Display")

    st.text("Model : {}".format(result.model))
    st.text("Processing time : {}s".format(result.time))

    image_with_preds = draw_preds(image, result.detections)
    st.image(image_with_preds, width=1024, caption="Image with detections")

    st.markdown("### Detection dump")
    for detection in result.detections:
        st.json(detection.json())
```

## Tester son application localement

- installer les dépendances (`pip install -r requirements.txt`)
- `streamlit run app.py`, qui créée l'application interactive sur le port 8501 de la machine (localhost:8501)
- Si vous mettez l'application à jour, le serveur de développement se relance automatiquement

## Docker

### Construire le docker

```bash
PROJECT_ID=$(gcloud config get-value project 2> /dev/null)
docker build -t eu.gcr.io/${PROJECT_ID}/{your app name}:{your version} -f Dockerfile .
```

### Tester le docker

Au lieu de faire `streamlit run app.py`, vous pouvez lancer le docker localement et aller sur localhost:8501 pour tester le docker

```bash
PROJECT_ID=$(gcloud config get-value project 2> /dev/null)
docker run --rm -p 8501:8501 eu.gcr.io/${PROJECT_ID}/{your app name}:{your version}
```

### Pousser le docker sur google container registry

```bash
gcloud auth configure-docker
docker push eu.gcr.io/${PROJECT_ID}/{your app name}:{your version}
```

## Liens Utiles

https://docs.streamlit.io/en/stable/getting_started.html
