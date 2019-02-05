# Generated by Django 2.1.5 on 2019-02-05 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20190204_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_date', models.DateField()),
                ('act_number', models.SmallIntegerField()),
                ('counterparty', models.TextField()),
                ('length_from', models.FloatField()),
                ('length_to', models.FloatField()),
                ('wall_thickness_max', models.FloatField()),
                ('wall_thickness_min', models.FloatField()),
                ('radius_rounding_max', models.FloatField()),
                ('radius_rounding_min', models.FloatField()),
                ('pipe_diam_out', models.FloatField()),
                ('pipe_diam_in', models.FloatField()),
                ('uktzed', models.IntegerField()),
                ('price_in', models.FloatField()),
                ('price_in_nds', models.FloatField()),
                ('price_out', models.FloatField()),
                ('price_out_NDS', models.FloatField()),
                ('base_units_weight', models.TextField()),
                ('base_units_length', models.TextField()),
                ('weight_acc', models.FloatField()),
                ('weight_fact', models.FloatField()),
                ('stock', models.TextField()),
                ('place', models.TextField()),
                ('contract', models.TextField()),
                ('created_by', models.TextField()),
                ('create_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='height_shs',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='width_shs',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseinvoice',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Product'),
        ),
        migrations.AddField(
            model_name='purchaseinvoice',
            name='standard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Standard'),
        ),
        migrations.AddField(
            model_name='purchaseinvoice',
            name='steel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Steel'),
        ),
    ]