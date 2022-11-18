import datetime

from basic import models


def questao1():
    queryset = models.Employee.objects.filter(name__icontains='Silva')


def questao2():
    queryset = models.Employee.objects.filter(salary__gt=5000)


def questao3():
    queryset = models.Customer.objects.filter(income__lt=2000)


def questao4():
    start_date = datetime.date(2010, 1, 1)
    end_date = datetime.date(2021, 12, 31)

    queryset = models.Employee.objects.filter(admission_date__year__range=(2010, 2021))


def questao42():
    queryset = models.Employee.objects.filter(admission_date__year__gte=2010, admission_date__year__lte=2021)
