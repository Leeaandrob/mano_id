from django.conf import settings

MANO_URL = settings.MANO_URL
MANO_COOKIE_NAME = getattr(settings, 'MANO_COOKIE_NAME', 'manoid')
MANO_ID_URL = getattr(settings, 'MANO_ID_URL', MANO_URL + "me/")
MANO_LOGIN_URL = getattr(settings, 'MANO_LOGIN_URL', MANO_URL + "login/")
MANO_LOGOUT_URL = getattr(settings, 'MANO_LOGOUT_URL',  MANO_URL + "logout/")
