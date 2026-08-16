# FastApi projects
some of my fastapi projects

## MangaDex cli
A cli application to search and get info about mangas
Built using Tenrai API, completely compatible with Jikan API
### How to use
Search an anime (to get the MAL (MyAnimeList) id)
```bash
    python manga_cli.py search "One piece"
```

Info about the anime using MAL id
```bash
    python manga_cli.py info "13" # mal id of onepiece, find it using search command
```

Compare multiple animes using MAL id
-# sorts the anime passed with highest score and creates a comparison graph (11 12 13 are the mal ids of big 3 animes)
```bash
    python manga_cli.py compare 11 12 13
```