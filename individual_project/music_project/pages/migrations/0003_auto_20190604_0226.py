# Generated by Django 2.2.1 on 2019-06-04 02:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_musicians_playlist_usersongs'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersongs',
            name='playlist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pages.Playlist', verbose_name='Плэйлист'),
        ),
        migrations.AddField(
            model_name='usersongs',
            name='song',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pages.Song', verbose_name='Песня'),
        ),
        migrations.AlterField(
            model_name='usersongs',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
