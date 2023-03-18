import socket

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    host_name = socket.gethostname()
    return {"message": f"Hello World, {host_name}"}
