from django.db import models
import django_filters
from phonenumber_field.modelfields import PhoneNumberField

class BuilderStatus(models.Model):
    master_id = models.OneToOneField('PcBuilder', models.DO_NOTHING, db_column='master_id', primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        if self.status == 0:
            return f'{self.master_id} свободен'
        else:
            return f'{self.master_id} занят'
        
    class Meta:
        managed = False
        db_table = 'builder_status'


class Cars(models.Model):
    car_id = models.IntegerField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    courier = models.ForeignKey('Couriers', models.DO_NOTHING, blank=True, null=True)

    def __str__(self) -> str:
        if self.status == 0:
            return f'Машина номер {self.car_id} свободна'
        else:
            return f'Сборщик номер {self.car_id} занята {self.courier}'

    class Meta:
        managed = False
        db_table = 'cars'


class CleanerStatus(models.Model):
    status = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    master_id = models.OneToOneField('PcCleaner', models.DO_NOTHING, db_column='master_id', primary_key=True)

    def __str__(self) -> str:
        if self.status == 0:
            return f'{self.master_id} свободен'
        else:
            return f'{self.master_id} занят'

    class Meta:
        managed = False
        db_table = 'cleaner_status'

class ItemsForOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=255, null=False)
    id_order = models.ForeignKey('Orders', models.DO_NOTHING, db_column='id_order')

    def __str__(self) -> str:
        return f'{self.item_name} в {self.id_order}'

    class Meta:
        managed = False
        db_table = 'items_for_order'


class Client(models.Model):
    client_id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = PhoneNumberField(region="RU")
    client_email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=128)

    def __str__(self):
        return f"Клиент номер: {self.client_id}" + f" Имя: {self.full_name}" + f" Телефон: {self.phone_number}" + f" Почта: {self.client_email}"
        

    class Meta:
        managed = False
        db_table = 'client'


class ClientCommentCourier(models.Model):
    comment_id = models.IntegerField(primary_key=True)  # The composite primary key (comment_id, id_order) found, that is not supported. The first column is selected.
    comment = models.CharField(max_length=128, blank=True, null=True)
    service_rating = models.FloatField(blank=True, null=True)
    datetime_comment = models.DateTimeField(blank=True, null=True)
    id_order = models.ForeignKey('Orders', models.DO_NOTHING, db_column='id_order')
    
    def __str__(self):
        return f"Комментарий номер {self.comment_id} к курьеру доставлявший {self.id_order}"

    class Meta:
        managed = False
        db_table = 'client_comment_courier'
        unique_together = (('comment_id', 'id_order'),)


class ClientCommentDevices(models.Model):
    id_order = models.ForeignKey('Orders', models.DO_NOTHING, db_column='id_order')
    comment_id = models.IntegerField(primary_key=True)  # The composite primary key (comment_id, id_order) found, that is not supported. The first column is selected.
    comment_text = models.CharField(max_length=128, blank=True, null=True)
    item_rating = models.FloatField()
    datetime_comment = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Комментарий номер {self.comment_id} к предмету из {self.id_order}"

    class Meta:
        managed = False
        db_table = 'client_comment_devices'
        unique_together = (('comment_id', 'id_order'),)


class ClientCommentMaster(models.Model):
    client_comment_id = models.IntegerField(primary_key=True)  # The composite primary key (client_comment_id, id_order) found, that is not supported. The first column is selected.
    comment = models.CharField(max_length=128, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    id_order = models.ForeignKey('Orders', models.DO_NOTHING, db_column='id_order')

    def __str__(self):
     return f"Комментарий номер {self.comment_id} к мастеру из {self.id_order}"

    class Meta:
        managed = False
        db_table = 'client_comment_master'
        unique_together = (('client_comment_id', 'id_order'),)


# class ClientCommentsOperator(models.Model):
#     comment = models.CharField(max_length=128, blank=True, null=True)
#     rating = models.FloatField(blank=True, null=True)
#     datetime_comment = models.DateField(blank=True, null=True)
#     comment_id = models.IntegerField(primary_key=True)  # The composite primary key (comment_id, support_id) found, that is not supported. The first column is selected.
#     support = models.ForeignKey('Techsupp', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'client_comments_operator'
#         unique_together = (('comment_id', 'support'),)


class Couriers(models.Model):
    courier_id = models.IntegerField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    time_to_deliver = models.DateTimeField()
    id_order = models.ForeignKey('Orders', models.DO_NOTHING, db_column='id_order', blank=True, null=True)
    delivery_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    def __str__(self) -> str:
        if self.status == 0:
            return f"Курьер номер {self.courier_id} свободен"
        else:
            return f"Курьер номер {self.courier_id} доставляет {self.id_order}"

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
    type = models.CharField(max_length=20, blank=True, null=True)

    
    def __str__(self) -> str:
        return f"{self.name} Стоимость: {self.price} Рейтинг: {self.rating} Количество: {self.amount}"

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
    type = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.name} Стоимость: {self.price} Рейтинг: {self.rating} Количество: {self.amount}"

    class Meta:
        managed = False
        db_table = 'hdd'


