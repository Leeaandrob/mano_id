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

3. Use Gate ID User Model:
    AUTH_USER_MODEL = 'gate_id.User'

4. Include the gate_id URLconf in your project urls.py like this::

```
    import gate_id
    url(r'^', include(gate_id.urls, namespace='gate_id')),
```

5. Run `python manage.py migrate` to create the Gate ID models.
