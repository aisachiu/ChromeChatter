from django import http
from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    return http.HttpResponse('Hello World!')

def andrew(request):
    return http.HttpResponse('Andrew')

def blankForm(request):
        # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'chatMessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('chat.html', context_dict, context)
