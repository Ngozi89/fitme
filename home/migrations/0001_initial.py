# Generated by Django 3.2.24 on 2024-03-14 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memb_name', models.CharField(max_length=50)),
                ('memb_email', models.IntegerField()),
            ],
        ),
    ]