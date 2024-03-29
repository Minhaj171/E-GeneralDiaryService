# Generated by Django 2.2.7 on 2019-12-16 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adminn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='policeComplain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Complain_type', models.CharField(max_length=55)),
                ('Complainant_name', models.CharField(max_length=55)),
                ('Mobile_Number', models.CharField(max_length=55)),
                ('National_id', models.CharField(max_length=55)),
                ('District', models.CharField(max_length=55)),
                ('Thana', models.CharField(max_length=55)),
                ('Address', models.CharField(max_length=55)),
                ('Complain_description', models.CharField(max_length=55)),
                ('Email', models.EmailField(max_length=50, unique=True)),
            ],
        ),
    ]
