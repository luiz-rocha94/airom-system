from django.db import models
import pandas as pd
from itertools import islice


class UsedCar(models.Model):
    model = models.CharField(max_length=100, null=True)
    year = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    transmission = models.CharField(max_length=100, null=True)
    mileage = models.IntegerField(null=True)
    fueltype = models.CharField(max_length=100, null=True)
    tax = models.IntegerField(null=True)
    mpg = models.FloatField(null=True)
    enginesize = models.FloatField(null=True)


class Table:
    def __init__(self, table):
        self.table = table

    def from_data(self, csv_file, *args, **kwargs):
        """
        Import .csv file, uses pandas read_csv args and kwargs.
        """
        data = pd.read_csv(csv_file, *args, **kwargs)
        batch_size = 100
        objs = (self.table(**row) for index, row in data.iterrows())
        while True:
            batch = list(islice(objs, batch_size))
            if not batch:
                break
            self.table.objects.bulk_create(batch, batch_size)

    def to_data(self, **kwargs):
        """
        Export table data, uses django objects filter kwargs.
        """
        values = self.table.objects.filter(**kwargs).values()
        data = pd.DataFrame(values)
        return data
