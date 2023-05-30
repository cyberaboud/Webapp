"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including sanother URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from myapp.views import *
from login.views import *
from django.urls import path, include
from users.views import *

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from users.views import *
from django.contrib import admin

from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView

from users.forms import LoginForm

urlpatterns = [
    path('departements/', departement_list, name='departement_list'),
    path('employes/', employe_list, name='employe_list'),
    path('agendas/', agenda_list, name='agenda_list'),
    #path('', home, name='home'),
    path('departements/add/', add_departement, name='add_departement'),
    path('departements/delete/<int:id>', departement_delete, name='departement_delete'),
    path('departements/update/<int:id>', departement_update, name='departement_update'),


    path('employes/add/', add_employe, name='add_employe'),
    path('employes/delete/<int:id>', employe_delete, name='employe_delete'),
    path('employes/update/<int:id>', employe_update, name='employe_update'),


    path('activitess/add/', add_activites, name='add_activites'),
    path('activitess/delete/<int:id>', activites_delete, name='activites_delete'),
    path('activitess/update/<int:id>', activites_update, name='activites_update'),



    path('script/', execute_query, name='script_page'),



    path('procesverbals/', procesverbal_list, name='procesverbal_list'),
    path('activitesdepts/', activitesdept_list, name='activitesdept_list'),
    path('actdeptverbals/', actdeptverbal_list, name='actdeptverbal_list'),
    path('absents/', absent_list, name='absent_list'),
    path('activites/', activites_list, name='activites_list'),
    path('alertes/', alertes_list, name='alertes_list'),
    
    path('agendas/add/', add_agenda, name='add_agenda'),
    path('admin/', admin.site.urls),

    path('', include('users.urls')),

    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=LoginForm), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),


    path('accounts/profile/', profile, name='profile'),

    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
