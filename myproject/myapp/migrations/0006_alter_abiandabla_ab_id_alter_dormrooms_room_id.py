# Generated by Django 4.0.4 on 2022-05-09 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_dormstudents_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abiandabla',
            name='ab_id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dormrooms',
            name='room_id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]