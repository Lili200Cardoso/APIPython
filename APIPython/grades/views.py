from django.http import HttpResponse 

def grades(request):
    if request.method == "GET":
        return HttpResponse("Maravilhosa Lili!")
