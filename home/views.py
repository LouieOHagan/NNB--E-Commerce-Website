from django.shortcuts import render


def index(request):
    """ index view renders the home/route page """

    return render(request, 'home/index.html')
