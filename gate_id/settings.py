from django.conf import settings

GATE_URL = settings.GATE_URL
GATE_COOKIE_NAME = getattr(settings, 'GATE_COOKIE_NAME', 'gateid')
GATE_ID_URL = getattr(settings, 'GATE_ID_URL', GATE_URL + "me/")
GATE_LOGIN_URL =  getattr(settings, 'GATE_LOGIN_URL', GATE_URL + "login/")
GATE_LOGOUT_URL =  getattr(settings, 'GATE_LOGOUT_URL',  GATE_URL + "logout/")
