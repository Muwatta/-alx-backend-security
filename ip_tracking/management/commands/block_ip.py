from django.core.management.base import BaseCommand
from ip_tracking.models import BlockedIP

class Command(BaseCommand):
    help = 'Block an IP address'

    def add_arguments(self, parser):
        parser.add_argument('ip', type=str)

    def handle(self, *args, **kwargs):
        BlockedIP.objects.create(ip_address=kwargs['ip'])
        self.stdout.write(self.style.SUCCESS('IP blocked successfully'))
