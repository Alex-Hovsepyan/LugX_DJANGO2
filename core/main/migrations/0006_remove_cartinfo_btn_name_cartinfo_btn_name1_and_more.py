# Generated by Django 4.2.1 on 2023-05-25 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_userorder_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartinfo',
            name='btn_name',
        ),
        migrations.AddField(
            model_name='cartinfo',
            name='btn_name1',
            field=models.CharField(default=1, max_length=40, verbose_name='Button Name 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartinfo',
            name='btn_name2',
            field=models.CharField(default=1, max_length=40, verbose_name='Button Name 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartinfo',
            name='count_title',
            field=models.CharField(default=1, max_length=50, verbose_name='Count Title'),
            preserve_default=False,
        ),
    ]
