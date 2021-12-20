from fastapi import FastAPI
from datetime import datetime
import socket
app = FastAPI()

@app.get("/")
async def root():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    return {"timestamp": current_time, "IP": IPAddr}
