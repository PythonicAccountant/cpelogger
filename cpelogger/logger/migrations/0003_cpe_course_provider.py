# Generated by Django 3.1.12 on 2021-06-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0002_cpe_course_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpe',
            name='course_provider',
            field=models.CharField(default='P', max_length=200),
            preserve_default=False,
        ),
    ]
