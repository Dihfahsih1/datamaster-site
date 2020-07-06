from django import template
from ..models import *

register = template.Library()
@register.simple_tag
def phone_number():
    detail = CompanyDetail.objects.get(id=1)
    number = detail.phone
    return number

@register.simple_tag
def Emailaddress():
    detail = CompanyDetail.objects.get(id=1)
    address = detail.email_address
    return address

@register.simple_tag
def physical_address():
    detail = CompanyDetail.objects.get(id=1)
    area_address = detail.address
    return area_address

@register.simple_tag
def name():
    detail = CompanyDetail.objects.get(id=1)
    full_name = detail.company_name
    return full_name
 
@register.simple_tag
def facebook():
    fb = CompanyDetail.objects.get(id=1)
    facbook = fb.facebook_url
    return facbook

@register.simple_tag
def youtube():
    yt = CompanyDetail.objects.get(id=1)
    youtu = yt.youtube_url
    return youtu    

@register.simple_tag
def logo():
    log = CompanyDetail.objects.get(id=1)
    x = log.company_logo.url
    return x       

@register.simple_tag
def company_footer():
    foot = CompanyDetail.objects.get(id=1)
    x = foot.footer
    return x       