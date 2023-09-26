from django import template
register = template.Library()


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.copy()
    for key, value in kwargs.items():
        query[key] = value
    return query.urlencode()


@register.filter
def custom_range(value, arg):
    if value == None:
        value = 0
    start, end = arg.split(",")
    return range(value + int(start), value + int(end) + 1)