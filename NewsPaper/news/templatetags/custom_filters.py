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

