from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django import forms
from django.forms import formset_factory
import django_filters
import datetime as dt
from phonenumber_field.formfields import PhoneNumberField


from .models import (
    Client,
    Login,
    Items,
    Orders,
    Hdd,
    Ssd,
    Mice,
    Flash,
    Microphones,
    Keyboards,
    PcBuilder,
    PcCleaner,
    PcMaster,
    Services,
    CleanerStatus,
    BuilderStatus,
    MasterStatus,
    ItemsForOrder,
    ClientCommentMaster,
    ClientCommentDevices,
    OrderFilter,
    BuilderFilter,
    MasterFilter,
    CleanerFilter,
    ItemFilter,
    PickUpPoint,
    Techsupp,
    Couriers,
    ClientCommentCourier,
)

item_types = {
    "HDD": Hdd,
    "SSD": Ssd,
    "Mouse": Mice,
    "Microphones": Microphones,
    "Flash": Flash,
    "Keyboard": Keyboards,
}


def check_cookie(request):
    try:
        client_login = request.COOKIES.get("cookie_login")
        client_password = request.COOKIES.get("cookie_password")
        return True
    except:
        return False


def all_clients(request):
    client_list = Client.objects.raw("SELECT * FROM Client")
    template = loader.get_template("html/all_clients.html")
    context = {
        "client_list": client_list,
    }
    return HttpResponse(template.render(context, request))


class register_form(forms.Form):
    full_name = forms.CharField(required=True)
    phone = PhoneNumberField(region="RU")
    email = forms.EmailField(required=True)
    login = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    password_repeat = forms.CharField(required=True, widget=forms.PasswordInput())
    address = forms.CharField(required=True)

    def get_name(self):
        data = self.cleaned_data["full_name"]
        return data


def register_client(request):
    if request.method == "POST":
        form = register_form(request.POST)
        template = loader.get_template("html/client_register.html")

        if form.is_valid():
            logins = Login.objects.all()
            for log in logins:
                if form.cleaned_data["login"] == log.client_login:
                    context = {"register_form": form, "error": "Логин занят"}
                    return HttpResponse(template.render(context, request))

            if form.cleaned_data["password"] != form.cleaned_data["password_repeat"]:
                context = {"register_form": form, "error": "Пароли не совпадают"}
                return HttpResponse(template.render(context, request))
            try:
                max_id = Client.objects.order_by("-client_id")[0].client_id
            except:
                max_id = 0
            client_id = max_id + 1
            full_name = form.cleaned_data["full_name"]
            phone_number = form.cleaned_data["phone"]
            
            client_email = form.cleaned_data["email"]
            address = form.cleaned_data["address"]

            client = Client(
                client_id=client_id,
                full_name=full_name,
                phone_number=phone_number,
                client_email=client_email,
                address=address,
            )
            client.save()

            client_login = form.cleaned_data["login"]
            client_password = form.cleaned_data["password"]

            login = Login(
                client_login=client_login,
                client_password=client_password,
                client_id=client_id,
            )
            login.save()

            response = HttpResponseRedirect("../login/")
            return response

    form = register_form()
    template = loader.get_template("html/client_register.html")
    context = {
        "register_form": form,
        "Message": "Введите корректный номер телефона (например, 8 (301) 123-45-67) или номер с префиксом международной связи."
    }
    return HttpResponse(template.render(context, request))


class login_form(forms.Form):
    login = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())


def login(request):
    try:
        login = Login.objects.get(
            client_login=request.COOKIES.get("cookie_login")
        ).client_login
        password = Login.objects.get(
            client_password=request.COOKIES.get("cookie_password")
        ).client_password
        response = HttpResponseRedirect("../profile/")
        return response
    except:
        if request.method == "POST":
            form = login_form(request.POST)
            if form.is_valid():
                try:
                    logins = Login.objects.get(client_login=form.cleaned_data["login"])
                except:
                    template = loader.get_template("html/login.html")
                    context = {"login_form": form, "error": f"Неверный логин"}
                    return HttpResponse(template.render(context, request))

                if logins.client_password == form.cleaned_data["password"]:
                    response = HttpResponseRedirect("../profile/")
                    response.set_cookie("cookie_login", logins.client_login)
                    response.set_cookie("cookie_password", logins.client_password)
                    return response

                template = loader.get_template("html/login.html")
                context = {"login_form": form, "error": f"Неверный пароль"}
                return HttpResponse(template.render(context, request))

        template = loader.get_template("html/login.html")
        context = {"login_form": login_form()}
        return HttpResponse(template.render(context, request))


