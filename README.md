run without docker:
```
pip install -r requirements
uvicorn main:app
```
check service:
```
curl -F "file=@data.csv" localhost:8000/graph --output out.png
```