from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from starlette.responses import StreamingResponse
import matplotlib.pyplot as plt
import numpy as np
import io
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/graph",)
async def scatter_plot(file: UploadFile = File(...)):
    s = await file.read()
    data = np.genfromtxt(io.StringIO(s.decode()))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
    ax1.scatter(data[:, 0], data[:, 1])
    ax2.scatter(data[:, 0]/data[:, 0].max(), data[:, 1]/data[:, 1].max())

    pic_buf = io.BytesIO()
    plt.savefig(pic_buf, format='png')
    pic_buf.seek(0)

    return StreamingResponse(pic_buf, media_type="image/png")


@app.get("/graph", response_class=HTMLResponse)
def upload_btn():
    return """
    <html>
        <body>
            <div align="center">
                Use post method to send csv and get pictures
            <div/>
        </body>
    </html>
    """