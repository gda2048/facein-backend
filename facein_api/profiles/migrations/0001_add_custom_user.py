# Generated by Django 2.2.12 on 2020-05-24 15:45

import django.contrib.auth.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models

import profiles.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('companies', '0001_add_companies_rooms'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login',
                 models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.',
                                                     verbose_name='superuser status')),
                ('username', models.CharField(
                    error_messages={'unique': 'A user with that username already exists.'},
                    help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                    max_length=150, unique=True,
                    validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                    verbose_name='username')),
                ('first_name',
                 models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name',
                 models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_security', models.BooleanField(default=False,
                                                    help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                                                    verbose_name='security status')),
                ('is_admin', models.BooleanField(default=False,
                                                 help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                                                 verbose_name='admin status')),
                ('is_blacklisted', models.BooleanField(default=False,
                                                       help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                                                       verbose_name='black list status')),
                ('info', models.CharField(blank=True, help_text='Info.', max_length=255,
                                          verbose_name='info')),
                (
                'date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                              related_name='users', related_query_name='user',
                                              to='companies.Company', verbose_name='Компания')),
                ('groups', models.ManyToManyField(blank=True,
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set',
                                                  related_query_name='user', to='auth.Group',
                                                  verbose_name='groups')),
                ('user_permissions',
                 models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                        related_name='user_set', related_query_name='user',
                                        to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', profiles.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BlackWhiteList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('is_blacklisted',
                 models.BooleanField(default=False, verbose_name='В черном списке')),
                ('is_whitelisted',
                 models.BooleanField(default=False, verbose_name='В белом списке')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='user_lists',
                                           related_query_name='user_list', to='companies.Room',
                                           verbose_name='Помещение')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='rooms', related_query_name='room',
                                           to=settings.AUTH_USER_MODEL,
                                           verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Черный и Белый Списки Помещения',
                'verbose_name_plural': 'Черный и Белый Списки Помещений',
                'unique_together': {('room', 'user')},
            },
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.CheckConstraint(
                check=models.Q(('is_blacklisted', True), ('is_superuser', True), _negated=True),
                name='superusers_are_not_blocked'),
        ),
    ]
