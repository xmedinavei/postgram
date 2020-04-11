"""Post application module."""

##################################################################
#The app is installed on setting.py on INSTALLED_APS[] as 'posts'#
##################################################################

from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Post application settings."""

    name = 'posts'
    varbose_name = 'Posts'
