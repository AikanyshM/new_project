from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    first_invent_numbers = models.IntegerField()
    balance_group = models.IntegerField()

    def __str__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    inventory_number = models.IntegerField()
    initial_cost = models.IntegerField()
    residual_value = models.IntegerField()

    def __str__(self):
        return self.name



# Create your models here.
