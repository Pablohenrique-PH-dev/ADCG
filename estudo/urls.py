# criação da pagina precisa ter 'url' - 'view' e 'template'

from django.urls import path, reverse_lazy
from.views import Homeestudos, Homepage, Detalhesestudo, Pesquisaestudo, Paginaperfil, Criarconta, Homeprincipal, Sobre, Midias
from django.contrib.auth import views as auth_view

app_name = 'estudo'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('estudos/', Homeestudos.as_view(), name='homeestudos'),
    path('estudos/<int:pk>', Detalhesestudo.as_view(), name='detalhesestudo'),
    path('pesquisa/', Pesquisaestudo.as_view(), name='pesquisaestudo'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html',
                                                             success_url=reverse_lazy('estudo:homeestudos')), name='mudarsenha'),
    path('homeprincipal/', Homeprincipal.as_view(), name='homeprincipal'),
    path('sobre/', Sobre.as_view(), name='sobre'),
    path('midias/', Midias.as_view(), name='midias'),
]

"""

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('estudos/', Homeestudos.as_view(), name='homeestudos'),
    path('estudos/<int:pk>', Detalhesestudo.as_view(), name='detalhesestudo'),
    path('pesquisa/', Pesquisaestudo.as_view(), name='pesquisaestudo'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html',
                                                             success_url=reverse_lazy('estudo:homeestudos')), name='mudarsenha'),
    path('testepagina/', Testepagina.as_view(), name='testepagina'),
]
"""