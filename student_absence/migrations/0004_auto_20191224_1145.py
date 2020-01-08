# Generated by Django 2.2.8 on 2019-12-24 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_absence', '0003_studentabsencesettingsmodel_filter_students_for_educ'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='studentabsencemodel',
            name='period',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student_absence.PeriodModel'),
        ),
        migrations.AddField(
            model_name='studentabsencemodel',
            name='is_absent',
            field=models.BooleanField("Étudiant absent", default=False),
        ),
    ]