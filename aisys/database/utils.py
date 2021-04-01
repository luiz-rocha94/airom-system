import pandas as pd
from mindsdb_sdk import SDK
from itertools import islice


def table_import(table, csv_file, *args, **kwargs):
    """
    Import .csv file, uses pandas read_csv args and kwargs.
    """
    data = pd.read_csv(csv_file, *args, **kwargs)
    batch_size = 100
    objs = (table(**row) for index, row in data.iterrows())
    while True:
        batch = list(islice(objs, batch_size))
        if not batch:
            break
        table.objects.bulk_create(batch, batch_size)


def table_export(table, csv_file, **kwargs):
    """
    Export table data, uses django objects filter kwargs.
    """
    values = table.table.objects.filter(**kwargs).values()
    data = pd.DataFrame(values)
    return data.to_csv(csv_file)
