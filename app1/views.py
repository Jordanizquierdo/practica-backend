from django.shortcuts import render

# Create your views here.


def incio(request):
    data = {"nombre":"jordan","edad":"76","mascota":"gato"}
    return render(request,'app1/index.html',data)