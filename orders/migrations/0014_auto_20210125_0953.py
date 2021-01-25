# Generated by Django 2.2.13 on 2021-01-25 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20201229_0839'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderdetails',
            options={'verbose_name': 'Order Details', 'verbose_name_plural': 'Order Details'},
        ),
        migrations.AddField(
            model_name='orders',
            name='pay_status',
            field=models.CharField(choices=[('Fully-Paid', 'Fully-Paid'), ('Partial', 'Partial'), ('Not-Paid', 'Not-Paid')], default='Not-Paid', max_length=20),
        ),
    ]
