# Generated by Django 3.0.6 on 2020-08-02 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendedperson',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]