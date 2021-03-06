# Generated by Django 3.0.6 on 2020-06-04 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20200603_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='13 Character ISBN number</a>', max_length=13, verbose_name='ISBN'),
        ),
    ]
