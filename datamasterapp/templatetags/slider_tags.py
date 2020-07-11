from django import template
from ..models import *

register = template.Library()
#get slider1 details
@register.simple_tag
def sliding_name1():
    detail = Slider.objects.get(id=1)
    name = detail.slider_feature.Feature_Title
    return name

@register.simple_tag
def sliding_image1():
    detail = Slider.objects.get(id=1)
    image = detail.slider_feature.Feature_Image.url
    return image  

@register.simple_tag
def sliding_sub_title1():
    detail = Slider.objects.get(id=1)
    x = detail.slider_feature.Feature_Sub_Title
    return x 

@register.simple_tag
def sliding_description1():
    detail = Slider.objects.get(id=1)
    x = detail.slider_feature.Feature_Description
    return x 

#get slider2 details
@register.simple_tag
def sliding_name2():
    detail = Slider.objects.get(id=2)
    name = detail.slider_feature.Feature_Title
    return name
    
@register.simple_tag
def sliding_image2():
    detail = Slider.objects.get(id=2)
    image = detail.slider_feature.Feature_Image.url
    return image 

@register.simple_tag
def sliding_sub_title2():
    detail = Slider.objects.get(id=2)
    x = detail.slider_feature.Feature_Sub_Title
    return x 

@register.simple_tag
def sliding_description2():
    detail = Slider.objects.get(id=2)
    x = detail.slider_feature.Feature_Description
    return x 

#get slider3 details
@register.simple_tag
def sliding_name3():
    detail = Slider.objects.get(id=3)
    name = detail.slider_feature.Feature_Title
    return name
    
@register.simple_tag
def sliding_image3():
    detail = Slider.objects.get(id=3)
    image = detail.slider_feature.Feature_Image.url
    return image  

@register.simple_tag
def sliding_sub_title3():
    detail = Slider.objects.get(id=3)
    x = detail.slider_feature.Feature_Sub_Title
    return x 

@register.simple_tag
def sliding_description3():
    detail = Slider.objects.get(id=3)
    x = detail.slider_feature.Feature_Description
    return x 


#get slider4 details
@register.simple_tag
def sliding_name4():
    detail = Slider.objects.get(id=4)
    name = detail.slider_feature.Feature_Title
    return name

@register.simple_tag
def sliding_image4():
    detail = Slider.objects.get(id=4)
    image = detail.slider_feature.Feature_Image.url
    return image 

@register.simple_tag
def sliding_sub_title4():
    detail = Slider.objects.get(id=4)
    x = detail.slider_feature.Feature_Sub_Title
    return x 

@register.simple_tag
def sliding_description4():
    detail = Slider.objects.get(id=4)
    x = detail.slider_feature.Feature_Description
    return x 