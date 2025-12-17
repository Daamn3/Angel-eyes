from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.http import JsonResponse


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

def  ct_register(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    phone=request.POST['phone']
    photo=request.FILES['photo']
    username=request.POST['username']
    password=request.POST['password']
    email=request.POST['email']
    if User.objects.filter(username= username).exists():
        return JsonResponse({'status':'user already exists'})
    else:
        user=User.objects.create_user(username=username,password=password)
        user.groups.add(Group.objects.get(name='Caretaker'))
        a=caretaker()
        a.fname=fname
        a.lname=lname
        a.place=place
        a.pin=pin
        a.post=post
        a.phone=phone
        a.email=email
        a.photo=photo
        a.LOGIN=user
        a.save()
        print(password)
        return JsonResponse({'status':'registered successfully'});

def ct_home(request):
    un=request.POST['uname']
    pw=request.POST['pass']
    print(un,pw)
    user = authenticate(request, username=un, password=pw)
    if user is not None:
        if user.groups.filter(name='Caretaker').exists():
            lid =user.id
            return JsonResponse({'message':'login successfull','lid':lid})
        else:
            print('1st else')
            return JsonResponse({'message':'invalid credentials'})

    else:
        return JsonResponse({'message':'invalid username or password'})



def pro_pic(request):
    lid=request.POST['lid']
    id=caretaker.objects.get(LOGIN_id=lid)
    pfp=id.photo.url
    return JsonResponse({
        'photo':pfp
    })

def pro_det(request):
    lid=request.POST['lid']
    id=caretaker.objects.get(LOGIN_id=lid)
    fname=id.fname
    lname=id.lname
    gender=id.gender
    place=id.place
    post=id.post
    photo=id.photo.url
    pin=id.pin
    phone=id.phone
    email=id.email
    return JsonResponse({
        'fname' : fname,
        'lname' : lname,
        'gender' :gender,
        'place': place,
        'post':post,
        'photo': photo,
        'pin':pin,
        'phone' : phone,
        'email': email,
    })



