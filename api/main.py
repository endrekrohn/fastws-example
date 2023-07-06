from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI
from fastws import Client, Message

from api.service import service


@asynccontextmanager
async def lifespan(app: FastAPI):
    service.setup(app)
    yield


app = FastAPI(lifespan=lifespan)


@app.websocket("/")
async def fastws_stream(client: Annotated[Client, Depends(service.manage)]):
    await service.serve(client)


@app.post("/{topic}", tags=["Alert"])
async def alert_on_topic(topic: str, message: str):
    await service.server_send(
        Message(type="feature_2.alert", payload={"message": message}),
        topic=topic,
    )
    return "ok"
