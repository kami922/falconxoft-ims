from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("",views.home,name='home'),
    path("signUp",views.register,name="register"),
    path("login",views.login,name='login'),
    path("createEquip",views.CreateEquipment,name="equipment"),
    path("editPW",views.change_password,name="editPW"),
    path('book', views.reserve_equipment, name='book'),
    path("history",views.reservationHistory,name='history'),
]
