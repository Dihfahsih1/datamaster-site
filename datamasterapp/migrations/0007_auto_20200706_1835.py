# Generated by Django 2.2.8 on 2020-07-06 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamasterapp', '0006_mainfeature_feature_sub_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainfeature',
            name='Feature_Sub_Title',
            field=models.CharField(blank=True, max_length=50000, null=True),
        ),
    ]