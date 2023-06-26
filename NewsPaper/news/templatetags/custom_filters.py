from django import template


register = template.Library()


@register.filter()
def censor(word):
    bad_words = ['редиска', 'мат']
    if isinstance(word, str):
        for i in word.split():
            if i in bad_words:
                word = word.replace(i, i[0] + '*' * len(i[1:]))
    return word


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['requests'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()

