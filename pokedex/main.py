import requests
import argparse


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

def main():
    parser = argparse.ArgumentParser(description="Pokedex CLI")
    parser.add_argument("name", type=str, help="pokemon name or id")
    args = parser.parse_args()

    poke = get_pokemon(args.name)
    if poke is None:
        return None
    print(f"#{poke['id']}: {poke["name"].title()}")
    types = [t["type"]["name"] for t in poke["types"]]
    print(f"Types: {" ,".join(types)}")
    for entry in poke["stats"]:
        print(f"{entry["stat"]["name"]}: {entry["base_stat"]}")

if __name__=="__main__":
    main()