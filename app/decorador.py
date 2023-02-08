from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group

def Adminstrador(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    group = Group.objects.filter(name="Administrador").first()
    actual_decorator = user_passes_test(
        lambda u: u.is_active and (group in u.groups.all()) or u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
def JefedeArea(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    group = Group.objects.filter(name="Jefe de Area").first()
    actual_decorator = user_passes_test(
        lambda u: u.is_active and (group in u.groups.all()) or u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
def Vicedecano(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    group = Group.objects.filter(name="Vicedecano").first()
    actual_decorator = user_passes_test(
        lambda u: u.is_active and (group in u.groups.all()) or u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
def JefedeArea_Vicedecano(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    group = Group.objects.filter(name="Vicedecano").first()
    group1 = Group.objects.filter(name="Jefe de Area").first()
    actual_decorator = user_passes_test(
        lambda u: u.is_active and (group in u.groups.all()) or (
            group1 in u.groups.all()) or u.is_superuser ,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator