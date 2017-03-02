# pandazzz
A simple experiment to serve content of tabular files through a REST API with Django and pandas.

## Getting Started

Clone the repo, create a virtualenv, and install dependencies:

```
pip install -r requirements.txt
```

Instantiate database and apply migrations:

```
./manage.py migrate
```

Launch the Django development server:

```
./mangage.py runserver
```

## Retrieving Data

A sample data file (`data/movies.csv`) is hard-coded and can be queried by field:

```
http://localhost:8000/data?format=json&fields=Name,ReleaseDate,AvgRating
```

This will return JSON that includes the selected fields:

```
[{"Name":"Toy Story (1995)","ReleaseDate":1995,"AvgRating":4.15},{"Name":"Jumanji (1995)","ReleaseDate":1995,"AvgRating":3.2},{"Name":"Grumpier Old Men (1995)","ReleaseDate":1995,"AvgRating":3.02},{"Name":"Waiting to Exhale (1995)","ReleaseDate":1995,"AvgRating":2.73}, ...]
```

Other formats such as CSV can be retrieved as well:

```
http://localhost:8000/data?format=csv&fields=Name,ReleaseDate,AvgRating
```

Details about possible formats are included in the [django-rest-pandas](https://github.com/wq/django-rest-pandas) documentation.


