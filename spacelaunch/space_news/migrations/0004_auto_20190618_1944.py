# Generated by Django 2.2.2 on 2019-06-18 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space_news', '0003_auto_20190618_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launches',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(),
        ),
    ]