class change_password_form(forms.Form):
    login = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    new_password = forms.CharField(required=True, widget=forms.PasswordInput())
    repeat_new_password = forms.CharField(required=True, widget=forms.PasswordInput())


def change_password(request):
    if request.method == "POST":
        form = change_password_form(request.POST)
        if form.is_valid():
            try:
                logins = Login.objects.get(client_login=form.cleaned_data["login"])
            except:
                template = loader.get_template("html/change_password.html")
                context = {"change_password_form": form, "error": f"Неверный логин"}
                return HttpResponse(template.render(context, request))

            if logins.client_password == form.cleaned_data["password"]:
                if (
                    form.cleaned_data["new_password"]
                    != form.cleaned_data["repeat_new_password"]
                ):
                    context = {
                        "change_password_form": change_password_form(),
                        "error": "Пароли не совпадают",
                    }
                    template = loader.get_template("html/change_password.html")
                    return HttpResponse(template.render(context, request))

                logins.client_password = form.cleaned_data["new_password"]
                logins.save()
                template = loader.get_template("html/change_password.html")
                context = {
                    "client": Client.objects.get(client_id=logins.client_id),
                    "status": "Пароль изменен",
                    "change_password_form": change_password_form()
                }
                return HttpResponse(template.render(context, request))

            template = loader.get_template("html/change_password.html")
            context = {"change_password_form": change_password_form(), "error": f"Неверный пароль"}
            return HttpResponse(template.render(context, request))

    template = loader.get_template("html/change_password.html")
    context = {"change_password_form": change_password_form()}
    return HttpResponse(template.render(context, request))


class create_order_form(forms.Form):
    choices = ()
    for type in item_types:
        for item_name in item_types[type].objects.all():
            choices = (*choices, (item_name.name, item_name))

    choices_pick_up = ()
    for pick_name in PickUpPoint.objects.all():
        choices_pick_up = (*choices_pick_up, (pick_name.address_point, pick_name.address_point))

    items = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices = choices, required=True)
    delivery_type_choices = ((1, "Курьером"), (2, "В пункте выдачи заказа"))
    delivery_type = forms.ChoiceField(choices=delivery_type_choices, required=True)
    pick_up_points = forms.ChoiceField(widget=forms.RadioSelect,
                                        choices = choices_pick_up,
                                        required=False
                                    )


def create_order(request):
    item_write = []

    item_f = ItemFilter(request.GET, queryset=Items.objects.all())

    for type in item_types:
        for item_name in item_types[type].objects.all():
            item_write.append(item_name)

    if request.method == "POST":
        form = create_order_form(request.POST)
        if form.is_valid() and form.cleaned_data["items"]:
            try:
                client_id = Login.objects.get(
                    client_login=request.COOKIES.get("cookie_login")
                ).client_id
                client_address = Client.objects.get(client_id=client_id).address
            except:
                response = HttpResponseRedirect("../login/")
                return response

            status = "OK"
            print(form.cleaned_data["pick_up_points"])
            if form.cleaned_data["delivery_type"] == '1' and form.cleaned_data["pick_up_points"]:
                status = "Нельзя добавить заказ с курьером и адресом пункта выдачи заказов"
                template = loader.get_template("html/create_order.html")  
                context = {"create_order":  create_order_form(), 'filter': item_f, "status": status}
                return HttpResponse(template.render(context, request))
            
            try:
                max_id = Orders.objects.order_by("-id_order")[0].id_order
            except:
                max_id = 0
            if form.cleaned_data["delivery_type"] == '2':
                pick_point = PickUpPoint.objects.get(address_point=form.cleaned_data["pick_up_points"])
            else: pick_point = None

            order = Orders(
                order_datetime=dt.datetime.utcnow(),
                id_order=max_id + 1,
                order_sum=0,
                order_status=0,  # 0 - обрабатывается, 1 - доставлеяется, 2 - доставлен
                client_id=client_id,
                client_address=client_address,
                delivery_type=form.cleaned_data["delivery_type"],
                pick_up_point_id=pick_point.id_point if pick_point else None,
                courier_id=None
            )
            order.save()
            
            for it in form.cleaned_data["items"]:
                items = Items.objects.get(item_name=it)
                item = item_types[items.type].objects.get(name=it)
                if item.amount != 0:
                    try:
                        max_id = ItemsForOrder.objects.order_by("-id")[0].id
                    except:
                        max_id = 0
                        
                    item_for_order = ItemsForOrder(
                        id=max_id + 1,
                        item_name=it,
                        id_order = order
                    )
                    item.amount -= 1
                    item.save()

                    order.order_sum += item.price
                    order.save()
                    item_for_order.save()
            template = loader.get_template("html/create_order.html")  
            context = {"create_order":  create_order_form(), "id": order.id_order, 'filter': item_f, "status": status}
            return HttpResponse(template.render(context, request))
    template = loader.get_template("html/create_order.html")
    context = {"create_order": create_order_form(), 'filter': item_f}  # "items": item_write,
    return HttpResponse(template.render(context, request))

