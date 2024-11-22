from django.shortcuts import render
from userauths.forms import UserRegisterForm

def register_view(request):
    if request.method == "POST":
        print("Usuario registrado exitosamente")
    else:
        print("No se ha podido registrar el usuario")

    form = UserRegisterForm()

    context = {
        'form' : form,
    }
    return render(request, "userauths/sign-up.html", context)