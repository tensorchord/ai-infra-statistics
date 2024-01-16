import pypistats
from datetime import date


projects = ["leptonai", "modal", "fireworks-ai", "banana-dev", "together"]
unified_names = ["lepton.ai", "modal.com", "fireworks.ai", "banana.dev", "toghther.ai"]

with open("inference-raw-data-pypi.csv", "a") as f:
    for i, project in enumerate(projects):
        data = pypistats.overall(project, total=True, format="numpy")
        total_downloads = data[-1][3]
        f.write(f"{date.today().strftime('%Y-%m-%d')},{total_downloads},{unified_names[i]},{project}\n")
