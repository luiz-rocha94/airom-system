from mindsdb_sdk import SDK


# Connect to MindsDB Server URL
mdb = SDK('http://127.0.0.1:47334')

# Create datasource
file = r'D:\archive\heart_failure_clinical_records_dataset.csv'
mdb.datasources['heart_failure'] = {'file': file}

# learn from database
mdb.predictors.learn('heart_failure_model',
                     'heart_failure',
                     'death_event')

# predict
result = mdb.predictors('heart_failure_model').predict({'age': 30, 'time': 5})
