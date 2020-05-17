from django.http import HttpResponse


class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Function handles generic/unknown webhook events """
        return HttpResponse(
            content=f'Unhandled Webhook recieved: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ Function handles stripe payment_intenent.succeeded events """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """ Function handles stripe payment_intenent.payment_failed events """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200
        )
