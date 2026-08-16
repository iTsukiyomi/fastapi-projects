# FastApi projects
A collection of my fastapi projects and experiments.

---

## Projects

### MangaDex cli
A cli application for searching, comparing and getting information about a manga.

**Built with:**
- Python
- Pandas
- Matplotlib (for comparison charts)
- TenRai API
- Compatible with Jikan API

#### Usage

**Search for a manga:**

```bash
    python manga_cli.py search "One piece"
```
> *Prints the top 5 results for the anime entered with its MAL id.*

**Info about the manga using MAL id:**

```bash
    python manga_cli.py info "13" 
```
> *Prints a formatted info about the anime (13 is the MAL id, found using search command above).*

**Compare multiple animes using MAL id:**

```bash
    python manga_cli.py compare 11 12 13
```
> *Sorts the anime passed with the highest score and creates a comparison graph. (using pandas and matplotlib)*

#### Installation

```bash
    git clone https://github.com/iTsukiyomi/fastapi-projects
    cd <project-directory/mangadex>

    uv sync
```

#### Requirements

- Python 3.x
- UV
- Internet Connection
- Some brain
