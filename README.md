=====
Gate ID
=====

Gate ID is an app to make easy to integrate with Gate ID SSO.

Quick start
-----------

1. Add "gate_id" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'gate_id',
    ]

2. Add serverside settings like this:
    GATE_APPLICATION_NAME = 'subdomain-app-name'
    GATE_URL = 'https://accounts.gate.cx/'

3. Add Gate ID Middleware in the end of middlewares list:
    MIDDLEWARE_CLASSES = (
        ...
        'gate_id.middleware.GateSessionMiddleware',
    )

4. Use Gate ID User Model:
    AUTH_USER_MODEL = 'gate_id.User'

5. Include the gate_id URLconf in your project urls.py like this::

    url(r'^', include(gate_id.urls, namespace='gate_id')),

6. Run `python manage.py migrate` to create the Gate ID models.
