# Generated by Django 2.2.1 on 2019-06-09 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20190609_1601'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Musicians',
        ),
        migrations.RemoveField(
            model_name='song',
            name='youtube_link',
        ),
    ]