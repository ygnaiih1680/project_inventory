from django import template
register = template.Library()


@register.simple_tag
def define(var):
    return var