def logout(request):
    logged = False
    response = HttpResponseRedirect("../login/")
    response.delete_cookie("cookie_login")
    response.delete_cookie("cookie_password")
    return response


def profile(request):
    try:
        client_login = request.COOKIES.get("cookie_login")
    except:
        response = HttpResponseRedirect("../login/")
        return response

    try:
        logins = Login.objects.get(client_login=client_login)
    except:
        response = HttpResponseRedirect("../login/")
        return response
    

    template = loader.get_template("html/profile.html")
    context = {
        "client": Client.objects.get(client_id=logins.client_id),
    }
    response = HttpResponse(template.render(context, request))
    response.set_cookie("cookie_login", logins.client_login)
    response.set_cookie("cookie_password", logins.client_password)
    return response


class make_orders_services_form(forms.Form):
    # service_type_choices = ((1, "builder"), (2, "cleaner"), (3, "master"))
    #services_type = forms.ChoiceField(choices=service_type_choices, required=True)
    masters_id = forms.IntegerField(required=True)


master_types = {"1": PcBuilder, "2": PcMaster, "3": PcCleaner}

master_status_type = {
    "1": BuilderStatus,
    "2": MasterStatus,
    "3": CleanerStatus,
}


def make_orders_service(request):
    
    builderFilter = BuilderFilter(request.GET, queryset=PcBuilder.objects.all())
    masterFilter = MasterFilter(request.GET, queryset=PcMaster.objects.all())
    cleanerFilter = CleanerFilter(request.GET, queryset=PcCleaner.objects.all())

    service_type = str(request.GET.get("service_type"))

    if request.method == "POST":
        builderFilter = BuilderFilter(request.GET, queryset=PcBuilder.objects.all())
        masterFilter = MasterFilter(request.GET, queryset=PcMaster.objects.all())
        cleanerFilter = CleanerFilter(request.GET, queryset=PcCleaner.objects.all())
        form = make_orders_services_form(request.POST)
        if form.is_valid():
            services = Services.objects.get(
                services_type=service_type
            )
            master = master_types[str(services.services_type)].objects.get(
                master_id=form.cleaned_data["masters_id"]
            )
            master_status = master_status_type[str(services.services_type)].objects.get(
                master_id=form.cleaned_data["masters_id"]
            )
            if master_status.status != 1:
                try:
                    client_id = Login.objects.get(
                        client_login=request.COOKIES.get("cookie_login")
                    ).client_id
                    client_address = Client.objects.get(client_id=client_id).address
                except:
                    raise ValueError(f"No cookies")

                try:
                    max_id = Orders.objects.order_by("-id_order")[0].id_order
                except:
                    max_id = 0

                order = Orders(
                    order_datetime=dt.datetime.utcnow(),
                    id_order=max_id + 1,
                    order_sum=services.price,
                    order_status=0,  # 0 - обрабатывается, 1 - доставлеяется, 2 - доставлен
                    client_id=client_id,
                    client_address=client_address,
                    delivery_type=None,
                    services_type=service_type,
                    master_id=master.master_id,
                )
                order.save()

                master_status.status = 1
                master_status.time = dt.datetime.utcnow()
                master_status.save()

                template = loader.get_template("html/make_order_service.html")
                context = {
                    "make_orders_services_form": make_orders_services_form(),
                    "master": master,
                    "master_type": service_type,
                    "builderFilter": builderFilter,
                    "masterFilter": masterFilter,
                    "cleanerFilter": cleanerFilter
                }
                return HttpResponse(template.render(context, request))

    template = loader.get_template("html/make_order_service.html")
    context = {
        "make_orders_services_form": make_orders_services_form(),
        "master_type": service_type,
        "builderFilter": builderFilter,
        "masterFilter": masterFilter,
        "cleanerFilter": cleanerFilter
    }
    return HttpResponse(template.render(context, request))




