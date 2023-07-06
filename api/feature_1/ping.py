from fastws import OperationRouter

router = OperationRouter(prefix="feature_0.")


@router.send("ping")
async def send_ping() -> str:
    return "pong"
