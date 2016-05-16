# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import redirect

def login(request):
    next_url = request.GET.get('next')
    url = '%s?service=%s' % (settings.GATE_LOGIN_URL, settings.GATE_APPLICATION_NAME)
    if next_url:
        url = '%s&next=%s' % (url, next_url)
    if settings.DEBUG:
        port = request.get_host().split(':')[-1]
        url = '%s&port=%s' % (url, port)

    return redirect(url)

def logout(request):
    url = settings.GATE_LOGOUT_URL + "?service=%s" % (settings.GATE_APPLICATION_NAME)
    if settings.DEBUG:
        port = request.get_host().split(':')[-1]
        url = '%s&port=%s' % (url, port)

    return redirect(url)
