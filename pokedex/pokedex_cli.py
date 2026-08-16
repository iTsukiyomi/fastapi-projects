import requests
import argparse
import json
import os

CACHE_DIR = "pokedex_cache" 


BASE_URL = "https://pokeapi.co/api/v2"

def get_pokemon(name_or_id):
    try:
        response = requests.get(f"{BASE_URL}/pokemon/{name_or_id}", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
        print(f"{name_or_id} not found")
        return None
    except requests.exceptions.RequestException as e:
        print(e)
        return None

def get_poke_cached(name_or_id, fetch_func):
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache_path = os.path.join(CACHE_DIR, f"{name_or_id}.json")

    if os.path.exists(cache_path):
        with open(cache_path, "r") as f:
            print(f"loaded {name_or_id} from cache")
            return json.load(f)
    data = fetch_func(name_or_id)
    if data is not None:
        with open(cache_path, "w") as f:
            json.dump(data, f)
    return data

def main():
    parser = argparse.ArgumentParser(description="Pokedex CLI")
    parser.add_argument("name", type=str, help="pokemon name or id")
    args = parser.parse_args()

    poke = get_poke_cached(args.name, get_pokemon)
    if poke is None:
        return None
    print(f"#{poke['id']}: {poke["name"].title()}")
    types = [t["type"]["name"] for t in poke["types"]]
    print(f"Types: {" ,".join(types)}")
    for entry in poke["stats"]:
        print(f"{entry["stat"]["name"]}: {entry["base_stat"]}")

if __name__=="__main__":
    main()