class Indtracks(models.Model):
    ind_track_id = models.IntegerField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    time_to_deliver = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        if self.status == 0:
            return f"Производственный грузовик номер {self.ind_track_id} свободен"
        else:
            return f"Производственный грузовик номер {self.ind_track_id} занят"
        
    class Meta:
        managed = False
        db_table = 'indtracks'


class IndtracksStatus(models.Model):
    status = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    ind_track = models.OneToOneField(Indtracks, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'indtracks_status'


class Industries(models.Model):
    industry_id = models.IntegerField(primary_key=True)  # The composite primary key (industry_id, provider_id) found, that is not supported. The first column is selected.
    industry_address = models.CharField(max_length=20)
    industry_name = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f"Производство {self.industry_name} номер {self.industry_id}"
    
    class Meta:
        managed = False
        db_table = 'industries'



        

class Invoices(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    storage = models.ForeignKey('Storage', models.DO_NOTHING, blank=True, null=True)
    ind_track = models.ForeignKey(Indtracks, models.DO_NOTHING, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    industry = models.ForeignKey(Industries, models.DO_NOTHING, blank=True, null=True)
    invoices_date = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return f"Накладная номер {self.invoice_id}"

    class Meta:
        managed = False
        db_table = 'invoices'
        


class Items(models.Model):
    item_id = models.IntegerField(primary_key=True, auto_created=True)
    item_name = models.CharField(max_length=32)
    storage = models.ForeignKey('Storage', models.DO_NOTHING)
    type = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self) -> str:
        return f"Предмет {self.type} номер {self.item_id}"

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

    def __str__(self) -> str:
        return f"{self.name} Стоимость: {self.price} Рейтинг: {self.rating} Количество: {self.amount}"

    class Meta:
        managed = False
        db_table = 'keyboards'


class Login(models.Model):
    client_login = models.CharField(max_length=32)
    client_password = models.CharField(max_length=32)
    client = models.OneToOneField(Client, models.DO_NOTHING, primary_key=True)  # The composite primary key (client_id, client_login) found, that is not supported. The first column is selected.

    def __str__(self) -> str:
        return f"{self.client_login}"

    class Meta:
        managed = False
        db_table = 'login'
        unique_together = (('client', 'client_login'),)


class MasterStatus(models.Model):
    status = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    master_id = models.OneToOneField('PcMaster', models.DO_NOTHING, db_column='master_id', primary_key=True)

    def __str__(self) -> str:
        if self.status == 0:
            return f'{self.master_id} свободен'
        else:
            return f'{self.master_id} занят'

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

    def __str__(self) -> str:
        return f"{self.name} Стоимость: {self.price} Рейтинг: {self.rating} Количество: {self.amount}"

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

    def __str__(self) -> str:
        return f"{self.name} Стоимость: {self.price} Рейтинг: {self.rating} Количество: {self.amount}"

    class Meta:
        managed = False
        db_table = 'microphones'


# class Operators(models.Model):
#     support = models.ForeignKey('Techsupp', models.DO_NOTHING, blank=True, null=True)
#     operator_id = models.IntegerField(primary_key=True)
#     status = models.IntegerField(blank=True, null=True)
#     name = models.CharField(max_length=128, blank=True, null=True)
#     rating = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'operators'


class Orders(models.Model):
    order_datetime = models.DateTimeField()
    id_order = models.IntegerField(primary_key=True)
    order_sum = models.FloatField()
    order_status = models.IntegerField()
    client = models.ForeignKey(Client, models.DO_NOTHING)
    services_type = models.IntegerField(null=True, blank=True)
    client_address = models.CharField(max_length=128)
    delivery_type = models.IntegerField()
    master_id = models.IntegerField()
    pick_up_point_id = models.IntegerField()
    courier_id = models.IntegerField()

    def __str__(self) -> str:
        return f"Заказ номер {self.id_order}"

    class Meta:
        managed = False
        db_table = 'orders'


class PcBuilder(models.Model):
    master_id = models.IntegerField(primary_key=True)
    rating = models.FloatField(blank=True, null=True)
    service = models.ForeignKey('Services', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, null=False)
    time = models.DateTimeField(null=False)

    def __str__(self) -> str:
        return f"Сбощик номер {self.master_id}"

    class Meta:
        managed = False
        db_table = 'pc_builder'


class PcCleaner(models.Model):
    master_id = models.IntegerField(primary_key=True)
    rating = models.IntegerField(blank=True, null=True)
    service = models.ForeignKey('Services', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, null=False)
    time = models.DateTimeField(null=False)

    def __str__(self) -> str:
        return f"Чистильщик номер {self.master_id}"

    class Meta:
        managed = False
        db_table = 'pc_cleaner'


class PcMaster(models.Model):
    master_id = models.IntegerField(primary_key=True)
    rating = models.FloatField(blank=True, null=True)
    service = models.ForeignKey('Services', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, null=False)
    time = models.DateTimeField(null=False)

    def __str__(self) -> str:
        return f"Мастер номер {self.master_id}"

    class Meta:
        managed = False
        db_table = 'pc_master'


class PickUpPoint(models.Model):
    id_point = models.IntegerField(primary_key=True)
    open_hours = models.DateTimeField()
    address_point = models.CharField(max_length=100, blank=True, null=True)
    id_order = models.ForeignKey(Orders, models.DO_NOTHING, db_column='id_order', blank=True, null=True)

    def __str__(self) -> str:
        return f"Пункт выдачи номер {self.id_point}"

    class Meta:
        managed = False
        db_table = 'pick_up_point'


class Services(models.Model):
    services_type = models.IntegerField(primary_key=True)
    price = models.FloatField(blank=True, null=False)
    
    def __str__(self) -> str:
        d = {
            1: "Builder",
            2: "Master",
            3: "Cleaner",
        }
        return f"Service type is {d[self.services_type]}" 
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

    def __str__(self) -> str:
        return f"{self.name} Стоимость: {self.price} Рейтинг: {self.rating} Количество: {self.amount}"
    class Meta:
        managed = False
        db_table = 'ssd'


class Storage(models.Model):
    storage_id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self) -> str:
        return f"Склад номер {self.storage_id}"

    class Meta:
        managed = False
        db_table = 'storage'


class Techsupp(models.Model):
    support_id = models.IntegerField(primary_key=True)
    datetime_tech_supp = models.DateTimeField(blank=True, null=True)
    client = models.ForeignKey(Client, models.DO_NOTHING, blank=True, null=True)
    question = models.TextField()

    def __str__(self) -> str:
        return f"Вопрос номер {self.support_id}"

    class Meta:
        managed = False
        db_table = 'techsupp'


class Tracks(models.Model):
    track_id = models.IntegerField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    time_to_deliver = models.DateTimeField(blank=True, null=True)
    id_point = models.ForeignKey(PickUpPoint, models.DO_NOTHING, db_column='id_point', blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'tracks'

class InvoiceItems(models.Model):
    item_id = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=255)
    params = models.CharField(max_length=255)
    type = models.CharField(max_length=20)
    amount = models.IntegerField()
    invoice_id = models.ForeignKey(Invoices, models.DO_NOTHING, db_column='invoice_id')
    price = models.FloatField()

    def __str__(self) -> str:
        return f"{self.item_name} количеством {self.amount} из {self.invoice_id}"
    class Meta:
        managed = False
        db_table = 'invoice_items'

class OrderFilter(django_filters.FilterSet):
    id_order = django_filters.NumberFilter()

    order_sum = django_filters.NumberFilter()
    order_sum__gt = django_filters.NumberFilter(field_name='order_sum', lookup_expr='gt')
    order_sum__lt = django_filters.NumberFilter(field_name='order_sum', lookup_expr='lt')

    order_datetime = django_filters.DateTimeFilter(field_name='order_datetime')
    order_datetime__gt = django_filters.DateTimeFilter(field_name='order_datetime', lookup_expr='gt')
    order_datetime__lt = django_filters.DateTimeFilter(field_name='order_datetime', lookup_expr='lt')

    class Meta:
        model = Orders
        fields = ['id_order', 'order_sum', 'order_datetime']

class BuilderFilter(django_filters.FilterSet):
    master_num = django_filters.NumberFilter(field_name='master_id')
    master_name = django_filters.CharFilter(field_name='name', lookup_expr="icontains")

    rating_gt = django_filters.NumberFilter(field_name='rating', lookup_expr='gt')
    rating_lt = django_filters.NumberFilter(field_name='rating', lookup_expr='lt')

    builderstatus = django_filters.NumberFilter(field_name='builderstatus__status')
    service_type = django_filters.NumberFilter(field_name='service_id')

    class Meta:
        model = PcBuilder
        fields = ['master_id', 'rating']

class MasterFilter(django_filters.FilterSet):
    master_num = django_filters.NumberFilter(field_name='master_id')
    master_name = django_filters.CharFilter(field_name='name', lookup_expr="icontains")

    rating_gt = django_filters.NumberFilter(field_name='rating', lookup_expr='gt')
    rating_lt = django_filters.NumberFilter(field_name='rating', lookup_expr='lt')

    masterstatus = django_filters.NumberFilter(field_name='masterstatus__status')
    service_type = django_filters.NumberFilter(field_name='service_id')

    class Meta:
        model = PcMaster
        fields = ['master_id', 'rating']

class CleanerFilter(django_filters.FilterSet):
    master_num = django_filters.NumberFilter(field_name='master_id')
    master_name = django_filters.CharFilter(field_name='name', lookup_expr="icontains")

    rating_gt = django_filters.NumberFilter(field_name='rating', lookup_expr='gt')
    rating_lt = django_filters.NumberFilter(field_name='rating', lookup_expr='lt')

    cleanerstatus = django_filters.NumberFilter(field_name='cleanerstatus__status')
    service_type = django_filters.NumberFilter(field_name='service_id')

    class Meta:
        model = PcMaster
        fields = ['master_id', 'rating']


class ItemFilter(django_filters.FilterSet):

    item_name = django_filters.CharFilter(field_name='item_name', lookup_expr="icontains")

    # price_gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    # price_lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')


    class Meta:
        model = Items
        fields = ['item_name']