from django.http import HttpResponse
from django.shortcuts import render, redirect
from django_otp.decorators import otp_required


def home(request):
    return HttpResponse("Você saiu com sucesso. Volte logo!")


@otp_required
def painel_seguro(request):
    return HttpResponse("Você está autenticado via MFA.")


@otp_required
def dashboard(request):
    if not request.user.is_verified():
        return redirect("two_factor:setup")
    return HttpResponse("Dashboard com MFA verificado.")


from two_factor.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'two_factor/core/login.html'
    template_name_token = 'two_factor/core/token.html'
