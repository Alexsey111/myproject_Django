from jinja2 import Environment as Jinja2Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

def Environment(**options):
    env = Jinja2Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env
