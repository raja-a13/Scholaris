# Generated by Django 2.0.6 on 2018-11-10 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test_Designing', '0003_auto_20181110_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='mark',
            field=models.IntegerField(default=0),
        ),
    ]
