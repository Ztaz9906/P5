from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from app.views import *

urlpatterns = [path('', index),
               path('login/', LoginFormView.as_view(), name='login'),
               path('logout/', LogoutView.as_view(), name='logout'),
               path('principal/', PrincipalTemplateView.as_view(), name='principal'),

               # -------------------------------------------------------
               # ----------- Local Básico URLS ------------
               # -------------------------------------------------------

               path('local/',
                    localListView.as_view(),
                    name='local'),

               path('local/add/',
                    localCreateView.as_view(),
                    name='add_local'),

               path('local/edit/<int:pk>/',
                    localUpdateView.as_view(),
                    name='editar_local'),

               path('local/delete/<int:pk>/',
                    localDeleteView.as_view(),
                    name='eliminar_local'),
               
               # -------------------------------------------------------
               # ----------- Planillas URLS ------------
               # -------------------------------------------------------

               path('Planilla/',
                    PlanillaListView.as_view(),
                    name='planilla'),

               path('Planilla/edit/<int:pk>/',
                    PlanillaUpdateView.as_view(),
                    name='editar_planilla'),

               path('Planilla/detalles/<int:pk>/',
                    details,
                    name='detalles_planilla'),
               
               # -------------------------------------------------------
               # ----------- Medio Básico URLS ------------
               # -------------------------------------------------------

               path('MedioBasico/',
                    MedioBasicoListView.as_view(),
                    name='medio'),

               path('MedioBasico/add/',
                    MedioBasicoCreateView.as_view(),
                    name='add_medio'),

               path('MedioBasico/edit/<int:pk>/',
                    MedioBasicoUpdateView.as_view(),
                    name='editar_medio'),

               path('MedioBasico/delete/<int:pk>/',
                    MedioBasicoDeleteView.as_view(),
                    name='eliminar_medio'),
               
               # -------------------------------------------------------
               # ----------- Usuarios URLS ------------
               # -------------------------------------------------------

               path('Usuario/',
                    UsuarioListView.as_view(),
                    name='user'),

               path('Usuario/add/',
                    UsuarioCreateAdminView.as_view(),
                    name='add_user'),

               path('Usuario/edit/<int:pk>/',
                    UsuarioUpdateView.as_view(),
                    name='editar_user'),

               path('Usuario/delete/<int:pk>/',
                    UsuarioDeleteView.as_view(),
                    name='eliminar_user'),


               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
