from django.shortcuts import render

def inicio(request):
    return render (request, "Rangel/inicio.html")
def registro(request):
    return render(request, 'Rangel/formregistro.html')
