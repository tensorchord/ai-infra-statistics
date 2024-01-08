import pypistats
from datetime import date


projects = ["llama-cpp-python", "gpt4all"]
unified_names = ["llama.cpp", "gpt4all"]

with open("inference-local-raw-data-pypi.csv", "a") as f:
    for i, project in enumerate(projects):
        data = pypistats.overall(project, total=True, format="numpy")
        total_downloads = data[-1][3]
        f.write(f"{date.today().strftime('%Y-%m-%d')},{total_downloads},{unified_names[i]},{project}\n")
