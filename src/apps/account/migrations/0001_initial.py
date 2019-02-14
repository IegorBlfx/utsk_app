# Generated by Django 2.1.5 on 2019-02-14 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('commentary', models.CharField(max_length=14)),
                ('bank_mfo', models.IntegerField()),
                ('bank_name', models.CharField(max_length=30)),
                ('payment_account', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Counterparty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownership_type', models.SmallIntegerField(choices=[(1, 'TOV'), (2, 'FOP'), (3, 'PP'), (4, 'ZAT')])),
                ('name', models.CharField(max_length=120)),
                ('inn', models.IntegerField()),
                ('edrpou', models.IntegerField()),
                ('adress_by_documents', models.CharField(max_length=200)),
                ('adress_by_fact', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('create_by', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('doc_date', models.DateField()),
                ('doc_number', models.CharField(max_length=15)),
                ('created_by', models.CharField(max_length=15)),
                ('created_date', models.DateField()),
                ('paid', models.BooleanField()),
                ('commentary', models.CharField(max_length=30)),
                ('do_smth', models.BooleanField()),
                ('delete', models.BooleanField()),
                ('contract', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Contract')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_to_product', models.CharField(max_length=30)),
                ('weigth_product', models.FloatField()),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Document')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OtherData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport_type', models.SmallIntegerField(choices=[(1, ' Sat'), (2, 'Delivery'), (3, 'Car')])),
                ('transport_mark', models.SmallIntegerField(choices=[(1, 'Mers'), (2, 'Zil'), (3, 'Maz'), (4, 'Gazel')])),
                ('transport_number', models.CharField(max_length=8)),
                ('trailer_number', models.CharField(max_length=8)),
                ('driver', models.CharField(max_length=30)),
                ('driver_license', models.CharField(max_length=10)),
                ('attorney_list_number', models.CharField(max_length=5)),
                ('attorney_list_from', models.DateField()),
                ('attorney_name', models.CharField(max_length=25)),
                ('date_of_payment', models.DateField()),
                ('date_of_loading', models.DateField()),
                ('term_reservation', models.DateField()),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Document')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(max_length=50)),
                ('playground', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('commentary', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width_shs', models.FloatField(blank=True, null=True)),
                ('height_shs', models.FloatField(blank=True, null=True)),
                ('diameter_pipe', models.FloatField(blank=True, null=True)),
                ('wall', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length_from', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12')])),
                ('length_to', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12')])),
                ('wall_thickness_max', models.FloatField(blank=True, null=True)),
                ('wall_thickness_min', models.FloatField(blank=True, null=True)),
                ('radius_rounding_max', models.FloatField(blank=True, null=True)),
                ('radius_rounding_min', models.FloatField(blank=True, null=True)),
                ('pipe_diam_out', models.FloatField(blank=True, null=True)),
                ('pipe_diam_in', models.FloatField(blank=True, null=True)),
                ('uktzed', models.IntegerField(blank=True, null=True)),
                ('price_in', models.FloatField(blank=True, null=True)),
                ('price_in_nds', models.FloatField(blank=True, null=True)),
                ('price_out', models.FloatField(blank=True, null=True)),
                ('price_out_NDS', models.FloatField(blank=True, null=True)),
                ('weight_acc', models.FloatField(blank=True, null=True)),
                ('weight_fact', models.FloatField(blank=True, null=True)),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Document')),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Place')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.SmallIntegerField(choices=[(1, 'GOST 8732'), (2, 'GOST 8734'), (3, 'GOST 10705'), (4, 'GOST 10706'), (5, 'TU UV  2.7 , 2.4.45')])),
                ('steel', models.SmallIntegerField(choices=[(1, 'steel 20'), (2, 'steel 35'), (4, 'steel 09G2S')])),
                ('comment', models.TextField(blank=True, max_length=15, null=True)),
                ('strength_yield', models.SmallIntegerField()),
                ('strength_tensile', models.SmallIntegerField()),
                ('extending', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='purchaseinvoice',
            name='standard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Standard'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.PurchaseInvoice'),
        ),
        migrations.AddField(
            model_name='counterparty',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Location'),
        ),
        migrations.AddField(
            model_name='contract',
            name='counterparty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Counterparty'),
        ),
    ]
