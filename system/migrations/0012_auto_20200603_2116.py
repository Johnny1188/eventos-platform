# Generated by Django 3.0.6 on 2020-06-03 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0011_eventgoer_eventbuddy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventgoer',
            name='eventBuddy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.EventGoer'),
        ),
    ]