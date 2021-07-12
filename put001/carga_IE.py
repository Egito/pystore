import os
import django

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'map.settings')
django.setup()

from openpyxl import load_workbook
from entregas.models import Iniciativa_Estrategica

path = os.getcwd()
if 'cargas' in path:
    filepath = ''
else:
    filepath = 'cargas/'

wb = load_workbook(filename=filepath+"dados/map-e.xlsx")

InicEst = wb['InicEst']
Iniciativa_Estrategica.objects.all().delete()
for i, row in enumerate(InicEst):
    if i>0:
        Iniciativa_Estrategica.objects.update_or_create(titulo=row[0].value, descricao=row[2].value)
