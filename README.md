# article scraper

### Setting up
----

Cloning the repo:
```sh
git clone git@github.com:jamesesguerra/article_scraper.git
```

Making a virtual env:
```sh
python -m venv venv
```

Activating the env:
```sh
# windows
\venv\Scripts\activate

# unix
source venv/bin/activate
```

Installing dependencies:
```sh
pip install -r article_scraper/requirements.txt
```

Change dirs:
```sh
cd article_scraper && article_scraper
```

### Usage
----

Run `main.py` and enter company number:

Choices: 
- Pilipino Star Ngayon [0]
- ABS-CBN News [1]
- GMA Network (Balitambayan) [2]
```sh
python main.py
```

\* CSV files are placed inside `article_scraper/csv_files/`

### Combining CSV files
---

Run `combine_csv.py` in `article_scraper/`:
```sh
# article_scraper/

python combine_csv.py
```

This combines all the CSV files in `article_scraper/csv_files` into one CSV file named `combined_csv.csv`.


