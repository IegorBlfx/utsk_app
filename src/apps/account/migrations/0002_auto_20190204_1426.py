# Generated by Django 2.1.5 on 2019-02-04 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standard',
            name='comment',
            field=models.TextField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='standard',
            name='name',
            field=models.TextField(max_length=15),
        ),
        migrations.AlterField(
            model_name='standard',
            name='number',
            field=models.TextField(max_length=15),
        ),
        migrations.AlterField(
            model_name='steel',
            name='name',
            field=models.TextField(max_length=15),
        ),
    ]
