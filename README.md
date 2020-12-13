run without docker:
```
pip install -r requirements
uvicorn main:app
```
run with docker:
```
chmod +x run.sh
./run.sh
```

check service:
```
curl -F "file=@data.csv" localhost:8000/graph --output out.png
```