# Generated by Django 2.1.7 on 2019-02-20 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kubeportal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kubernetesnamespace',
            name='uid',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='kubernetesserviceaccount',
            name='uid',
            field=models.CharField(max_length=50, null=True),
        ),
    ]