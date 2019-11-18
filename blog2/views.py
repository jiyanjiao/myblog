from django.shortcuts import render

# Create your views here.


def index(request):
    # return HttpResponse("success")
    return render(request, "blog2/index.html", {'hello': 'blog2'})
