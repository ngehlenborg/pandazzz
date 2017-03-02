# views.py
from rest_pandas import PandasSimpleView
import pandas as pd

class TimeSeriesView(PandasSimpleView):
    def get_data(self, request, *args, **kwargs):
        print(str(request.query_params))
        df = pd.read_csv('/Users/nils/Projects/pandazzz/pandazzz/pandazzz/data_38.csv')

        print(request.query_params['fields'])

        return df.filter( items=request.query_params['fields'].split(","))
