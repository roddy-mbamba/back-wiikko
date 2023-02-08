# Generated by Django 4.1.5 on 2023-02-07 09:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField()),
                ('createAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('UpdateAt', models.DateTimeField(auto_now=True)),
                ('user', models.ManyToManyField(related_name='message_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]