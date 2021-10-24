import sys
from redis import Redis

client = Redis()


def watch_links_data(name):
    print(f"Worker {name} started.")
    while True:
        link = client.blpop('links')
        print(link)
    print(f"worker {name} ended.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise KeyError("Worker name is required")
    watch_links_data(sys.argv[1])
    # print(sys.argv[1], len(sys.argv))
