# Generated by Django 2.2.12 on 2020-08-16 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moves', '0001_add_camera_movelog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='camera',
            options={'verbose_name': 'Camera', 'verbose_name_plural': 'Cameras'},
        ),
        migrations.AlterField(
            model_name='camera',
            name='from_room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='from_cameras', related_query_name='from_camera', to='companies.Room', verbose_name='Exit Room Camera'),
        ),
        migrations.AlterField(
            model_name='camera',
            name='to_room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='to_cameras', related_query_name='to_camera', to='companies.Room', verbose_name='Enter Room Camera'),
        ),
    ]
