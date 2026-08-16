import argparse
import pandas as PD
from manga_api import search_manga, get_manga_details, format_manga_summary, get_manga_details_cached
from manga_compare import manga_compare, plot_comparison


def main():
    parser = argparse.ArgumentParser(description="Mangadex api")
    subparsers = parser.add_subparsers(dest="command")

    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("query", type=str)

    info_parser = subparsers.add_parser("info")
    info_parser.add_argument("mal_id", type=int)

    compare_parser = subparsers.add_parser("compare")
    compare_parser.add_argument("mal_ids", type=int, nargs="+")

    args = parser.parse_args()

    if args.command == "search":
        res = search_manga(args.query)
        if not res:
            return print("No results found")
        for manga in res:
            return print(f"#{manga['mal_id']} - {manga['title']}")
    elif args.command == "info":
        result = get_manga_details_cached(args.mal_id, get_manga_details)
        if result is None:
            return
        print(format_manga_summary(result))
    elif args.command == "compare":
        manga_list = manga_compare(args.mal_ids)
        if manga_list is None:
            return
        df = PD.DataFrame(manga_list)
        plot_comparison(df, "score")
        return print(df.sort_values("score", ascending=False).to_string(index=False))
    else:
        parser.print_help()


if __name__=="__main__":
    main()