def my_orders(request):
    try:
        client_login = request.COOKIES.get("cookie_login")
    except:
        response = HttpResponseRedirect("../login/")
        return response

    client = Client.objects.get(
        client_id=Login.objects.get(client_login=client_login).client_id
    )

    f = OrderFilter(request.GET, queryset=Orders.objects.filter(client_id=client.client_id))

    item_orders = []
    service_orders = []
    items_for_order = {}
    for order in Orders.objects.filter(client_id=client.client_id):
        if order.client_id == client.client_id:
            if order.master_id == None:
                item_orders.append(order)
            else:
                service_orders.append(order)

    template = loader.get_template("html/my_orders.html")
    context = {"item_orders": item_orders, "service_orders": service_orders, 'filter': f}
    return HttpResponse(template.render(context, request)) # {'filter': f}


def get_order(request):
    
    id_order = request.GET.get('id_order')
    try:
        client_login = request.COOKIES.get("cookie_login")
    except:
        response = HttpResponseRedirect("../login/")
        return response

    try:
        order = Orders.objects.get(id_order=id_order)
    except:
        response = HttpResponseRedirect("../get_order")
        return response
    
    its = []
    itemss = ItemsForOrder.objects.all()
    for it in itemss:
        if it.id_order == order:
            i = Items.objects.get(item_name=it.item_name)
            ii = item_types[i.type].objects.get(name=it.item_name)
            its.append(ii)
    template = loader.get_template("html/get_order.html")
    if order.pick_up_point_id:
        pick_point = PickUpPoint.objects.get(id_point=order.pick_up_point_id).address_point
        courier = None
    else: 
        pick_point = None
        courier = Couriers.objects.get(courier_id=order.courier_id).courier_id

    context = {"order": order, "items": its, "pick_point": pick_point, "courier":courier}
    return HttpResponse(template.render(context, request))



def delete_order(request):
    try:
        client_login = request.COOKIES.get("cookie_login")
    except:
        response = HttpResponseRedirect("../login/")
        return response
    
    id_order = request.GET.get('id_order')
    
    try:
        client_login = request.COOKIES.get("cookie_login")
    except:
        response = HttpResponseRedirect("../login/")
        return response

    client = Client.objects.get(
        client_id=Login.objects.get(client_login=client_login).client_id
    )
    try:
        order = Orders.objects.get(id_order=id_order)
        order.delete()
    except:
        response = HttpResponseRedirect("../my_orders")
        return response

    response = HttpResponseRedirect("../my_orders")
    return response


class comment_master_form(forms.Form):
    marks = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    rating = forms.ChoiceField(choices=marks, required=True)
    comment = forms.CharField(widget=forms.Textarea)


def leave_master_comment(request):
    try:
        client_login = request.COOKIES.get("cookie_login")
    except:
        response = HttpResponseRedirect("../login/")
        return response

    id_order = request.GET.get('id_order')
    print(id_order)

    if request.method == "POST":
        form = comment_master_form(request.POST)
        if form.is_valid():

            order = Orders.objects.get(id_order=id_order)
            type = order.services_type
            master = master_types[str(type)].objects.get(master_id=order.master_id)

            master.rating = (master.rating + int(form.cleaned_data["rating"]))/2
            master.save()

            try:
                max_id = ClientCommentMaster.objects.order_by("-client_comment_id")[0].client_comment_id
            except:
                max_id = 0

            com = ClientCommentMaster(
                client_comment_id = max_id + 1,
                rating = form.cleaned_data["rating"],
                comment = form.cleaned_data["comment"],
                id_order = order
            )
            com.save()

            template = loader.get_template("html/leave_master_comment.html")
            context = {'done': "Комментарий оставлен"}
            return HttpResponse(template.render(context, request))  

    template = loader.get_template("html/leave_master_comment.html")
    context = {"comment_master_form": comment_master_form()}
    return HttpResponse(template.render(context, request))  

class comment_item_form(forms.Form):
    marks = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    rating = forms.ChoiceField(choices=marks, required=True)
    comment = forms.CharField(widget=forms.Textarea)


