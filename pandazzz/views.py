# views.py
from rest_pandas import PandasSimpleView
import pandas as pd

class TimeSeriesView(PandasSimpleView):
    def get_data(self, request, *args, **kwargs):
       
        # Replace this with a smarter way to load a data file
        df = pd.read_table('data/movies.csv', sep=';')

        # return columns requested in "fields" query parameter
        return df.filter( items=request.query_params['fields'].split(","))