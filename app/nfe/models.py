from django.db import models
from app.accounts.models import Empresa

class NotaFiscal(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    arquivo_xml = models.FileField(upload_to='nfe/xml/')
    arquivo_pdf = models.FileField(upload_to='nfe/pdf/', blank=True, null=True)
    data_envio = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='PENDENTE')
    cfop = models.CharField(max_length=10, blank=True)
    ncm = models.CharField(max_length=10, blank=True)
    cst = models.CharField(max_length=10, blank=True)
    icms = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    classificacao = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"NF-e {self.pk} - {self.empresa}"
