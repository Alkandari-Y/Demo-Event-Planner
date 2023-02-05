from django.shortcuts import render


def customhandler404(request, exception, template_name="404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response


def customhandler403(request, exception, template_name="403.html"):
    response = render(request, template_name)
    response.status_code = 403
    return response
