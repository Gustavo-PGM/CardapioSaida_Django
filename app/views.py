from django.shortcuts import render
from .models import Segunda, Terca, Quarta, Quinta, Sexta, Primeiro, Segundo, Terceiro, Quarto, Quinto, Sexto, Setimo, Oitavo, Nono, Decimo, DecimoPrimeiro, DecimoSegundo

def home(request):
    return render(request, 'paginas/home.html')

def cardapio(request):
    dias = {
        'segunda': Segunda.objects.all(),
        'terca': Terca.objects.all(),
        'quarta': Quarta.objects.all(),
        'quinta': Quinta.objects.all(),
        'sexta': Sexta.objects.all(),

    }
    return render(request, 'paginas/cardapio.html', dias)


def ordemsaida(request):
    ordem = {
        'primeiro': Primeiro.objects.all(),
        'segundo': Segundo.objects.all(),
        'terceiro': Terceiro.objects.all(),
        'quarto': Quarto.objects.all(),
        'quinto': Quinto.objects.all(),
        'sexto': Sexto.objects.all(),
        'setimo': Setimo.objects.all(),
        'oitavo': Oitavo.objects.all(),
        'nono': Nono.objects.all(),
        'decimo': Decimo.objects.all(),
        'decimo_primeiro': DecimoPrimeiro.objects.all(),
        'decimo_segundo': DecimoSegundo.objects.all(),
    }

    return render(request, 'paginas/ordemsaida.html', ordem)