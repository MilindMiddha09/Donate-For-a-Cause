# Generated by Django 4.2 on 2023-05-29 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_alter_registration_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='Verification',
            field=models.FileField(max_length=250, null=True, upload_to='Registration/'),
        ),
    ]
