import os

CLUSTER_VERSION_OPERATOR_ID: str = "version"
CLUSTER_POLLING_SECONDS_INTERVAL: int = os.environ.get("CLUSTER_POLLING_SECONDS_INTERVAL", 120)
