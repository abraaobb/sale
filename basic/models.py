from django.db import models


# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    gender = models.CharField(max_length=1, null=False, default='M')

    class Meta:
        db_table = 'employee'
        managed = True
