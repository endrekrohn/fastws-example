import logging
from fastws import Client, OperationRouter, FastWS
from pydantic import BaseModel

router = OperationRouter(prefix="feature_1.")


class SubscriptionPayload(BaseModel):
    topic: str


class SubscriptionResponse(BaseModel):
    detail: str
    topics: set[str]


@router.send("subscribe")
async def subscribe_to_topic(
    payload: SubscriptionPayload,
    client: Client,
    app: FastWS,
) -> SubscriptionResponse:
    """
    Subscribe to a topic.
    """
    client.subscribe(payload.topic)
    logging.info(f"app now has clients: {app.connections}")
    return SubscriptionResponse(
        detail=f"Subscribed to {payload.topic}", topics=client.topics
    )


@router.send("unsubscribe")
async def unsubscribe_from_topic(
    payload: SubscriptionPayload,
    client: Client,
) -> SubscriptionResponse:
    """
    Unsubscribe from a topic.
    """
    client.unsubscribe(payload.topic)
    return SubscriptionResponse(
        detail=f"Unubscribed to {payload.topic}", topics=client.topics
    )
