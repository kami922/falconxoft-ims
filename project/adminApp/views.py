# Create your views here.
from django.shortcuts import render,redirect
from .forms import UserForm,LoginForm,EquipmentForm
from django.contrib.auth.models import auth
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from core.models import Equipment,Reservation
from django.http import HttpResponse

#admin app views

# Create your views here.
@login_required(login_url='adlogin')
def home(request):
    return render(request,"adminApp/home.html")

@login_required(login_url='adlogin')
def ApproveUser(request):
    unApprovedUser = User.objects.filter(is_active = False)
    context = {"user":unApprovedUser}
    return render(request,"adminApp/approveUser.html",context)


@login_required(login_url='adlogin')
def CreateEquipment(request):
    form = EquipmentForm()
    if request.method == "POST":
        form = EquipmentForm(request.POST)
        if form.is_valid():
            equip = form.save(commit=False)
            equip.assigned_to = request.user
            equip.save()
            return redirect("home")
    context = {"eForm":form}
    return render(request,"adminApp/bookEquip.html",context)



@login_required(login_url='adlogin')
def report(request):
    reservations = Reservation.objects.all()
    report_data = []
    for reservation in reservations:
        report_data.append({
            'user':reservation.user.username,
            'equipment':reservation.equipmentId.deviceName,
            'reserved_from':reservation.reserved_from,
            'reserved_to':reservation.reserved_to,
        })
    context = {'report_data':report_data}
    return render(request,'adminApp/report.html',context)

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request,data = request.POST)
        if form.is_valid():
            email = request.POST.get("email")
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request,email=email,password=password,username=username)
            print(user)
            if user is not None:
                auth.login(request,user)
                return redirect("home2")
    context = {'logF':form}
    return render(request,"adminApp/login.html",context)    

def logout_view(request):
    logout(request)
    return HttpResponse("logout")


@login_required(login_url="adlogin")
def delete_users(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = User.objects.get(pk=user_id)  
        user.delete()
        messages.success(request, 'User deleted successfully.') 

    users = User.objects.all().order_by('username')  
    context = {'users': users}
    return render(request, 'adminApp/deleteUser.html', context)

@login_required(login_url="adlogin")
def cancelReservation(request):
    reservations = Reservation.objects.all()
    context = {"reservations":reservations}
    return render(request,'adminApp/delReservation.html',context)



def ViewEquip(request):
    equipments = Equipment.objects.all()
    context = {"equipments":equipments}
    return render(request,"adminApp/viewEquip.html",context)


def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            print(form)
            user = User.objects.create_user(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password1"],
                email = form.cleaned_data["email"],
                is_staff = True
            )
            user.save()
            return redirect("home")
    context = {"regForm":form}
    return render(request,"adminApp/signUp.html",context=context)

@login_required(login_url="adlogin")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('adlogin')
    else:
        form = PasswordChangeForm(request.user)

    context = {'form': form}
    return render(request, 'adminApp/change_password.html', context)

@login_required(login_url="adlogin")
def approve_users(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = User.objects.get(pk=user_id)
        if not user.is_active:
            user.is_active = True
            user.save()
    unapproved_users = User.objects.filter(is_active=False)
    context = {'unapproved_users': unapproved_users}
    return render(request, 'adminApp/approveUser.html', context)


