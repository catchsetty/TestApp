# Generated by Django 2.2.13 on 2020-08-12 16:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200801_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, null=True)),
                ('ingredient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Ingredients')),
            ],
        ),
        migrations.CreateModel(
            name='StockInstance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stock_date', models.DateField(default=datetime.date.today, unique_for_date=True)),
                ('stock_status', models.CharField(choices=[('n', 'New'), ('ip', 'In Progress'), ('d', 'Done')], default='n', max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='orders',
            name='ordered_by',
            field=models.CharField(blank=True, default='WC', max_length=80),
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
        migrations.AddField(
            model_name='stockdetails',
            name='stock_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.StockInstance'),
        ),
    ]