docker build -t graph .
docker run -d --name graph -p 8765:8000 graph
docker logs graph

# example of using
# curl -F "file=@data.csv" where_service_was_deployed/graph --output out.png