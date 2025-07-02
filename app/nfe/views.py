from django.shortcuts import render

def classificar_nota(dados):
    if dados['cst'] in ('060', '070'):
        return 'RISCO'
    if dados['icms'] and float(dados['icms']) > 1000:
        return 'ALERTA'
    return 'REGULAR'

