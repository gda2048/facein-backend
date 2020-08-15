# Generated by Django 2.2.12 on 2020-08-15 23:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_fix_user_model'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blackwhitelist',
            options={'verbose_name': 'Black list and white list', 'verbose_name_plural': 'Black lists and white lists'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username'], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterField(
            model_name='blackwhitelist',
            name='is_blacklisted',
            field=models.BooleanField(default=False, verbose_name='Blacklisted'),
        ),
        migrations.AlterField(
            model_name='blackwhitelist',
            name='is_whitelisted',
            field=models.BooleanField(default=False, verbose_name='Whitelisted'),
        ),
        migrations.AlterField(
            model_name='blackwhitelist',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_lists', related_query_name='user_list', to='companies.Room', verbose_name='Room'),
        ),
        migrations.AlterField(
            model_name='blackwhitelist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', related_query_name='room', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', related_query_name='user', to='companies.Company', verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='user',
            name='info',
            field=models.TextField(blank=True, max_length=255, verbose_name='Additional notes'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_blacklisted',
            field=models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. ', verbose_name='blacklisted'),
        ),
    ]
