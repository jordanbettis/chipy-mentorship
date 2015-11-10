from django.core.management.base import BaseCommand, CommandError
import pandas
import math
from chipyapp.models import Module, Area, Complex, DataType, Penetration, ActiveUnit

YEAR=2015
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs=1, type=unicode)

    def handle(self, *args, **options):
        with open(options['filename'][0]) as fd:
           data = pandas.read_csv(fd, dtype) #unicode
           Complex.objects.all().delete()
           for row in data.iterrows():
              if not math.isnan(row[1]['Module']):
                   module_obj, _ = Module.objects.get_or_create(module_number=row[1]['Module'])   
              if row[1]['Area'] != 'nan':
                   area_obj, _ = Area.objects.get_or_create(area=row[1]['Area'])
              complex_obj =  Complex.objects.create(
                   complex_name = row[1]['Complex Name'],
                   complex_code = row[1]['Direct Complex Code'],
                   hmc = row[1]['House Misc Code'],
                   unit = row[1]['Units'],
                   module = module_obj,
                   area = area_obj)
