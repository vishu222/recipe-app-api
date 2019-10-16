import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """command to wait the execution util db is available"""
    def handle(self, *args, **options):
        self.stdout.write('waiting for db...')
        conn = None
        while not conn:
            try:
                conn = connections['default']
            except OperationalError:
                self.stdout.write('database unavailable waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('database available!'))
