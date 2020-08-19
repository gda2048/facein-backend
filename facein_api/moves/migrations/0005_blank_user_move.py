# Generated by Django 2.2.12 on 2020-08-19 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moves', '0004_null_user_move'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movelog',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='logs', related_query_name='log', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
