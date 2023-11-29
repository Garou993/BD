from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django import forms
import datetime as dt


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
    phone = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    login = forms.CharField(required=True)
    password = forms.CharField(required=True)
    password_repeat = forms.CharField(required=True)
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
                    context = {"register_form": form, "error": "Login taken"}
                    return HttpResponse(template.render(context, request))

            if form.cleaned_data["password"] != form.cleaned_data["password_repeat"]:
                context = {"register_form": form, "error": "Passwords are not the same"}
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
    }
    return HttpResponse(template.render(context, request))


class login_form(forms.Form):
    login = forms.CharField(required=True)
    password = forms.CharField(required=True)


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
                    context = {"login_form": form, "error": f"wrong login"}
                    return HttpResponse(template.render(context, request))

                if logins.client_password == form.cleaned_data["password"]:
                    response = HttpResponseRedirect("../profile/")
                    response.set_cookie("cookie_login", logins.client_login)
                    response.set_cookie("cookie_password", logins.client_password)
                    return response

                template = loader.get_template("html/login.html")
                context = {"login_form": form, "error": f"wrong password"}
                return HttpResponse(template.render(context, request))

        template = loader.get_template("html/login.html")
        context = {"login_form": login_form()}
        return HttpResponse(template.render(context, request))


class change_password_form(forms.Form):
    login = forms.CharField(required=True)
    password = forms.CharField(required=True)
    new_password = forms.CharField(required=True)
    repeat_new_password = forms.CharField(required=True)


def change_password(request):
    if request.method == "POST":
        form = change_password_form(request.POST)
        if form.is_valid():
            try:
                logins = Login.objects.get(client_login=form.cleaned_data["login"])
            except:
                template = loader.get_template("html/change_password.html")
                context = {"change_password_form": form, "error": f"wrong login"}
                return HttpResponse(template.render(context, request))

            if logins.client_password == form.cleaned_data["password"]:
                if (
                    form.cleaned_data["new_password"]
                    != form.cleaned_data["repeat_new_password"]
                ):
                    context = {
                        "register_form": form,
                        "error": "Passwords are not the same",
                    }
                    return HttpResponse(template.render(context, request))

                logins.client_password = form.cleaned_data["new_password"]
                logins.save()
                template = loader.get_template("html/change_password.html")
                context = {
                    "client": Client.objects.get(client_id=logins.client_id),
                    "status": "password changed",
                }
                return HttpResponse(template.render(context, request))

            template = loader.get_template("html/change_password.html")
            context = {"change_password_form": form, "error": f"wrong password"}
            return HttpResponse(template.render(context, request))

    template = loader.get_template("html/change_password.html")
    context = {"change_password_form": change_password_form()}
    return HttpResponse(template.render(context, request))


class create_order_form(forms.Form):
    delivery_type_choices = ((1, "courier"), (2, "pick-up-point"))
    delivery_type = forms.ChoiceField(choices=delivery_type_choices, required=True)


def create_order(request):
    if request.method == "POST":
        form = create_order_form(request.POST)
        if form.is_valid():
            try:
                client_id = Login.objects.get(
                    client_login=request.COOKIES.get("cookie_login")
                ).client_id
                client_address = Client.objects.get(client_id=client_id).address
            except:
                response = HttpResponseRedirect("../login/")
                return response

            try:
                max_id = Orders.objects.order_by("-id_order")[0].id_order
            except:
                max_id = 0

            order = Orders(
                order_datetime=dt.datetime.utcnow(),
                id_order=max_id + 1,
                order_sum=0,
                order_status=0,  # 0 - обрабатывается, 1 - доставлеяется, 2 - доставлен
                client_id=client_id,
                client_address=client_address,
                delivery_type=form.cleaned_data["delivery_type"],
            )
            order.save()

            template = loader.get_template("html/create_order.html")
            context = {"create_order": form, "id": max_id}
            return HttpResponse(template.render(context, request))

    template = loader.get_template("html/create_order.html")
    context = {"create_order": create_order_form()}  # "items": item_write,
    return HttpResponse(template.render(context, request))


class add_to_order_from(forms.Form):
    order_id = forms.IntegerField(required=True)
    item_name = forms.CharField(max_length=255, required=True)


