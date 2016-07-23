# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import redirect

from mano_id import settings as mano_settings


def login(request):
    next_url = request.GET.get('next')
    url = '%s?service=%s' % (mano_settings.MANO_LOGIN_URL,
                             settings.MANO_APPLICATION_NAME)
    if next_url:
        url = '%s&next=%s' % (url, next_url)
    if settings.DEBUG:
        port = request.get_host().split(':')[-1]
        url = '%s&port=%s' % (url, port)

    return redirect(url)


def logout(request):
    url = mano_settings.MANO_LOGOUT_URL + "?service=%s" % (
        settings.MANO_APPLICATION_NAME)
    if settings.DEBUG:
        port = request.get_host().split(':')[-1]
        url = '%s&port=%s' % (url, port)

    return redirect(url)
