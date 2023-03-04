# Context
Technical test by Giskard : https://github.com/lioncowlionant/developer-test

# How to try this app
```bash
# run this app
uvicorn main:app --reload
```

```bash
# try this app
curl -X POST -H "Content-Type: application/json" -d '{"millennium_falcon" : {"autonomy": 6,"departure": "Tatooine","arrival": "Endor","routes_db": "universe.db"},"empire": {"countdown": 8,"bounty_hunters": [{"planet": "Hoth","day": 6},{"planet": "Hoth","day": 7},{"planet": "Hoth","day": 8}]}}' http://localhost:8000/give_me_the_odds
```

# Tests
## Run tests (unit tests & integration tests)
```bash
pytest
```

## Run coverage
### Generate sources
```bash
coverage run --source=./.. -m pytest
```

### Generate report
```bash
# Generate html report (open to index.html)
coverage html 

# Generate report in your command line
coverage report
```