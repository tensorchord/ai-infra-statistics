import pypistats
from datetime import date


projects = ["pgvector", "pymilvus", "qdrant-client", "chromadb", "pinecone-client", "weaviate-client"]
unified_names = ["pgvector", "milvus", "qdrant", "chromadb", "pinecone", "weaviate"]

with open("vectordb-raw-data-pypi.csv", "a") as f:
    for i, project in enumerate(projects):
        data = pypistats.overall(project, total=True, format="numpy")
        total_downloads = data[-1][3]
        f.write(f"{date.today().strftime('%Y-%m-%d')},{total_downloads},{unified_names[i]},{project}\n")
