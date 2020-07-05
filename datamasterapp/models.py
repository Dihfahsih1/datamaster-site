from django.db import models

class Features(models.Model):
    Feature_Title = models.CharField(max_length=500, blank=True, null=True)
    Feature_Description = models.TextField(blank=True, null=True)
    Feature_Image = models.ImageField(upload_to='features/',max_length= 10000,blank=True, null=True)
    def __str__(self):
        return self.Feature_Title
