from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')
def password(request):
    characters=list('asdfghjklqwertyuiopzxcvbnm')
    thePass=''
    length=int(request.GET.get('length',12))
    if request.GET.get('UpperCase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLMNBVCXZ'))
    if request.GET.get('Numbers'):
        characters.extend(list('01234567889'))
    if request.GET.get('Special'):
        characters.extend(list('~!@#$%^&*()-=+_\|''"?><,."'))
    for x in range(length):
        thePass+=random.choice(characters)
    return render(request,'generator/password.html',{'password':thePass})
def about(request):
    return render(request,'generator/about.html')
