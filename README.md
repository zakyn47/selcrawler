# selcrawler

selcrawler is basic selenium webcrawler
features:
- crawl webpages
- gather links
- gather email adresses
- gather phone numbers

## Installation


clone repository
```bash
git clone https://github.com/zakyn47/selcrawler.git
```
create virtual env
```bash
python3 -m venv <virtualenv_name>
```
activate virtual environment
```bash
source <virtualenv_name>/bin/activate
```
install requirements
```bash
pip install -r requirements.txt
```



## Usage

```bash
python3 crawler.py <starting_url> <number of pages>
```

## Example
```bash
python3 crawler.py www.seznam.cz 10
```