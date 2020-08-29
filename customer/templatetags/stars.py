from django import template


register = template.Library()
@register.simple_tag()

def countStars(totalstars):
    list = []
    for i in range(0,totalstars):
        list.append(i)
    return list    

@register.simple_tag()
def countStars2(totalStars):
    totalStars2 = 5 - totalStars
    list2 = []
    for i in range(0,totalStars2):
        list2.append(i)
    return list2    