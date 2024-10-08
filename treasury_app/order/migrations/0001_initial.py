# Generated by Django 5.1.1 on 2024-09-30 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(choices=[('1M', '1 Month'), ('3M', '3 Month'), ('6M', '6 Month'), ('1Y', '1 Year'), ('2Y', '2 Year'), ('5Y', '5 Year'), ('10Y', '10 Year'), ('20Y', '20 Year'), ('30Y', '30 Year')], max_length=3)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('yield_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_of_purchase', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.CharField(default='submitted', max_length=20)),
            ],
        ),
    ]
