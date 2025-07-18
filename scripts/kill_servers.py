import contextlib

from anaconda_ai import get_default_client
from anaconda_ai.exceptions import AnacondaAIException

client = get_default_client()

for server in client.servers.list():
    with contextlib.suppress(AnacondaAIException):
        server.stop()
    client.servers.delete(server.id)
