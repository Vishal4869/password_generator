
from django.shortcuts import render
import random


def index(request):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols ='''"#$%&'()*+,-./:;<=>?@[\]^_`{|}~!"'''

    upp = request.POST.get('switch1', 'off')
    low = request.POST.get('switch2', 'off')
    num = request.POST.get('switch3', 'off')
    sym = request.POST.get('switch4', 'off')
    value = request.POST.get('text')
    if value == '':
        value =0

    length = int(0 if value is None else value)

    if upp == 'off' and low == 'off'and num == 'off' and sym == 'off' and length != 0 :
        return render(request, 'index.html')

    if upp == 'on':
        a1 = upper
    else:
        a1 = ''

    if low == 'on':
        a2 = lower
    else:
        a2 = ''

    if num == 'on':
        a3 = numbers
    else:
        a3 = ''

    if sym == 'on':
        a4 = symbols
    else:
        a4 = ''

    all = a1 + a2 + a3 + a4

    password = "".join(random.choices(all, k=length))
    param = {'pwd':password}

    return render(request, 'index.html', param)










