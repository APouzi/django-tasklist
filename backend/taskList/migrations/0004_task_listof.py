# Generated by Django 4.0.2 on 2022-02-17 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskList', '0003_usertasklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='listof',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taskList.usertasklist'),
        ),
    ]
