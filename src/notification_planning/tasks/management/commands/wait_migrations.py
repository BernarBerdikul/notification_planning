import time

from django.core.management.base import BaseCommand
from django.db import DEFAULT_DB_ALIAS, connections
from django.db.migrations.executor import MigrationExecutor


def is_database_synchronized(database):
    connection = connections[database]
    connection.prepare_database()
    executor = MigrationExecutor(connection)
    targets = executor.loader.graph.leaf_nodes()
    return not executor.migration_plan(targets)


class Command(BaseCommand):
    help = 'Проверяет все ли миграции совершены'

    def handle(self, *args, **options):
        migrations_pending = True
        while migrations_pending:
            if is_database_synchronized(DEFAULT_DB_ALIAS):
                self.stdout.write(self.style.SUCCESS('Миграции завершены'))
                migrations_pending = False
            else:
                self.stdout.write(
                    self.style.WARNING(
                        'Миграции еще не завершены. Ожидаем 2 секунды',
                    ),
                )
                time.sleep(2)
