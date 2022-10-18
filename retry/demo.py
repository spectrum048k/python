import random
import logging
from requests.exceptions import HTTPError
from retry import retry

logging.basicConfig()

@retry(HTTPError, tries=10, delay=0.1, backoff=2)
def pretend_request():
    if random.random() < 0.01:
        raise HTTPError("Something went wrong!")
    return {"status": "alive"}

# retry decorator will handle retry logic for us 
for _ in range(500):
    pretend_request()
