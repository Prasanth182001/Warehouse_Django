# Generated by Django 4.1.4 on 2023-04-10 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table_p',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Products', models.CharField(max_length=20)),
                ('Quantity', models.IntegerField()),
            ],
        ),
    ]
