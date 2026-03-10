from django.shortcuts import render
from .models import Familiar


def lista_familiares(request):
    todos_los_familiares = Familiar.objects.all()

    contexto = {"familiares": todos_los_familiares}
    return render(request, "familiares/lista.html", contexto)
