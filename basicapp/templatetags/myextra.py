from django import template

#register = template.library()

#@register.filter(name='cut')
def cut(value,arg):
    #It cuts all values from the arg string
    return value.replace(arg,'')

#register.filter('cut',cut)
