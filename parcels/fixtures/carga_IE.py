import os
import django

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from openpyxl import load_workbook
from parcels.models import Parcel

path = os.getcwd()
if 'cargas' in path:
    filepath = ''
else:
    filepath = 'cargas/'

wb = load_workbook(filename=filepath+"map-e.xlsx")

InicEst = wb['Entregas_N_Parcela']
Parcel.objects.all().delete()
for i, row in enumerate(InicEst):
    if i>0:
        Parcel.objects.update_or_create(
            value=row[2].value, 
            datep=row[3].value,
            parcel=row[4].value,
            status=row[5].value,
            comment=row[6].value
            )
