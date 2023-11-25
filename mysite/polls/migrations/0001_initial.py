# Generated by Django 4.2.7 on 2023-11-21 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('car_id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cars',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.IntegerField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=11)),
                ('client_email', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'client',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClientCommentCourier',
            fields=[
                ('comment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('comment', models.CharField(blank=True, max_length=128, null=True)),
                ('service_rating', models.FloatField(blank=True, null=True)),
                ('datetime_comment', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'client_comment_courier',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClientCommentDevices',
            fields=[
                ('comment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('comment_text', models.CharField(blank=True, max_length=128, null=True)),
                ('item_rating', models.FloatField()),
                ('datetime_comment', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'client_comment_devices',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClientCommentMaster',
            fields=[
                ('client_comment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('comment', models.CharField(blank=True, max_length=128, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'client_comment_master',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClientCommentsOperator',
            fields=[
                ('comment', models.CharField(blank=True, max_length=128, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('datetime_comment', models.DateField(blank=True, null=True)),
                ('comment_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'client_comments_operator',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Couriers',
            fields=[
                ('courier_id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('time_to_deliver', models.TimeField()),
                ('delivery_price', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
            ],
            options={
                'db_table': 'couriers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Indtracks',
            fields=[
                ('ind_track_id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('time_to_deliver', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'indtracks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Industries',
            fields=[
                ('industry_id', models.IntegerField(primary_key=True, serialize=False)),
                ('industry_address', models.CharField(max_length=20)),
                ('industry_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'industries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('invoice_id', models.IntegerField(primary_key=True, serialize=False)),
                ('price', models.FloatField(blank=True, null=True)),
                ('invoices_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'invoices',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=32)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'items',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Operators',
            fields=[
                ('operator_id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'operators',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_datetime', models.DateField()),
                ('id_order', models.IntegerField(primary_key=True, serialize=False)),
                ('order_sum', models.FloatField()),
                ('order_status', models.IntegerField()),
                ('services_type', models.IntegerField()),
                ('client_address', models.CharField(max_length=128)),
                ('item_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PcBuilder',
            fields=[
                ('build_id', models.IntegerField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pc_builder',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PcCleaner',
            fields=[
                ('cleaner_id', models.IntegerField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pc_cleaner',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PcMaster',
            fields=[
                ('id_master', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('rating', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pc_master',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PickUpPoint',
            fields=[
                ('id_point', models.IntegerField(primary_key=True, serialize=False)),
                ('open_hours', models.DateTimeField()),
                ('address_point', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'pick_up_point',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('provider_id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('item_name', models.CharField(blank=True, max_length=20, null=True)),
                ('params', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'providers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('service_id', models.IntegerField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('time', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'services',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('storage_id', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'storage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Techsupp',
            fields=[
                ('support_id', models.IntegerField(primary_key=True, serialize=False)),
                ('datetime_tech_supp', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'techsupp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('track_id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('time_to_deliver', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tracks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BuilderStatus',
            fields=[
                ('build', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='polls.pcbuilder')),
                ('status', models.IntegerField(blank=True, null=True)),
                ('time', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'builder_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CleanerStatus',
            fields=[
                ('status', models.IntegerField(blank=True, null=True)),
                ('time', models.DateField(blank=True, null=True)),
                ('cleaner', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='polls.pccleaner')),
            ],
            options={
                'db_table': 'cleaner_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Flash',
            fields=[
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='polls.items')),
                ('params', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.FloatField()),
                ('in_stock', models.CharField(blank=True, max_length=128, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('item_name', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'flash',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hdd',
            fields=[
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='polls.items')),
                ('params', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.FloatField()),
                ('in_stock', models.CharField(blank=True, max_length=128, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'hdd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IndtracksStatus',
            fields=[
                ('status', models.IntegerField(blank=True, null=True)),
                ('time', models.DateField(blank=True, null=True)),
                ('ind_track', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='polls.indtracks')),
            ],
            options={
                'db_table': 'indtracks_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Keyboards',
            fields=[
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='polls.items')),
                ('params', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.FloatField()),
                ('in_stock', models.CharField(blank=True, max_length=128, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'keyboards',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('client_login', models.CharField(max_length=32)),
                ('client_password', models.CharField(max_length=32)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='polls.client')),
            ],
            options={
                'db_table': 'login',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterStatus',
            fields=[
                ('status', models.IntegerField(blank=True, null=True)),
                ('time', models.DateField(blank=True, null=True)),
                ('id_master', models.OneToOneField(db_column='id_master', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='polls.pcmaster')),
            ],
            options={
                'db_table': 'master_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mice',
            fields=[
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='polls.items')),
                ('params', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.FloatField()),
                ('in_stock', models.CharField(blank=True, max_length=128, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'mice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Microphones',
            fields=[
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='polls.items')),
                ('params', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.FloatField()),
                ('in_stock', models.CharField(blank=True, max_length=128, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'microphones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ssd',
            fields=[
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='polls.items')),
                ('params', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.FloatField()),
                ('in_stock', models.CharField(blank=True, max_length=128, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'ssd',
                'managed': False,
            },
        ),
    ]