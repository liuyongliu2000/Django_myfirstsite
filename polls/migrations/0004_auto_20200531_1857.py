# Generated by Django 3.0.6 on 2020-05-31 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
