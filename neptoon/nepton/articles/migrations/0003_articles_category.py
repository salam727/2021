# Generated by Django 3.1.1 on 2020-09-12 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='Category',
            field=models.ManyToManyField(to='articles.Category', verbose_name='Category'),
        ),
    ]