# Generated by Django 3.1 on 2020-10-08 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STR_app', '0004_auto_20201008_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message_content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='action_taken',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='alternative_thought',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='emotion',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='negative_thought',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='situation',
            field=models.TextField(null=True),
        ),
    ]
