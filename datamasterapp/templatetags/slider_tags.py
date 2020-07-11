from django import template
from ..models import *

register = template.Library()
@register.simple_tag
def sliding_name1():
    detail = Slider.objects.get(id=1)
    name = detail.slider_name
    return name

@register.simple_tag
def sliding_image1():
    detail = Slider.objects.get(id=1)
    image = detail.slider_image.url
    return image       
@register.simple_tag
def sliding_description1():
    detail = Slider.objects.get(id=1)
    x = detail.slider_description
    return x 

@register.simple_tag
def sliding_name2():
    detail = Slider.objects.get(id=2)
    name = detail.slider_name
    return name
    
@register.simple_tag
def sliding_image2():
    detail = Slider.objects.get(id=2)
    image = detail.slider_image.url
    return image  
@register.simple_tag
def sliding_description2():
    detail = Slider.objects.get(id=2)
    x = detail.slider_description
    return x 

# @register.simple_tag
# def sliding_name3():
#     detail = Slider.objects.get(id=3)
#     name = detail.slider_name
#     return name
    
# @register.simple_tag
# def sliding_image3():
#     detail = Slider.objects.get(id=3)
#     image = detail.slider_image.url
#     return image         
# @register.simple_tag
# def sliding_description3():
#     detail = Slider.objects.get(id=3)
#     x = detail.slider_description
#     return x     