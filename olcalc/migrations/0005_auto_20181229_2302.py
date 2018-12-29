# Generated by Django 2.1.4 on 2018-12-29 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olcalc', '0004_auto_20181008_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='QFaculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='QMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='QOlymp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('level', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='QPrivilege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='QUniversuty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='qmapping',
            name='olymp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olcalc.QOlymp'),
        ),
        migrations.AddField(
            model_name='qmapping',
            name='privilege',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olcalc.QPrivilege'),
        ),
        migrations.AddField(
            model_name='qmapping',
            name='unifac',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olcalc.QFaculty'),
        ),
        migrations.AddField(
            model_name='qfaculty',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olcalc.QUniversuty'),
        ),
    ]
