Run container:
docker build --no-cache --tag=nginx-test:latest .
docker run -d -p 8080:80 nginx-test

docker run -p 8080:80 -p 8000:8000 nginx-test