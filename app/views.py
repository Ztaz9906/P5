from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from app.forms import PlanillaForm,MedioBasicoForm,RegisterAdminForm,UpdateUserForm,localForm
from app.models import Planilla,MedioBasico,User,Local
from django.contrib.auth.decorators import login_required, permission_required
from app.decorador import Adminstrador, JefedeArea, Vicedecano,JefedeArea_Vicedecano
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to="login")
    else:
        return HttpResponseRedirect(redirect_to="principal")


class LoginFormView(SuccessMessageMixin,LoginView):
    authentication_form = AuthenticationForm
    template_name = "sign-in/login.html"
    success_url = reverse_lazy('principal')
    success_message = "Usuario logeado"

class PrincipalTemplateView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = "index.html"
    permission_required = 'app.view_user'

"""---------------------------------------------------------------
-----------------------------Local VIEW ------------------------
---------------------------------------------------------------"""
@method_decorator([JefedeArea],name='dispatch')
class localListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Local
    template_name = 'locales/index.html'
    permission_required = 'app.view_local'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de locales'
        return context
@method_decorator([JefedeArea],name='dispatch')
class localCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Local
    form_class = localForm
    template_name = 'locales/add.html'
    success_url = reverse_lazy('local')
    success_message = "Local creado"
    permission_required = 'app.add_local'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir local'
        return context
    def post(self, request, *args, **kwargs):
        local = Local(nombre=request.POST.get('nombre'),tipo = request.POST.get('tipo'))
        local.save()
        planilla = Planilla(local=local)
        planilla.save()
        return redirect('local')
@method_decorator([JefedeArea],name='dispatch')   
class localUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Local
    form_class = localForm
    template_name = 'locales/edit.html'
    success_url = reverse_lazy('local')
    success_message = "Local editado"
    permission_required = 'app.change_local'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar local'
        return context
@method_decorator([JefedeArea],name='dispatch')
class localDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Local
    template_name = 'locales/delete.html'
    success_url = reverse_lazy('local')
    success_message = "Local eliminado"
    permission_required = 'app.delete_local'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar local'
        return context


"""---------------------------------------------------------------
-----------------------------Medio Basico VIEW ------------------------
---------------------------------------------------------------"""
@method_decorator([JefedeArea],name='dispatch')
class MedioBasicoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = MedioBasico
    template_name = 'medios/index.html'
    permission_required = 'app.view_mediobasico'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de MedioBasicoes'
        return context
@method_decorator([JefedeArea],name='dispatch')
class MedioBasicoCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = MedioBasico
    form_class = MedioBasicoForm
    template_name = 'medios/add.html'
    success_url = reverse_lazy('medio')
    success_message = "Medio Básico creado"
    permission_required = 'app.add_mediobasico'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir MedioBasico'
        return context
@method_decorator([JefedeArea],name='dispatch')          
class MedioBasicoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = MedioBasico
    form_class = MedioBasicoForm
    template_name = 'medios/edit.html'
    success_url = reverse_lazy('medio')
    success_message = "Medio Básico editado"
    permission_required = 'app.change_mediobasico'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar MedioBasico'
        return context
@method_decorator([JefedeArea],name='dispatch')
class MedioBasicoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = MedioBasico
    template_name = 'medios/delete.html'
    success_url = reverse_lazy('medio')
    success_message = "Medio Básico eliminado"
    permission_required = 'app.delete_mediobasico'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar MedioBasico'
        return context

"""---------------------------------------------------------------
-----------------------------Planilla VIEW ------------------------
---------------------------------------------------------------"""
@method_decorator([Vicedecano],name='dispatch')
class PlanillaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Planilla
    template_name = 'planilla/index.html'
    permission_required = 'app.view_planilla'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Planillaes'
        return context
@method_decorator([Vicedecano],name='dispatch')              
class PlanillaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Planilla
    form_class = PlanillaForm
    template_name = 'planilla/edit.html'
    success_url = reverse_lazy('planilla')
    success_message = "Planilla editada"
    permission_required = 'app.change_planilla'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Planilla'
        return context
@login_required 
@permission_required('app.view_mediobasico', raise_exception=True)
@Vicedecano
def details(request,pk):
    local = Local.objects.get(pk=pk )
    context = {}
    context['title'] = local.nombre
    context['object_list'] = MedioBasico.objects.filter(local=local)
    return render(request, 'planilla/index_detail.html', context)       

"""---------------------------------------------------------------
-----------------------------Usuarios VIEW ------------------------
---------------------------------------------------------------"""
@method_decorator([Adminstrador],name='dispatch')
class UsuarioListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = User
    template_name = 'usuarios/index.html'
    permission_required = 'app.view_user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Usuarioes'
        return context
@method_decorator([Adminstrador],name='dispatch')
class UsuarioCreateAdminView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = RegisterAdminForm
    template_name = 'usuarios/add.html'
    success_url = reverse_lazy('user')
    success_message = "Usuario Registrado"
    permission_required = 'app.add_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir Dependiente'
        return context
@method_decorator([Adminstrador],name='dispatch')
class UsuarioUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model =User
    form_class = UpdateUserForm
    template_name = 'usuarios/edit.html'
    success_url = reverse_lazy('user')
    success_message = "Usuario Editado"
    permission_required = 'app.change_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Usuario'
        return context
@method_decorator([Adminstrador],name='dispatch') 
class UsuarioDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'usuarios/delete.html'
    success_url = reverse_lazy('user')
    success_message = "Usuario Eliminado"
    permission_required = 'app.delete_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Usuario'
        return context