# Generated by Django 2.1.5 on 2019-02-12 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190209_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField()),
                ('contract_type', models.SmallIntegerField(choices=[(1, 'Supply'), (2, 'Sells')])),
                ('contract_number', models.CharField(max_length=15)),
                ('our_company', models.SmallIntegerField(choices=[(1, 'Ugtransstroycompect'), (2, 'Pifagor'), (3, 'Forpost')])),
                ('type_nds', models.SmallIntegerField(choices=[(1, '20%'), (2, '5%'), (3, '0%')])),
                ('contract_currency', models.SmallIntegerField(choices=[(1, 'UAH'), (2, 'USD'), (3, 'EUR')])),
                ('contract_from', models.DateField()),
                ('contract_to', models.DateField()),
                ('contract_amount', models.FloatField()),
                ('created_by', models.CharField(max_length=15)),
                ('counterparty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Counterparty')),
            ],
        ),
    ]
