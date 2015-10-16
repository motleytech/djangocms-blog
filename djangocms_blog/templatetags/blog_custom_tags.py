from django import template
from django.conf import settings
from traceback import print_exc
import logging

register = template.Library()

@register.assignment_tag(takes_context=True)
def get_static_placeholder(context):
    try:
        path = context.get('request').path
        path = "/".join(path.split("/")[:3])
        if path in settings.STATIC_PLACEHOLDER_MAP:
            return settings.STATIC_PLACEHOLDER_MAP[path]
        return settings.STATIC_PLACEHOLDER_MAP['default']
    except:
        logging.exception("Error in get_static_placeholder tag.\n\
        Possibly missing the STATIC_PLACEHOLDER_MAP in settings.py")


    # fallback value in case nothing works
    return "blog-sidebar"
