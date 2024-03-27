from django import template

register = template.Library()

@register.filter
def split_paragraphs(text):
    return text.split('\n')