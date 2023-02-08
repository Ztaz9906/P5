from django.db import models
from django.utils.translation import gettext_lazy as T
from django.core.validators import RegexValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as T

validate_username = RegexValidator('^[A-Za-z\d]*$', 'Solo Letras y numeros , sin espacios')

validate_mb = RegexValidator('^(MB|MB-)\d{8,}$', 'Identificador Inválido')
tfno_regex = RegexValidator('^\+53\d{8}$', 'Teléfono invalido')
validate_ci = RegexValidator('^\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])\d{5}$', 'Carnet invalido')
validate_name = RegexValidator('^[A-Za-záãäéëêíîóöúüñç\s]*$', 'Solo Letras')

# Create your models here.

# Create your models here.
class OwnUserManager(BaseUserManager):
    """Manager para usuarios"""
    use_in_migrations = True

    def create_user(self, username, name, apellidos,  ci, tfno, password=None, **extra_kwargs):
        """Crea un nuevo Usuario"""
        if not username:
            raise ValueError("El nombre de usuario no puede estar vacio")

        user = self.model(username=username, name=name,
                          apellidos=apellidos, ci=ci, tfno=tfno, **extra_kwargs)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, name, apellidos,  ci, tfno, password=None, **extra_kwargs):
        user = self.create_user(username, name, apellidos, ci, tfno,
                                password, **extra_kwargs)

        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, validators=[validate_username])
    name = models.CharField(max_length=255 , validators=[validate_name])
    apellidos = models.CharField(max_length=255 , validators=[validate_name])
    ci = models.CharField(max_length=11, unique=True, null=False, blank=False, validators=[validate_ci])
    tfno = models.CharField(max_length=50 , validators=[tfno_regex])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = OwnUserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'apellidos', 'ci', 'tfno']

    def get_full_name(self):
        return "%s %s" % (self.name, self.apellidos)

    def get_short_name(self):
        return self.name

    def __str__(self):
        return (self.name)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def if_staff(self):
        return self.is_staff

class estado (models.TextChoices):
        bueno= 'B', T('Bueno')
        regular= 'R', T('Regular')
        malo = 'M', T('Malo')
        
class tipo (models.TextChoices):
        aula= 'A', T('Aula')
        salon= 'S', T('Salon')
        laboratorio = 'L', T('Laboratorio')
        departamento = 'D', T('Departamento')
        

class Local(models.Model):
    
    nombre = models.CharField(max_length=255)
    
    tipo = models.CharField(max_length=255,choices=tipo.choices)
    
    def __str__(self):
        return self.nombre

class MedioBasico(models.Model):
    
    mb = models.CharField(max_length=255, validators=[validate_mb])
    
    tipo = models.CharField(max_length=15, verbose_name='tipo',null=False, blank=False)
    
    local = models.ForeignKey(Local, on_delete = models.CASCADE)

    estado = models.CharField(max_length=255, verbose_name='estado',
                                     choices=estado.choices, null=False, blank=False)

    def __str__(self):
        return self.tipo

class estadomedioBasico (models.TextChoices):
        pendiente= 'P', T('Pendiente')
        aprobado= 'A', T('Aprobado')
        denegado = 'D', T('Denegado')

class Planilla(models.Model):
        
        local = models.OneToOneField(Local, on_delete=models.CASCADE,primary_key=True)
        
        fecha =  models.DateField(blank=False, null=False, auto_now=True)
    
        faltante = models.IntegerField(default=0,blank=True, null=True,validators=[MinValueValidator(0 , "La cantidad debe ser mayor o igual a 0")])
    
        sobrante = models.IntegerField(default=0,blank=True, null=True,validators=[MinValueValidator(0 , "La cantidad debe ser mayor o igual a 0")])
    
        estado = models.CharField(max_length=255,choices=estadomedioBasico.choices, null=False, blank=False,default='P')


        def __str__(self):
                return self.estado

        