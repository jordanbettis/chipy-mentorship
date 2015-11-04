from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs=1, type=unicode)

    def handle(self, *args, **options):
        print 'trying to open {}'.format(options['filename'])
        with open(options['filename'][0]) as fd:
            print "opened file"
