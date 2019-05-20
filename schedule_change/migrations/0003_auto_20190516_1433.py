# Generated by Django 2.0.9 on 2019-05-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_change', '0002_auto_20190516_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulechangecategorymodel',
            name='icon',
            field=models.CharField(default='', help_text='Icône utilisée par Font Awesome 4.7.', max_length=50),
        ),
        migrations.AlterField(
            model_name='schedulechangecategorymodel',
            name='color',
            field=models.CharField(default='', help_text='Valeur hexadecimal de la couleur.', max_length=6),
        ),
    ]
