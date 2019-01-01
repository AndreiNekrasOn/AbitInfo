# Generated by Django 2.1.4 on 2019-01-01 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olcalc', '0008_qspeciality'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.RemoveField(
            model_name='testfaculty',
            name='olymps',
        ),
        migrations.RemoveField(
            model_name='testuniver',
            name='f_title',
        ),
        migrations.RemoveField(
            model_name='univer_plus',
            name='olymps',
        ),
        migrations.AlterField(
            model_name='qmapping',
            name='unifac',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olcalc.QSpeciality'),
        ),
        migrations.AlterField(
            model_name='qolymp',
            name='subject',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Olymp',
        ),
        migrations.DeleteModel(
            name='TestFaculty',
        ),
        migrations.DeleteModel(
            name='TestUniver',
        ),
        migrations.DeleteModel(
            name='Univer_plus',
        ),
    ]