from django.shortcuts import render, redirect, reverse
from.models import Estudo, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomepage

    def get(self, resquest, *args, **kwargs):
        if resquest.user.is_authenticated:
            return redirect('estudo:homeprincipal')
        else:
            return super().get(resquest, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('estudo:login')
        else:
            return reverse('estudo:criarconta')


class Homeestudos(LoginRequiredMixin, ListView):
    template_name = "homeestudos.html"
    model = Estudo
    # oject _list


class Detalhesestudo(LoginRequiredMixin, DetailView):
    template_name = "detalhesestudo.html"
    model = Estudo

    def get(self, resquest, *args, **kwargs):
        estudo = self.get_object()
        estudo.visualizacoes += 1
        estudo.save()
        usuario = resquest.user
        usuario.estudos_vistos.add(estudo)
        return super().get(resquest, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Detalhesestudo, self).get_context_data(**kwargs)
        estudos_relacionados = Estudo.objects.filter(categoria=self.get_object().categoria)[0:]
        context["estudos_relacionados"] = estudos_relacionados
        return context


class Pesquisaestudo(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Estudo

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = Estudo.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None


class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('estudo:homeestudos')


class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('estudo:login')


class Homeprincipal(LoginRequiredMixin, ListView):
    template_name = "homeprincipal.html"
    model = Estudo
    # oject _list

class Sobre(LoginRequiredMixin, ListView):
    template_name = "sobre.html"
    model = Estudo
    # oject _list

class Midias(LoginRequiredMixin, ListView):
    template_name = "midias.html"
    model = Estudo
    # oject _list