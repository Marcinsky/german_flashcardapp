# Generated by Django 4.2.7 on 2023-11-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('german_word', models.CharField(max_length=100)),
                ('english_word', models.CharField(max_length=100)),
            ],
        ),
    ]
