# Generated by Django 2.2.8 on 2020-07-06 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datamasterapp', '0003_featuredetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feature_Title', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='featuredetail',
            name='Feature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datamasterapp.MainFeature'),
        ),
    ]