def add_to_order(request):
    item_write = []

    for type in item_types:
        for item_name in sorted(item_types[type].objects.all()):
            item_write.append(item_name)

    if request.method == "POST":
        form = add_to_order_from(request.POST)
        if form.is_valid():
            items = Items.objects.get(item_name=form.cleaned_data["item_name"])
            item = item_types[items.type].objects.get(
                name=form.cleaned_data["item_name"]
            )
            if item.amount != 0:
                try:
                    max_id = ItemsForOrder.objects.order_by("-id")[0].id
                except:
                    max_id = 0
                try:
                    order = Orders.objects.get(id_order=form.cleaned_data["order_id"])
                except:
                    response = HttpResponseRedirect("../add_to_order")
                    return response
                item_for_order = ItemsForOrder(
                    id=max_id + 1,
                    item_name=form.cleaned_data["item_name"],
                )
                item.amount -= 1
                item.save()

                order.order_sum += item.price
                item_for_order.order = order
                item_for_order.save()

                template = loader.get_template("html/add_to_order.html")
                context = {"items": item_write, "add_to_order": form, "item": item}
                return HttpResponse(template.render(context, request))
            response = HttpResponseRedirect("../add_to_order")
            return response

    template = loader.get_template("html/add_to_order.html")
    context = {
        "add_to_order": add_to_order_from(),
        "items": item_write,
    }  # "items": item_write,
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
    service_type_choices = ((1, "builder"), (2, "cleaner"), (3, "master"))
    services_type = forms.ChoiceField(choices=service_type_choices, required=True)
    master_id = forms.IntegerField(required=True)


master_types = {"1": PcBuilder, "2": PcMaster, "3": PcCleaner}

master_status_type = {
    "1": BuilderStatus,
    "2": MasterStatus,
    "3": CleanerStatus,
}


def make_orders_service(request):
    master_write = []

    for type in master_types:
        for master in sorted(master_types[type].objects.all()):
            print(master.master_id)
            if (
                master_status_type[type].objects.get(master_id=master.master_id).status
                == 0
            ):
                master_write.append(master)

    if request.method == "POST":
        form = make_orders_services_form(request.POST)
        if form.is_valid():
            services = Services.objects.get(
                services_type=form.cleaned_data["services_type"]
            )
            master = master_types[str(services.services_type)].objects.get(
                master_id=form.cleaned_data["master_id"]
            )
            master_status = master_status_type[str(services.services_type)].objects.get(
                master_id=form.cleaned_data["master_id"]
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
                    item_name=None,
                    delivery_type=None,
                    services_type=form.cleaned_data["services_type"],
                    master_id=master.master_id,
                )
                print(order)
                order.save()

                master_status.status = 1
                master_status.time = dt.datetime.utcnow()
                master_status.save()

                template = loader.get_template("html/make_order_service.html")
                context = {
                    "masters": master_write,
                    "make_orders_services_form": form,
                    "master": master,
                }
                return HttpResponse(template.render(context, request))

    template = loader.get_template("html/make_order_service.html")
    context = {
        "masters": master_write,
        "make_orders_services_form": make_orders_services_form(),
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

    item_orders = []
    service_orders = []
    items_for_order = {}
    for order in Orders.objects.all():
        if order.client_id == client.client_id:
            if order.master_id == None:
                item_orders.append(order)
            else:
                service_orders.append(order)

    template = loader.get_template("html/my_orders.html")
    context = {"item_orders": item_orders, "service_orders": service_orders}
    return HttpResponse(template.render(context, request))


class get_order_content_from(forms.Form):
    id_order = forms.IntegerField()


def get_order(request):
    if request.method == "POST":
        form = get_order_content_from(request.POST)
        if form.is_valid():
            try:
                client_login = request.COOKIES.get("cookie_login")
            except:
                response = HttpResponseRedirect("../login/")
                return response

            client = Client.objects.get(
                client_id=Login.objects.get(client_login=client_login).client_id
            )
            try:
                order = Orders.objects.get(id_order=form.cleaned_data["id_order"])
            except:
                response = HttpResponseRedirect("../get_order")
                return response
            template = loader.get_template("html/get_order.html")
            context = {"order": order}
            return HttpResponse(template.render(context, request))

    template = loader.get_template("html/get_order.html")
    context = {"get_order_content_from": get_order_content_from()}
    return HttpResponse(template.render(context, request))


class delete_order_form(forms.Form):
    id_order = forms.IntegerField()


def delete_order(request):
    if request.method == "POST":
        form = delete_order_form(request.POST)
        if form.is_valid():
            try:
                client_login = request.COOKIES.get("cookie_login")
            except:
                response = HttpResponseRedirect("../login/")
                return response

            client = Client.objects.get(
                client_id=Login.objects.get(client_login=client_login).client_id
            )
            try:
                order = Orders.objects.get(id_order=form.cleaned_data["id_order"])
                order.delete()
            except:
                response = HttpResponseRedirect("../delete_order")
                return response

            template = loader.get_template("html/delete_order.html")
            context = {
                "delete_order": form,
                "message": "Deleted",
            }
            return HttpResponse(template.render(context, request))

    template = loader.get_template("html/delete_order.html")
    context = {"delete_order_form": delete_order_form()}
    return HttpResponse(template.render(context, request))
