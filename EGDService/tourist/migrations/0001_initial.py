# Generated by Django 2.2.7 on 2019-12-14 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PoliceVerification',
            fields=[
                ('Verification_id', models.AutoField(primary_key=True, serialize=False)),
                ('Tourist_name', models.CharField(max_length=55)),
                ('C_tourist', models.CharField(max_length=55)),
                ('Tourist_M', models.CharField(max_length=55)),
                ('Tourist_Email', models.EmailField(max_length=50, unique=True)),
                ('Tourist_duration', models.CharField(max_length=55)),
                ('Passport_id', models.CharField(max_length=55)),
            ],
        ),
    ]