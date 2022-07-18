from .models import Estudo

def lista_estudos_recentes(request):
    lista_estudos = Estudo.objects.all().order_by('-data_criacao')[0:8]
    if lista_estudos:
        estudo_destaque = lista_estudos[0]
    else:
        estudo_destaque = None
    return {"lista_estudos_recentes": lista_estudos, "estudo_destaque": estudo_destaque}


def lista_estudos_em_alta(request):
    lista_estudos = Estudo.objects.all().order_by('-visualizacoes')[0:8]
    return {"lista_estudos_em_alta": lista_estudos}


