import requests

from django.contrib.auth import login, get_user_model

from mano_id import settings


User = get_user_model()


class ManoSessionMiddleware(object):

    def process_request(self, request):
        if request.user.is_anonymous():
            mano_id = request.COOKIES.get(settings.MANO_COOKIE_NAME)
            mano_user = requests.get(
                settings.MANO_ID_URL,
                cookies={settings.MANO_COOKIE_NAME: mano_id}
            ).json()

            if mano_user:
                try:
                    user = User.objects.get(email=mano_user['email'],
                                            uuid=mano_user['uuid'])
                except User.DoesNotExist:
                    user = User.objects.create_user(mano_user['email'],
                                                    uuid=mano_user['uuid'])

                user.first_name = mano_user['first_name']
                user.last_name = mano_user['last_name']
                user.save()

                user.backend = 'django.contrib.auth.backend.ModelBackend'

                login(request, user)
