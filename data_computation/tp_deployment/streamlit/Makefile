app:
	streamlit run app.py
build:
	docker build -f Dockerfile -t eu.gcr.io/third-ridge-138414/yolo-v5-streamlit:1.4 .
run:
	docker run --rm -p 8501:8501 eu.gcr.io/third-ridge-138414/yolo-v5-streamlit:1.4
push:
	docker push eu.gcr.io/third-ridge-138414/yolo-v5-streamlit:1.4
