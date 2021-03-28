from mindsdb_sdk import SDK
# csv file
file = r'D:\archive\insurance.csv'

# Connect to MindsDB Server URL
mdb = SDK('http://127.0.0.1:47334')

# Create datasource
mdb.datasources['health_insurance'] = {'file': file}

# learn from databse
mdb.predictors.learn('insurance_model',
                     'health_insurance',
                     'charges')

# predict
result = mdb.predictors('insurance_model').predict({'age': 30, 'bmi': 22})
