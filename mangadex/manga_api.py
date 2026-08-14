import requests

BASE_URL = "https://api.tenrai.org/v1"

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
