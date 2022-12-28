from django import template

from store.models import Image

register = template.Library()

@register.filter(name='get_first_image')
def get_first_image(product):
    img = Image.objects.filter(product=product).first()
    if img:
        return img.image.url
    else: 
        return False