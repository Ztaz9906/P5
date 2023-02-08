from django.contrib.auth.models import User, Group
from django.forms import ModelForm
from django import forms
from app.models import Planilla,MedioBasico,User,Local


class PlanillaForm(ModelForm):
    class Meta:
        model = Planilla
        fields = ['faltante','sobrante','estado']
        Widget = {
            'faltante' : forms.NumberInput(),
            'sobrante' : forms.NumberInput(),
            'estado' : forms.Select()
        }
    
class localForm(ModelForm):
    class Meta:
        model = Local
        fields = ['nombre','tipo']
        Widget = {
            'nombre' : forms.TextInput(),
            'tipo' : forms.Select()
        }

class MedioBasicoForm(ModelForm):
    class Meta:
        model = MedioBasico
        fields = ['mb','tipo','local','estado']
        Widget = {
            'mb' : forms.TextInput(),
            'tipo' : forms.TextInput(),
            'local' : forms.Select(),
            'estado' : forms.Select()
        }
        
class RegisterAdminForm(forms.ModelForm):
    
    password1 =forms.CharField(label='Contraseña', widget= forms.PasswordInput(
        attrs={
            'placeholder': 'Ingrese la contraseña...',
            'id': 'password1',
             'requiered': 'requiered',
        }
     ))
    password2 =forms.CharField(label='Confirmar Contraseña', widget= forms.PasswordInput(
        attrs={
            'placeholder': 'Ingrese la contraseña nuevamente...',
            'id': 'password1',
             'requiered': 'requiered',
        }
     ))
    class Meta:
        model = User
        fields = ['username','name','apellidos','ci','tfno','groups']
        widgets = {
            'username': forms.TextInput(),
            'name': forms.TextInput(),
            'apellidos': forms.TextInput(),
            'ci': forms.TextInput(),
            'tfno': forms.TextInput(),
            'groups' : forms.CheckboxSelectMultiple(),
        }
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2 :
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2
    
    def clean_email(self):
        username = self.cleaned_data.get('username')
        a = User.objects.filter(username=username)
        if a.exists():
            raise forms.ValidationError("El usuario ya existe")
        return username
    def clean_ci(self):
        ci = self.cleaned_data.get('ci')
        a = User.objects.filter(ci=ci)
        if a.exists():
            raise forms.ValidationError("El Carnet de identidad ya existe")
        return ci
    def clean_tfno(self):
        tfno = self.cleaned_data.get('tfno')
        a = User.objects.filter(tfno=tfno)
        if a.exists():
            raise forms.ValidationError("Este telefono ya esta siendo utilizado")
        return tfno
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        user.groups.clear()
        for g in self.cleaned_data['groups'] :
                user.groups.add(g)
        return user

class UpdateUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username','name','apellidos','ci','tfno','groups']
        widgets = {
            'username': forms.TextInput(),
            'name': forms.TextInput(),
            'apellidos': forms.TextInput(),
            'ci': forms.TextInput(),
            'tfno': forms.TextInput(),
            'groups' : forms.CheckboxSelectMultiple(),
        } 
        error_messages = {
            'username': {
                'required': "Este campo es requerido.",
                'unique': "El usuario ya existe"
            },
            'ci': {
                'required': "Este campo es requerido.",
                'unique': "El Carnet de identidad ya existe"
            },
            'tfno': {
                'required': "Este campo es requerido.",
                'unique': "Este telefono ya esta siendo utilizado"
            }   
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        user.groups.clear()
        for g in self.cleaned_data['groups'] :
                user.groups.add(g)
        return user