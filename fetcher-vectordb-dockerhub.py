import requests
from datetime import date

url = "https://hub.docker.com/v2/repositories/{0}/{1}"

images = ["pgvector/pgvector", "tensorchord/pgvecto-rs", "milvusdb/milvus", "qdrant/qdrant", "chromadb/chroma", "semitechnologies/weaviate"]
unified_names = ["pgvector", "pgvecto.rs", "milvus", "qdrant", "chromadb", "weaviate"]

with open("vectordb-raw-data-dockerhub.csv", "a") as f:
    for i, image in enumerate(images):
        org, repo = image.split("/")
        image_url = url.format(org, repo)
        print("fetching", image_url)
        r = requests.get(url.format(org, repo))
        data = r.json()
        total_downloads = data["pull_count"]
        f.write(f"{date.today().strftime('%Y-%m-%d')},{total_downloads},{unified_names[i]},{image}\n")
