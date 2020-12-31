# Generated by Django 3.1.4 on 2020-12-31 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsnDetailModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asn_code', models.CharField(max_length=255, verbose_name='ASN Code')),
                ('asn_status', models.IntegerField(default=1, verbose_name='ASN Status')),
                ('supplier', models.CharField(max_length=255, verbose_name='ASN Supplier')),
                ('goods_code', models.CharField(max_length=255, verbose_name='Goods Code')),
                ('goods_qty', models.IntegerField(default=0, verbose_name='Goods QTY')),
                ('goods_actual_qty', models.IntegerField(default=0, verbose_name='Goods Actual QTY')),
                ('sorted_qty', models.IntegerField(default=0, verbose_name='Sorted QTY')),
                ('goods_shortage_qty', models.IntegerField(default=0, verbose_name='Goods Shortage QTY')),
                ('goods_more_qty', models.IntegerField(default=0, verbose_name='Goods More QTY')),
                ('goods_damage_qty', models.IntegerField(default=0, verbose_name='Goods damage QTY')),
                ('goods_weight', models.FloatField(default=0, verbose_name='Goods Weight')),
                ('goods_volume', models.FloatField(default=0, verbose_name='Goods Volume')),
                ('creater', models.CharField(max_length=11, verbose_name='Who Created')),
                ('openid', models.CharField(max_length=255, verbose_name='Openid')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Delete Label')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time')),
            ],
            options={
                'verbose_name': 'data id',
                'verbose_name_plural': 'data id',
                'db_table': 'asndetail',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='AsnListModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asn_code', models.CharField(max_length=255, verbose_name='ASN Code')),
                ('asn_status', models.IntegerField(default=1, verbose_name='ASN Status')),
                ('total_weight', models.FloatField(default=0, verbose_name='Total Weight')),
                ('total_volume', models.FloatField(default=0, verbose_name='Total Volume')),
                ('supplier', models.CharField(max_length=255, verbose_name='ASN Supplier')),
                ('creater', models.CharField(max_length=255, verbose_name='Who Created')),
                ('openid', models.CharField(max_length=255, verbose_name='Openid')),
                ('transportation_fee', models.JSONField(default=dict, verbose_name='Transportation Fee')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Delete Label')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time')),
            ],
            options={
                'verbose_name': 'data id',
                'verbose_name_plural': 'data id',
                'db_table': 'asnlist',
                'ordering': ['-id'],
            },
        ),
    ]
