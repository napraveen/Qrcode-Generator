# Generated by Django 4.1.2 on 2023-02-03 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_register_delete_inputdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='address',
            new_name='data',
        ),
        migrations.RemoveField(
            model_name='register',
            name='email',
        ),
        migrations.RemoveField(
            model_name='register',
            name='name',
        ),
        migrations.RemoveField(
            model_name='register',
            name='phone',
        ),
    ]