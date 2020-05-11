from django.shortcuts import HttpResponse


def display_products(request):
    return HttpResponse("New page")
