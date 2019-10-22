# Generated by Django 2.2.6 on 2019-10-22 18:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(help_text='Type a note, if you dare')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 10, 22, 18, 54, 11, 30426, tzinfo=utc))),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
