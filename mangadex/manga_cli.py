import argparse
from manga_api import search_manga, get_manga_details, format_manga_summary

def main():
    parser = argparse.ArgumentParser(description="Mangadex api")
    subparsers = parser.add_subparsers(dest="command")

    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("query", type=str)

    info_parser = subparsers.add_parser("info")
    info_parser.add_argument("mal_id", type=int)

    args = parser.parse_args()

    if args.command == "search":
        res = search_manga(args.query)
        if not res:
            return print("No results found")
        for manga in res:
            return print(f"#{manga['mal_id']} - {manga['title']}")
    elif args.command == "info":
        result = get_manga_details(args.mal_id)
        if result is None:
            return
        print(format_manga_summary(result))
    else:
        parser.print_help()


if __name__=="__main__":
    main()