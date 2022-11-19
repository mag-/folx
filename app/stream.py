import asyncio
from pprint import pprint
import time
import requests

from mastodon import Mastodon, StreamListener
from .models import Status


class Listener(StreamListener):
    def on_update(self, status):
        s = Status.parse_obj(status)
        pprint(s)


def stream(stream_url):
    m = Mastodon(api_base_url="https://mastodon.social")
    listener = Listener()
    m.stream_public(listener, run_async=True, reconnect_async=True)


stream_url = "https://mastodon.social/api/v1/streaming/public"
stream(stream_url)
time.sleep(10)
