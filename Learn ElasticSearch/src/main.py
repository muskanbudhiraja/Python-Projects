from elasticsearch import Elasticsearch
from src.search import searchDataWithInserting


def start() -> None:
    es = Elasticsearch("http://localhost:9200")

    # Check if Elasticsearch is connected
    print(es.ping())  # Should return True
    searchDataWithInserting(es)

if __name__ == "__main__":
    start()