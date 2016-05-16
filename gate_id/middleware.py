import requests
from unipath import Path

from django.contrib.auth import authenticate, login, get_user_model
from django.utils.functional import SimpleLazyObject

from gate_id import settings

User = get_user_model()

class GateSessionMiddleware(object):

    def process_request(self, request):
        if request.user.is_anonymous():
            gate_id = request.COOKIES.get(settings.GATE_COOKIE_NAME)
            gate_user = requests.get(
                settings.GATE_ID_URL,
                cookies = {settings.GATE_COOKIE_NAME: gate_id},
                verify = Path(settings.BASE_DIR, 'certs.pem')
            ).json()

            if gate_user:
                try:
                    user = User.objects.get(email=gate_user['email'], uuid=gate_user['uuid'])
                except User.DoesNotExist:
                    user = User.objects.create_user(gate_user['email'], uuid=gate_user['uuid'])

                user.first_name = gate_user['first_name']
                user.last_name = gate_user['last_name']
                user.save()

                user.backend = 'django.contrib.auth.backend.ModelBackend'

                login(request, user)
