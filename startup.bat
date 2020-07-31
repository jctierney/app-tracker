docker build -t local/app-tracker-server .
docker run -it -p 8080:8080 --rm --name app-tracker-server-1 local/app-tracker-server