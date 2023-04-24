from django import template

register = template.Library()

@register.filter
def lookup(dic, key):
    return dic[str(key)]