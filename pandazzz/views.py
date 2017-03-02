# views.py
from rest_pandas import PandasSimpleView
import pandas as pd

class ItemView(PandasSimpleView):
    def get_data(self, request, *args, **kwargs):
       
        # Replace this with a smarter way to load a data file
        df = pd.read_table('data/movies.csv', sep=';')

        # return columns requested in "fields" query parameter
        return df.filter( items=request.query_params['attributes'].split(","))

class AttributeView(PandasSimpleView):
    def get_data(self, request, *args, **kwargs):
       
        # Replace this with a smarter way to load a data file
        df = pd.read_table('data/movies.csv', sep=';')

        attributes = []
        index = 0

        for datatype in df.dtypes:
          attributes.append( { 'name': str( df.columns.values[index] ), 'type': str( datatype ) } )
          index += 1
          print( datatype )

        return attributes