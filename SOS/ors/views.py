from django.http import HttpResponse


def test_ors(request):
    return HttpResponse("<h1>Django Testing ors<h1/>")