from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    verbose_name = 'Λογαριασμοί Χρηστών'

    def ready(self):
        import accounts.signals