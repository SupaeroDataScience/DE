app:
	uvicorn app:app --reload
build:
	docker build -f Dockerfile -t eu.gcr.io/third-ridge-138414/yolo-v5:1.1 .
run:
	docker run --rm -p 8000:8000 eu.gcr.io/third-ridge-138414/yolo-v5:1.1
push:
	docker push eu.gcr.io/third-ridge-138414/yolo-v5:1.1
