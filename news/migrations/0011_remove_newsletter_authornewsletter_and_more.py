# Generated by Django 4.1.4 on 2023-01-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_rename_user_newsletter_authornewsletter_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='authorNewsletter',
        ),
        migrations.AlterField(
            model_name='code',
            name='user_code',
            field=models.CharField(default='9301', max_length=4),
        ),
    ]
