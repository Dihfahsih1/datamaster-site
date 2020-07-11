# Generated by Django 2.2.8 on 2020-07-11 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datamasterapp', '0011_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='slider_feature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datamasterapp.MainFeature'),
        ),
    ]
