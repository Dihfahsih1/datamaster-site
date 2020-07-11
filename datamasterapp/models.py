from django.db import models
class CompanyDetail(models.Model):
    company_name = models.CharField(max_length=130, blank=True, null=True)
    company_logo = models.ImageField(upload_to='logo/',blank=True, null=True)
    address = models.CharField(max_length=130, blank=True, null=True)
    phone = models.CharField(max_length=130, blank=True, null=True)
    email_address = models.EmailField(max_length=120)
    facebook_url = models.URLField(max_length=130, blank=True, null=True)
    youtube_url = models.URLField(max_length=130, blank=True, null=True)
    footer = models.CharField(max_length=130, blank=True, null=True)
    class Meta:
        default_permissions = ('view', 'add', 'change', 'delete')
       
    def __str__(self):
        return self.company_name
class MainFeature(models.Model):
    Feature_Title = models.CharField(max_length=500, blank=True, null=True)
    Feature_Sub_Title = models.CharField(max_length=50000,blank=True, null=True)
    Feature_Description = models.TextField(blank=True, null=True)
    Feature_Image = models.ImageField(upload_to='features/',max_length= 10000,blank=True, null=True)
    def __str__(self):
        return self.Feature_Title

class Feature(models.Model):
    Feature_Title = models.CharField(max_length=500, blank=True, null=True)
    Feature_Description = models.TextField(blank=True, null=True)
    Feature_Image = models.ImageField(upload_to='features/',max_length= 10000,blank=True, null=True)
    def __str__(self):
        return self.Feature_Title

class Reason(models.Model):
    Reason_Title = models.CharField(max_length=500, blank=True, null=True)
    Reason_Description = models.TextField(blank=True, null=True)
    Reason_Image = models.ImageField(upload_to='features/',max_length= 10000,blank=True, null=True)
    def __str__(self):
        return self.Reason_Title

class FeatureDetail(models.Model):
    Feature = models.ForeignKey(MainFeature, on_delete=models.CASCADE,blank=True, null=True)
    Feature_Sub_Title = models.CharField(max_length=500, blank=True, null=True)
    Feature_Sub_Description = models.TextField(blank=True, null=True)
    Feature_Sub_Image = models.ImageField(upload_to='features/',max_length= 10000,blank=True, null=True)
    def __str__(self):
        return self.Feature_Sub_Title + str('('+ self.Feature.Feature_Title + ')')

class Feedback(models.Model):
    full_name = models.CharField(max_length=100, blank=True, null=True, default='Name')
    email = models.CharField(max_length=100, blank=True, null=True, default='email@example.com')
    date=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True, default='Name')
    comment=models.TextField(blank=True, null=True)
    def __str__(self):
        return self.full_name
        
class Slider(models.Model):
    Date = models.DateTimeField(auto_now=True)
    slider_name = models.CharField(max_length=100, blank=True, null=True, default='slider')
    slider_image = models.ImageField(upload_to='sliders/',max_length=1000, blank=True, null=True)
    slider_description=models.TextField(max_length=1000,blank=True, null=True)
    def __str__(self):
        return self.slider_name