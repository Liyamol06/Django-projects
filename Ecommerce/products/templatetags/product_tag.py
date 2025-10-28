from django import template


register=template.Library()

@register.filter(name='product_tag')
def product_tag(list_data, limits):
    data_items=[]
    i=0
    for item in list_data:
        data_items.append(item)
        i=i+1
        if i==limits:
            yield  data_items
            data_items, i=[], 0
    if data_items:    
        yield data_items
