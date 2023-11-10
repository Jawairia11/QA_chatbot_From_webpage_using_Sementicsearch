from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
from data import get_data
from op_ai import chat_bot

es_client = Elasticsearch(
    cloud_id = "First_deployment:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyRiZDJiODc4ZjVmOGM0NGExYWRmYjEyZDE0MGRhZTlmZiRiZTY1MzhiMWMzMWM0YzhkODc5OWJkYzk3NDMzNmE1OA==",
    basic_auth = ("elastic" , "8Uw7lIyse2lhRRBjZIa9eO7b")
)

def create_index(index_name):
    es_client.indices.create(
        index = index_name,
        mappings={
            "properties": {
                "id": {
                    "type": "text",
                },
                "data": {
                    "type": "text",
                },
                "embeddings": {
                    "type": "dense_vector",
                    "dims": 768,   # These are dimensions of our embeddings 
                }
            }
        }
    )
embedder = SentenceTransformer("multi-qa-mpnet-base-dot-v1")
def index_content(data, id , index_name):
    embeddings=embedder.encode(data)

    data={
        "id": id,
        "data": data ,
        "embeddings":embeddings
    }
    es_client.index(
        index = index_name,
        document=data 
    )
# create_index("wikipidia_data")  we have commented these after running 
# web_url= "https://en.wikipedia.org/wiki/Punjab"
# data = get_data(url = web_url)
# id = 0
# for chunks in data:
#     index_content(id = id , data = chunks , index_name = "wikipedia_data")
#     print(f"data for id ={id} is indexed in elastic search ")
#     id += 1

def query_data(query ,index_name ):
    embeddings = embedder.encode(query)
    results = es_client.search( 
    index = index_name ,
    source = ["data"],
    size = 2, 
    from_ = 0,
    query = {
        "script_score":{
            "query":{
                "match":{
                    "data":query
                }

            },
            "script":{
                "source": """ (cosineSimilarity(params.query_vector, "embeddings")+ 1)*params.encoder_boost + _score
                """ ,
                "params":{
                    "query_vector": embeddings,
                    "encoder_boost":10
                },
            },
        }
    }
    )
    #query="What is the capital of Punjab?"    ;later on after running index changed the position and moved these lines below
    #query_data(query,  "wikipedia-data")

    hits = results["hits"]["hits"]
    data_results = []
    for hit in hits:
        data_results.append({
            "Data": hit["_source"]["data"]
        })
    return data_results

query="What is the capital of Punjab?"
data = query_data(query,  "wikipedia_data")
#print(data)

answer = chat_bot(question = query , info = data)
print(answer)

