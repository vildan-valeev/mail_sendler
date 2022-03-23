from urllib import urlencode
from urlparse import urlparse, parse_qs

from django import template


register = template.Library()


@register.simple_tag
def modify_pagination_path(full_path, key, value):
    get_params = full_path
    if get_params.find('?') > -1:
        get_params = get_params[get_params.find('?')+1:]
    if get_params.find('#') > -1:
        get_params = get_params[:get_params.find('#')]

    params = parse_qs(get_params)
    params[key] = [str(value)]
    return urlencode(params, doseq=True)
