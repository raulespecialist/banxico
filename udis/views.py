import json
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

#Bmx-Token: e3980208bf01ec653aba9aee3c2d6f70f6ae8b066d2545e379b9e0ef92e9de25
token = '737fa8c8e182d900196f543575c3b031f4005fdb53c82461cf7d56a1cfa99879'
#https://www.banxico.org.mx/SieAPIRest/service/v1/token

def home(request):
    return render(request, 'udis/index.html')


def dashboard(request):
    #messages = Message.objects.all()
    #print (messages)
    #for message in messages:
        #print(message)
    
    return render(request, 'udis/dashboard.html')


#@require_POST
def udis(request):
    #response = requests.get('https://www.banxico.org.mx/SieInternet/consultaSerieGrafica.do?s=SP68257,CP150,1&l=es')
    response = requests.get('https://www.banxico.org.mx/SieAPIRest/service/v1/series/P68257,CP150/datos/oportuno?token=737fa8c8e182d900196f543575c3b031f4005fdb53c82461cf7d56a1cfa99879')
    # transfor the response to json objects
    todos = response.json()
    print (todos)
    return render(request, 'udis/dashboard2.html', {"todos": todos})
    #return HttpResponse('Welcom, This is my life')

 

#@csrf_exempt
#@require_POST
def usd(request):
    return HttpResponse('hi type parameters')