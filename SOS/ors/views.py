from django.http import HttpResponse


def test_ors(request):
    return HttpResponse("<h1>Testing ORS<h1/>")


