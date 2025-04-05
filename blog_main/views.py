from django.shortcuts import render

def home(request):
    # return HttpResponse("enducation for nation")
    return render(request,"home.html")