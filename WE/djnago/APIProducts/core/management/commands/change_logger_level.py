from django.core.cache import cache
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Change the logger level'

    def add_arguments(self, parser):
        parser.add_argument('log_level', type=str, help='Desired log level')

    def handle(self, *args, **options):
        log_level = options['log_level'].upper()

        valid_log_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if log_level not in valid_log_levels:
            self.stdout.write(self.style.ERROR("Invalid log level. Please use one of: DEBUG, INFO, WARNING, ERROR, CRITICAL"))
            return

        cache.set('loglevel', log_level)
        self.stdout.write(self.style.SUCCESS(f"Log level set to '{log_level}'"))

