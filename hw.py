from django.http import HttpResponse


def index(request):
    f = open("./HomePage.html", "r")
    html = f.read()
    print html
    return HttpResponse(html)


def indexhw(request):
    return HttpResponse("Hello World Demo!")
