# Mineral Catalog TH

## NOTE: THIS IS THE BRANCH FOR PROJECT 8
### To view project 6, go [here](https://github.com/MrLotU/MineralCatalogTHtree/Project6)

Before running the app, you have to load up the database. First, run `python manage.py migrate`

Than, open the django shell with `python manage.py shell` and execute the following:
```py
import loaddb 
loaddb.load_json()
```

After that, you're good to go to run the project!

## Tests
To check the test coverage, run `coverage run manage.py test`