docker build -t graph .
docker run -d --name graph -p 8765:80 graph