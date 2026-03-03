from django.shortcuts import render


# Create your views here.
def index(request):
    context = {"mensaje": "Bienvenidos a mi aplicación hecha en Django"}
    return render(request, "myapp/index.html", context)
