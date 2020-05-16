from django.shortcuts import HttpResponse


def checkout(request):
    """ view_cart view renders the cart page.
    It displays the items in the users cart
    """

    return HttpResponse("This is our new page")
