from django.shortcuts import redirect, render
from requests import get
from django.urls import reverse

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(reverse('admin:index')):
            if request.user.is_authenticated:
                last_ip = request.session.get('last_ip')
                current_ip = request.META.get('REMOTE_ADDR')
                if last_ip and last_ip != current_ip:
                    messages.warning(request, "Your IP address has changed since your last login!")
                    del request.session['last_ip']
                    return redirect('admin')

                request.session['last_ip'] = current_ip
        return self.get_response(request)
