# Generated by Django 2.2.1 on 2019-06-07 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20190605_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(null=True, to='pages.Song'),
        ),
        migrations.DeleteModel(
            name='UserSongs',
        ),
    ]
