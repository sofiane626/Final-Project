# Generated by Django 4.2.2 on 2023-07-08 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_anonymoususer2_note2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note2',
            old_name='product',
            new_name='article',
        ),
    ]