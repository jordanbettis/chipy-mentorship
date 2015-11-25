from django.core.management.base import BaseCommand, CommandError
import pandas
import math
from chipyapp.models import Module, Area, ServiceStatus, PropertyType, Team, Complex, LOB, Penetration, ActiveUnit

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs=1, type=unicode)
        parser.add_argument('--year', dest='year', type=int)
        parser.add_argument('--quarter', dest='quarter', type=int)

    def handle(self, *args, **options):
        with open(options['filename'][0]) as fd:
           year = options['year']
           quarter = options['quarter']
           data = pandas.read_csv(fd, dtype={"Direct Complex Code": unicode})
           for row in data.iterrows():
              if not math.isnan(row[1]['Module']):
                  module_obj, _ = Module.objects.get_or_create(module_number=row[1]['Module'])
              if row[1]['Area'] != 'nan':
                  area_obj, _ = Area.objects.get_or_create(area=row[1]['Area'])
              if row[1]['Type'] != 'nan':
                  service_status_obj, _ = ServiceStatus.objects.get_or_create(service_status=row[1]['Type'])
              if row[1]['Team'] != 'nan':
                  team_obj, _ = Team.objects.get_or_create(team=row[1]['Team'])
              if row[1]['Property Type'] != 'nan':
                  property_type_obj, _ = PropertyType.objects.get_or_create(property_type=row[1]['Property Type'])

              complex_obj, _  =  Complex.objects.get_or_create(
                  #complex_name = row[1]['Complex Name'],
                  complex_code = row[1]['Direct Complex Code'],
                  #hmc = row[1]['House Misc Code'],
                  unit = row[1]['Units'],
                  module = module_obj,
                  area = area_obj,
                  service_status = service_status_obj,
                  team = team_obj,
                  property_type = property_type_obj)

              for lob_name in ["Video", "HSD", "CDV", "XHS"]:
                  dt_obj, _ = LOB.objects.get_or_create(lob=lob_name)
                  lob_pen = "{} Pen".format(lob_name)
                  lob_active = "{} Active".format(lob_name)
                  Penetration.objects.create(
	              year = year,
                      quarter = quarter,
                      penetration = row[1][lob_pen],
                      complex_code = complex_obj,
                      lob = dt_obj
                  )
                  ActiveUnit.objects.create(
                      year = year,
                      quarter = quarter,
                      active_unit = row[1][lob_active],
                      complex_code = complex_obj,
                      lob = dt_obj)

