# Generated by Django 2.1 on 2018-08-14 17:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0046_auto_20180808_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teams.TeamMember')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='teams.TeamTask')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]