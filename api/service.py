from fastws import FastWS

from api.feature_0 import subscribe
from api.feature_1 import ping
from api.feature_2 import alert

service = FastWS(title="FastWS - Broker")

service.include_router(subscribe.router)
service.include_router(ping.router)
service.include_router(alert.router)


@service.send("ping", reply="pong")
def application_ping():
    ...
