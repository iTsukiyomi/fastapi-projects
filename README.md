# FastApi projects
A collection of my fastapi projects and experiments.

---

## MangaDex cli
A cli application for searching, comparing and getting information about a manga.

### How to use

Search for a manga:

```bash
python manga_cli.py search "One piece"
```
> *Prints the top 5 results for the anime entered with its MAL id.*

Info about the manga using MAL id:

```bash
python manga_cli.py info "13" 
```
> *Prints a formatted info about the anime (13 is the MAL id, found using search command above).*

Compare multiple animes using MAL id:

```bash
python manga_cli.py compare 11 12 13
```
> *Throws multiple manga into a graph and lets math decide which one is better.*

## Features

- Search for manga
- Get manga info
- Compare multiple manga
- Generate comparison chart
- Pretend this is useful contribution to society

## Tech stack

- Python
- FastAPi
- Pandas
- Matplotlib (for comparison charts)
- TenRai API 
- Compatible with Jikan API


#### Requirements

- Python 3.x
- UV
- Internet Connection
- Some brain
