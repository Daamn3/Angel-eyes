from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect


# Create your views here.
from myapp.models import object_table, Complaints, blind, caretaker


def login_get(request):
    # print('login_get')
    return render(request,'login.html')

def login_post(request):
    username=request.POST['user']
    password=request.POST['pass']
    print(username,password)
    user= authenticate(request, username=username,password=password)
    if user is not None:
        # print('1st if')

        if user.groups.filter(name='Admin').exists():
            # print('2nd if')
            login(request,user)
            messages.success(request,'login successful!')
            return redirect('/myapp/index_get/')
        else:
            messages.error(request,'Invalid credentials!')
            # print('1st else')
            return redirect('/myapp/login_get/')
    else:
        messages.success(request, 'Invalid UserName or Password!')
        return redirect('/myapp/login_get/')
        # print('ttttttttttttttt')


def logout_all(request):
    logout(request)
    return redirect('/myapp/login_get/')


def index_get(request):
    a=blind.objects.all().count()
    b=caretaker.objects.all().count()
    return render(request,'index.html',{'cn':a,'bn':b})

def forgotpass_get(request):
    return render(request,'forgotpass.html')


def send_reply_get(request,id):
    request.session['id']=id
    return render(request,'send_reply.html')

def view_blindperson_get(request):
    a=blind.objects.all
    return render(request, 'view_blindperson.html',{'data':a})

def view_caretaker_get(request):
    data=caretaker.objects.all
    return render(request, 'view_caretaker.html',{'data':data})

def view_complaint_get(request):
    data=Complaints.objects.all
    return render(request, 'view_complaint.html',{'data':data})

def objects_manage_get(request):
    return render(request,'objects_manage.html')

def objects_manage_post(request):
    name=request.POST['name']
    image=request.FILES['image']
    details=request.POST['details']

    fs=FileSystemStorage()
    path=fs.save(image.name,image)

    a=object_table()
    a.Name=name
    a.details=details
    a.image=path
    a.save()
    messages.success(request,'successfully added')
    return redirect('/myapp/view_object_get/')

def view_object_get(request):
    data=object_table.objects.all()
    return render(request,'view_object.html',{'data':data})

def edit_objects_get(request,id):
    o=object_table.objects.get(id=id)
    request.session['id']=id
    return render(request,'edit_objects.html',{'data':o})

def edit_objects_post(request):
    name=request.POST['name']
    details = request.POST['details']
    o=object_table.objects.get(id=request.session['id'])
    o.Name=name
    o.details=details
    if 'image' in request.FILES:
        image = request.FILES['image']
        fs = FileSystemStorage()
        path = fs.save(image.name, image)
        o.image=path
    o.save()
    messages.success(request, 'successfully updated')
    return redirect('/myapp/view_object_get/')

def delete_object(request,id):
    o=object_table.objects.get(id=id)
    o.delete()
    messages.success(request, 'successfully deleted')
    return redirect('/myapp/view_object_get/')

def send_reply_post(request):
    o=request.POST['reply']
    a=Complaints.objects.get(id=request.session['id'])
    a.reply=o
    a.save()
    messages.success(request,'successfully sended')
    return redirect('/myapp/view_complaint_get/')

