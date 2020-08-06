from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html', {'head':'Welcome To Pass Generator'})

def generate(request):

    char = list("abcdefghijklmnopqrstuvwxyz")
    lan = int(request.GET.get('langth', 10))
    if request.GET.get('uppercase'):
        char.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get('number'):
        char.extend(list('1234567890'))
    if request.GET.get('symble'):
        char.extend(list('!@#$%^&*()_+|\/?><'))
    
    password = ''

    for x in range(lan):
        password += random.choice(char)

    return render(request, 'generate.html', {'head': 'Congratulation, You have just Created a Unique Password', 'password':password})