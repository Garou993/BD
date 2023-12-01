from django.db import models


class BuilderStatus(models.Model):
    master_id = models.OneToOneField('PcBuilder', models.DO_NOTHING, db_column='master_id', primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'builder_status'


class Cars(models.Model):
    car_id = models.IntegerField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    courier = models.ForeignKey('Couriers', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars'


class CleanerStatus(models.Model):
    status = models.IntegerField(blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    master_id = models.OneToOneField('PcCleaner', models.DO_NOTHING, db_column='master_id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'cleaner_status'

class ItemsForOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=255, null=False)
    id_order = models.ForeignKey('Orders', models.DO_NOTHING, db_column='id_order')

    class Meta:
        managed = False
        db_table = 'items_for_order'


class Client(models.Model):
    client_id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=11)
    client_email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=128)

    def __str__(self):
        return f"client id: {self.client_id}" + f" full name: {self.full_name}" + f" phone number: {self.phone_number}" + f"client email: {self.client_email}"
        

    class Meta:
        managed = False
        db_table = 'client'


class ClientCommentCourier(models.Model):
    comment_id = models.IntegerField(primary_key=True)  # The composite primary key (comment_id, id_order) found, that is not supported. The first column is selected.
    comment = models.CharField(max_length=128, blank=True, null=True)
    service_rating = models.FloatField(blank=True, null=True)
    datetime_comment = models.DateField(blank=True, null=True)
    id_order = models.ForeignKey('Orders', models.DO_NOTHING, db_column='id_order')
    

    class Meta:
        managed = False
        db_table = 'client_comment_courier'
        unique_together = (('comment_id', 'id_order'),)


class ClientCommentDevices(models.Model):
    id_order = models.ForeignKey('Orders', models.DO_NOTHING, db_column='id_order')
    comment_id = models.IntegerField(primary_key=True)  # The composite primary key (comment_id, id_order) found, that is not supported. The first column is selected.
    comment_text = models.CharField(max_length=128, blank=True, null=True)
    item_rating = models.FloatField()
    datetime_comment = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_comment_devices'
        unique_together = (('comment_id', 'id_order'),)


class ClientCommentMaster(models.Model):
    client_comment_id = models.IntegerField(primary_key=True)  # The composite primary key (client_comment_id, id_order) found, that is not supported. The first column is selected.
    comment = models.CharField(max_length=128, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    id_order = models.ForeignKey('Orders', models.DO_NOTHING, db_column='id_order')

    class Meta:
        managed = False
        db_table = 'client_comment_master'
        unique_together = (('client_comment_id', 'id_order'),)


class ClientCommentsOperator(models.Model):
    comment = models.CharField(max_length=128, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    datetime_comment = models.DateField(blank=True, null=True)
    comment_id = models.IntegerField(primary_key=True)  # The composite primary key (comment_id, support_id) found, that is not supported. The first column is selected.
    support = models.ForeignKey('Techsupp', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'client_comments_operator'
        unique_together = (('comment_id', 'support'),)


class Couriers(models.Model):
    courier_id = models.IntegerField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    time_to_deliver = models.TimeField()
    id_order = models.ForeignKey('Orders', models.DO_NOTHING, db_column='id_order', blank=True, null=True)
    delivery_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'couriers'


class Flash(models.Model):
    item = models.OneToOneField('Items', models.DO_NOTHING, primary_key=True)
    params = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField()
    rating = models.FloatField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    
    def __str__(self) -> str:
        return f"{self.name} Cost:{self.price} Rating: {self.rating} Amount: {self.amount}"

    class Meta:
        managed = False
        db_table = 'flash'


class Hdd(models.Model):
    item = models.OneToOneField('Items', models.DO_NOTHING, primary_key=True)
    params = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField()
    rating = models.FloatField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.name} Cost:{self.price} Rating: {self.rating} Amount: {self.amount}"

    class Meta:
        managed = False
        db_table = 'hdd'


class Indtracks(models.Model):
    ind_track_id = models.IntegerField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    time_to_deliver = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indtracks'


class IndtracksStatus(models.Model):
    status = models.IntegerField(blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    ind_track = models.OneToOneField(Indtracks, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'indtracks_status'


class Industries(models.Model):
    industry_id = models.IntegerField(primary_key=True)  # The composite primary key (industry_id, provider_id) found, that is not supported. The first column is selected.
    industry_address = models.CharField(max_length=20)
    provider = models.ForeignKey('Providers', models.DO_NOTHING, unique=True)
    industry_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'industries'
        unique_together = (('industry_id', 'provider'),)


class Invoices(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    storage = models.ForeignKey('Storage', models.DO_NOTHING, blank=True, null=True)
    ind_track = models.ForeignKey(Indtracks, models.DO_NOTHING, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    industry = models.ForeignKey(Industries, models.DO_NOTHING, blank=True, null=True)
    provider = models.ForeignKey(Industries, models.DO_NOTHING, unique=True, to_field='provider_id', related_name='invoices_provider_set', blank=True, null=True)
    invoices_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoices'
        


class Items(models.Model):
    item_id = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=32)
    storage = models.ForeignKey('Storage', models.DO_NOTHING)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'


class Keyboards(models.Model):
    item = models.OneToOneField(Items, models.DO_NOTHING, primary_key=True)
    params = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField()
    rating = models.FloatField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keyboards'


class Login(models.Model):
    client_login = models.CharField(max_length=32)
    client_password = models.CharField(max_length=32)
    client = models.OneToOneField(Client, models.DO_NOTHING, primary_key=True)  # The composite primary key (client_id, client_login) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'login'
        unique_together = (('client', 'client_login'),)


class MasterStatus(models.Model):
    status = models.IntegerField(blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    master_id = models.OneToOneField('PcMaster', models.DO_NOTHING, db_column='master_id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'master_status'


class Mice(models.Model):
    item = models.OneToOneField(Items, models.DO_NOTHING, primary_key=True)
    params = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField()
    rating = models.FloatField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mice'


class Microphones(models.Model):
    item = models.OneToOneField(Items, models.DO_NOTHING, primary_key=True)
    params = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField()
    rating = models.FloatField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'microphones'


class Operators(models.Model):
    support = models.ForeignKey('Techsupp', models.DO_NOTHING, blank=True, null=True)
    operator_id = models.IntegerField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operators'


class Orders(models.Model):
    order_datetime = models.DateField()
    id_order = models.IntegerField(primary_key=True)
    order_sum = models.FloatField()
    order_status = models.IntegerField()
    client = models.ForeignKey(Client, models.DO_NOTHING)
    services_type = models.IntegerField()
    client_address = models.CharField(max_length=128)
    delivery_type = models.IntegerField()
    master_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orders'


class PcBuilder(models.Model):
    master_id = models.IntegerField(primary_key=True)
    rating = models.FloatField(blank=True, null=True)
    service = models.ForeignKey('Services', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, null=False)
    time = models.DateTimeField(null=False)

    class Meta:
        managed = False
        db_table = 'pc_builder'


class PcCleaner(models.Model):
    master_id = models.IntegerField(primary_key=True)
    rating = models.IntegerField(blank=True, null=True)
    service = models.ForeignKey('Services', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, null=False)
    time = models.DateTimeField(null=False)

    class Meta:
        managed = False
        db_table = 'pc_cleaner'


class PcMaster(models.Model):
    master_id = models.CharField(primary_key=True, max_length=128)
    rating = models.FloatField(blank=True, null=True)
    service = models.ForeignKey('Services', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, null=False)
    time = models.DateTimeField(null=False)

    class Meta:
        managed = False
        db_table = 'pc_master'


class PickUpPoint(models.Model):
    id_point = models.IntegerField(primary_key=True)
    open_hours = models.DateTimeField()
    address_point = models.CharField(max_length=100, blank=True, null=True)
    id_order = models.ForeignKey(Orders, models.DO_NOTHING, db_column='id_order', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pick_up_point'


class Providers(models.Model):
    provider_id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    item_name = models.CharField(max_length=20, blank=True, null=True)
    params = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'providers'


class Services(models.Model):
    services_type = models.IntegerField(primary_key=True)
    price = models.FloatField(blank=True, null=False)
    

    class Meta:
        managed = False
        db_table = 'services'


class Ssd(models.Model):
    item = models.OneToOneField(Items, models.DO_NOTHING, primary_key=True)
    params = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField()
    rating = models.FloatField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssd'


class Storage(models.Model):
    storage_id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage'


class Techsupp(models.Model):
    support_id = models.IntegerField(primary_key=True)
    datetime_tech_supp = models.DateField(blank=True, null=True)
    client = models.ForeignKey(Client, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'techsupp'


class Tracks(models.Model):
    track_id = models.IntegerField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    time_to_deliver = models.DateField(blank=True, null=True)
    id_point = models.ForeignKey(PickUpPoint, models.DO_NOTHING, db_column='id_point', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tracks'
