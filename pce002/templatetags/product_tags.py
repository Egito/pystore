from django import template

register = template.Library()

@register.filter()
def reminder(n):
    return n % 3

