# Generated by Django 2.2.8 on 2020-03-12 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pia', '0011_auto_20200302_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchgoalmodel',
            name='assessment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pia.AssessmentModel'),
        ),
        migrations.AlterField(
            model_name='crossgoalmodel',
            name='assessment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pia.AssessmentModel'),
        ),
    ]