
def createIndex(es) :
    es.indices.create(index="products", ignore=400)

def insertDataInIndex(es) :
    # Sample product data
    product_1 = {
        "name": "iPhone 15",
        "category": "Electronics",
        "price": 999.99,
        "in_stock": True
    }
    product_2 = {
        "name": "iPhone 15",
        "category": "Electronicss",
        "price": 999.99,
        "in_stock": True
    }

    # Insert into Elasticsearch
    es.index(index="products", id=1, document=product_1)
    es.index(index="products", id=2, document=product_2)
    es.indices.refresh(index="products") 
    print("✅ Document inserted!")

def searchData(es):
    query = {
    "query": {
        "match": {"category": "Electronics"}
        }
    }
    result = es.search(index="products", body=query)
    print("🔍 Search Results:", result["hits"]["hits"])

def searchDataWithInserting(es):
    createIndex(es)
    insertDataInIndex(es)
    searchData(es)

def searchDataWithoutInserting(es):
    searchData(es)
