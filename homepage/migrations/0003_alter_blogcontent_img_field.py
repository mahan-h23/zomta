# Generated by Django 4.1.7 on 2023-02-28 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_alter_blogcontent_homepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcontent',
            name='img_field',
            field=models.ImageField(blank=True, null=True, upload_to='homepage'),
        ),
    ]
