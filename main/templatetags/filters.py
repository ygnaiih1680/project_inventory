from django import template

register = template.Library()


@register.filter
def key(arr, i):
    return arr[i]


@register.filter
def odd(num):
    return num % 2 == 1


@register.filter
def length(param):
    return len(param)


@register.filter
def arr_str(arr):
    return ", ".join(arr)


@register.filter
def str_split(string):
    return string.strip().split()
