# Generated by Django 2.0.3 on 2018-04-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_support'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='AdminText',
            field=models.TextField(blank=True, null=True, verbose_name='管理员回复文本'),
        ),
    ]
