"""
WSGI config for pdf_extractor project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pdf_extractor.settings")

application = get_wsgi_application()
<<<<<<< HEAD
app = application
=======
>>>>>>> 894003f0bc5a2011ead0ba96e26d6d23d8ff31e7