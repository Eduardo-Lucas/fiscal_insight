from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile

def gerar_pdf(nota):
    html = render_to_string("nfe/relatorio.html", {"nota": nota})
    with tempfile.NamedTemporaryFile(delete=True, suffix=".pdf") as output:
        HTML(string=html).write_pdf(output.name)
        output.seek(0)
        return output.read()
