from django.contrib.auth.models import Group, Permission

class CustomGroup(Group):
    pass

class CustomPermission(Permission):
    pass
