from mindsdb_sdk import SDK


# Connect to MindsDB Server URL
mdb = SDK('http://127.0.0.1:47334')

# Create datasource, fail
#source = {'query': 'select * from database_heartfailure'}
#mdb.datasources['heart_failure'] = source

# learn from database
mdb.predictors.learn('heart_failure_model',
                     'heart_failure',
                     'death_event')

# predict
result = mdb.predictors('heart_failure_model').predict({'age': 30, 'time': 5})
