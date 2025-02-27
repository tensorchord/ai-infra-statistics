import pypistats
from datetime import date


projects = ["vllm", "bentoml", "mosec", "xinference", "openllm", "sglang"]
unified_names = ["vllm", "bentoml", "mosec", "xinference", "openllm", "sglang"]

with open("framework-inference-raw-data-pypi.csv", "a") as f:
    for i, project in enumerate(projects):
        data = pypistats.overall(project, total=True, format="numpy")
        total_downloads = data[-1][3]
        f.write(f"{date.today().strftime('%Y-%m-%d')},{total_downloads},{unified_names[i]},{project}\n")
