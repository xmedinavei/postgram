"""User app configuration."""

from django.apps import AppConfig


#app must be installed on settings.py on INSTALED_APPS using 'name'='users'
class UsersConfig(AppConfig):
    """User app config."""
    name = 'users'
    verbose_name = 'Users'
