# Generated by Django 2.2.5 on 2021-07-23 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapplication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
