# Generated by Django 3.1 on 2020-10-08 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('STR_app', '0003_auto_20201005_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='action_taken',
        ),
        migrations.RemoveField(
            model_name='record',
            name='alternative_thought',
        ),
        migrations.RemoveField(
            model_name='record',
            name='emotion',
        ),
        migrations.RemoveField(
            model_name='record',
            name='negative_thought',
        ),
        migrations.RemoveField(
            model_name='record',
            name='situation',
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('unread', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('from_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_sender', to='STR_app.patient')),
                ('from_therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='therapist_sender', to='STR_app.therapist')),
                ('to_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_reciever', to='STR_app.patient')),
                ('to_therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='therapist_receiver', to='STR_app.therapist')),
            ],
        ),
    ]