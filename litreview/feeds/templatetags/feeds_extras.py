from django import template

register = template.Library()


@register.filter
def model_type(instance):
    return type(instance).__name__


@register.filter
def subtract(value, arg):
    return value - arg


@register.simple_tag(takes_context=True)
def get_user_display(context, user):
    if user == context["user"]:
        return "Vous avez"
    return user.username + " a"
