# Generated by Django 2.1.4 on 2019-01-01 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olcalc', '0009_auto_20190101_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='QPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
