# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('game', models.CharField(max_length=100)),
                ('stage', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(related_name='groups_created', to=settings.AUTH_USER_MODEL)),
                ('teammates', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='groups_joined')),
            ],
        ),
    ]
