import matplotlib.pyplot as plt
from manga_api import get_manga_details_cached, get_manga_details


def manga_compare(mal_ids: list[int]):
    comparison = []
    for id in mal_ids:
        manga = get_manga_details_cached(id, get_manga_details)
        if manga is None:
            continue
        comparison.append({
            "name": manga.get("title", "unknown"),
            "chapters": manga.get("chapters") or 0,
            "volumes": manga.get("volumes") or 0,
            "score": manga.get("score") or 0
        })
    return comparison

def plot_comparison(df, field):
    short_titles = df["name"][:20]
    plt.figure(figsize=(10,6))
    plt.bar(short_titles, df[field])
    plt.ylabel(field.capitalize())
    plt.title(f"Manga {field.capitalize()} Comparison")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(f"{field}_comparison.png")
    plt.close()
