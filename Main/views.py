from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import EditUserForm, AvatarForm
from .models import Avatar


def index(request):
    return render(request, "Main/index.html")


def perfil(request):
    return render(request, "Main/perfil.html")


@login_required
def editar_perfil(request):
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=request.user)
        try:
            avatar = request.user.avatar
        except Avatar.DoesNotExist:
            avatar = None
        if avatar:
            avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        else:
            avatar_form = AvatarForm(request.POST, request.FILES)

        if form.is_valid() and avatar_form.is_valid():
            form.save()
            avatar_instance = avatar_form.save(commit=False)
            avatar_instance.user = request.user
            avatar_instance.save()
            return redirect("Main:perfil")
    else:
        form = EditUserForm(instance=request.user)
        if hasattr(request.user, "avatar"):
            avatar_form = AvatarForm(instance=request.user.avatar)
        else:
            avatar_form = AvatarForm()
    return render(
        request, "Main/editar_perfil.html", {"form": form, "avatar_form": avatar_form}
    )
