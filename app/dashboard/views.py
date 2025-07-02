from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app.nfe.models import NotaFiscal

# @login_required
def home(request):
    if not request.user.is_authenticated:
        return render(request, "dashboard/home.html", {"notas": []})
    notas = NotaFiscal.objects.filter(empresa=request.user.empresa).order_by('-data_envio')
    return render(request, "dashboard/home.html", {"notas": notas})
