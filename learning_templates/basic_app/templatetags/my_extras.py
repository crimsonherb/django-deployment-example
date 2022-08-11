from django import template

register = template.Library()

def destroy(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.replace(arg,'')


register.filter('destroy',destroy)