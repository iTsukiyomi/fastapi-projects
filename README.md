# FastApi projects
some of my fastapi projects

## MangaDex cli
A cli application to search and get info about mangas.\n
Built using Tenrai API, completely compatible with Jikan API.
### How to use
Search an anime (to get the MAL (MyAnimeList) id)
```bash
    python manga_cli.py search "One piece"
```
> *Prints the top 5 results for the anime entered with its MAL id.*

Info about the anime using MAL id
```bash
    python manga_cli.py info "13" 
```
> *Prints a formatted info about the anime (13 is the MAL id, found using search command above).*

Compare multiple animes using MAL id
```bash
    python manga_cli.py compare 11 12 13
```
> *Sorts the anime passed with the highest score and creates a comparison graph. (using pandas and matplotlib)*