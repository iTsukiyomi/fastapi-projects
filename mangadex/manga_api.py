import requests
import os
import json

BASE_URL = "https://api.tenrai.org/v1"
CACHE_DIR = "mangadex_cache"

def search_manga(query, limit = 5):
    try:
        response = requests.get(f"{BASE_URL}/manga", params={"q": query, "limit": limit}, timeout=20)

        response.raise_for_status()
        return response.json()['data']
    except requests.exceptions.RequestException as e:
        print(f"search failed: {e}")
        return []

def get_manga_details(mal_id):
    try:
        response = requests.get(f"{BASE_URL}/manga/{mal_id}", timeout=20)
        response.raise_for_status()
        return response.json()['data']
    except requests.exceptions.HTTPError:
        print(f"No manga found for {mal_id}")
        return None
    except requests.exceptions.RequestException:
        return None

def get_manga_details_cached(mal_id, fetch_func):
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache_path = os.path.join(CACHE_DIR, f"manga-{mal_id}.json")
    
    if os.path.exists(cache_path):
        with open(cache_path, "r") as f:
            print(f"loaded manga {mal_id} from cache")
            return json.load(f)
    data = fetch_func(mal_id)
    if data is not None:
        with open(cache_path, "w") as f:
            json.dump(data, f)
    return data

def format_manga_summary(manga):
    title = manga.get("title", "Unknown title")
    authors = manga.get("authors", [])
    author = " ,".join((a['name'] for a in authors) if authors else "Unknown author")
    synopsis = manga.get("synopsis", "Unknown description")
    chapters = manga.get("chapters", "Unknown chapters")
    status = manga.get("status", "Unknown status")
    genres = manga.get("genres", [])
    genre = " ".join((genre['name'] for genre in genres) if genres else "Unknown genres")

    return f"Title: {title}- by {author}\nDescription: {synopsis}\nChapters:{chapters}\nStatus: {status}\nGenre: {genre}"