def leave_item_comment(request):
    try:
        client_login = request.COOKIES.get("cookie_login")
    except:
        response = HttpResponseRedirect("../login/")
        return response
    
    item_name = request.GET.get('item_name')
    id_order = request.GET.get('id_order')

    items = Items.objects.get(item_name=item_name)
    item = item_types[items.type].objects.get(name=item_name)

    if request.method == "POST":
        form = comment_item_form(request.POST)
        if form.is_valid():

            item.rating = (item.rating + int(form.cleaned_data["rating"]))/2
            item.save()

            try:
                max_id = ClientCommentDevices.objects.order_by("-client_comment_id")[0].client_comment_id
            except:
                max_id = 0

            com = ClientCommentDevices(
                comment_id = max_id + 1,
                item_rating = form.cleaned_data["rating"],
                comment_text = form.cleaned_data["comment"],
                datetime_comment = dt.datetime.utcnow(),
                id_order = Orders.objects.get(id_order=id_order)
            )
            com.save()

            template = loader.get_template("html/leave_item_comment.html")
            context = {'done': "Комментарий оставлен"}
            return HttpResponse(template.render(context, request))  


    template = loader.get_template("html/leave_item_comment.html")
    context = {"comment_item_form": comment_item_form(), "item": item}
    return HttpResponse(template.render(context, request))  

class tech_supp_form(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    ...

def tech_supp(request):
    try:
        client_login = request.COOKIES.get("cookie_login")
    except:
        response = HttpResponseRedirect("../login/")
        return response
    
    try:
        client = Client.objects.get(client_id=Login.objects.get(client_login=client_login).client_id)
    except:
        response = HttpResponseRedirect("../login/")
        return response
    
    history = Techsupp.objects.filter(client_id=client.client_id)

    if request.method == "POST":
        form = tech_supp_form(request.POST)
        if form.is_valid():
            status = "Ожидайте ответа на почте"

            try:
                max_id = Techsupp.objects.order_by("-support_id")[0].support_id
            except:
                max_id = 0

            try:
                tech_supp = Techsupp(
                    support_id=max_id+1,
                    datetime_tech_supp=dt.datetime.utcnow(),
                    client_id=client.client_id,
                    question=form.cleaned_data["text"]
                )
                tech_supp.save()
            except:
                status = "Что-то пошло не так ;)"

            form = None
            template = loader.get_template("html/tech_supp.html")  
            context = {"tech_supp_form":  tech_supp_form(), "status": status, "history": history}
            return HttpResponse(template.render(context, request))
    form = None
    template = loader.get_template("html/tech_supp.html")  
    context = {"tech_supp_form":  tech_supp_form(), "history": history}
    return HttpResponse(template.render(context, request))
            
def show_question(request):
    sup_id = request.GET.get("support_id")
    question = Techsupp.objects.get(support_id=sup_id).question
    template = loader.get_template("html/question.html")  
    context = {"question": question}
    return HttpResponse(template.render(context, request))


class leave_comment_courier_form(forms.Form):
    marks = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    rating = forms.ChoiceField(choices=marks, required=True)
    text = forms.CharField(widget=forms.Textarea)


def leave_comment_courier(request):
    try:
        client_login = request.COOKIES.get("cookie_login")
    except:
        response = HttpResponseRedirect("../login/")
        return response

    id_order = request.GET.get('id_order')
    order = Orders.objects.get(id_order=id_order)
    
    form = None
    if request.method == "POST":
        form = leave_comment_courier_form(request.POST)
        if form.is_valid():
            status = "OK"

            # try:
            #order = Orders.objects.get(id_order=id_order)
            # except: 
            #     status = "Что-то пошло не так" 


            courier = Couriers.objects.get(courier_id=order.courier_id)
            courier.rating = (courier.rating + int(form.cleaned_data["rating"]))/2
           
            courier.save()

            try:
                max_id = ClientCommentCourier.objects.order_by("-comment_id")[0].comment_id
            except:
                max_id = 0

            com = ClientCommentCourier(
                comment_id = max_id + 1,
                service_rating = form.cleaned_data["rating"],
                comment = form.cleaned_data["text"],
                datetime_comment = dt.datetime.utcnow(),
                id_order = order
            )
            com.save()
            form = None
            template = loader.get_template("html/leave_comment_courier.html")
            context = {'done': "Комментарий оставлен", "status": status, "leave_comment_courier": leave_comment_courier_form()}
            return HttpResponse(template.render(context, request))  
    form = None
    template = loader.get_template("html/leave_comment_courier.html")
    context = {"leave_comment_courier": leave_comment_courier_form()}
    return HttpResponse(template.render(context, request))  