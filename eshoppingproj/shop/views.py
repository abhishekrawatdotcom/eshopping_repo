from django.shortcuts import render
from django.http import HttpResponse
from shop.models import product,contact,orders,orderupdate,EMPMODEL
import  json
from django.views.decorators.csrf import csrf_exempt
from shop.forms import RegistrationForm,loginform
from django.http import HttpResponse
from django.shortcuts import redirect
from shop.paytm import cheksum
Merchant_Key='vN9adsz8HjPBQS0S'
import checksum

def index(request):
    products = product.objects.all()
    return render(request,'index.html',{'products':products})


def about(request):
    return render(request,'about.html')

def contactview(request):
    if request.method == 'POST':

        name = request.POST.get('name', '')

        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        print(name, email, phone, desc)
        count = contact(name=name, email=email, phone=phone, desc=desc)
        count.save()


    return render(request,'contact.html')






def productview(request, myid):
    prod=product.objects.filter(id= myid)


    return render(request,'productview.html',{'prodd':prod})
def searchmatch(query, item):
    if query in  item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False


def search(request):
    query=request.GET.get('search')
    prot = product.objects.all()
    products=[item for item in prot if searchmatch(query,item)]

    return render(request,'search.html',{'products':products})

def checkout(request):
    if request.method == 'POST':

        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        items_json =request.POST.get('itemsjson', '')

        email = request.POST.get('email', '')
        phone = request.POST.get('phone','')
        address = request.POST.get('address', '')
        state = request.POST.get('state', '')
        city = request.POST.get('city', '')
        zip = request.POST.get('zip','')


        print(name, email, phone, address, state,zip, city,items_json,amount)
        order = orders(items_json=items_json,name=name, email=email, phone=phone,zip=zip, address=address, state=state, city=city, amount=amount)
        order.save()
        update=orderupdate(order_id=order.order_id,update_desc='The order has been placed')
        update.save()
        thank=True
        id=order.order_id
        #return render(request,'checkout.html',{'thank':thank,'id':id})
        param_dict={
            "MID": "BIJNyb01758738100470",
            "ORDER_ID": str(order.order_id),
            "CUST_ID": email,
            "TXN_AMOUNT": str(amount),
            "CHANNEL_ID": "WEB",
            "INDUSTRY_TYPE_ID": "Retail",
            "WEBSITE": "WEBSTAGING",
            "CALLBACK_URL":'http://127.0.0.1:8000/shop/handlerequest'
        }
        param_dict['CHECKSUMHASH']= cheksum.generate_checksum(param_dict, Merchant_Key)
        return render(request,'paytm.html',{'param_dict':param_dict})

    return render(request,'checkout.html')

@csrf_exempt
def handlerequest(request):
    formm=request.POST
    request_dict={}
    for i in formm.keys():
        request_dict[i]=formm[i]
        if i =="CHECKSUMHASH":
            cheksumm=formm[i]

    verify=cheksum.verify_checksum(request_dict,Merchant_Key,cheksumm)
    if verify:
        if request_dict['RESPCODE'] =='01':
            print('Your Order Is Successfull')
        else:
            print('order is not success full' + request_dict['RESPMSG'])

    return render(request,'paymentstatus.html',{'response':request_dict})

def pro1(request):
    products = product.objects.all()
    return render(request,'pro1.html',{'products':products})

def pro2(request):
    products = product.objects.all()
    return render(request,'pro2.html',{'products':products})

def pro3(request):
    products = product.objects.all()
    return render(request,'pro3.html',{'products':products})












def registrationview(request):
    if request.method=='POST':
        rform= RegistrationForm(request.POST)
        if rform.is_valid():
            fname=request.POST.get('first_name')
            lname = request.POST.get('last_name')
            uname = request.POST.get('user_name')
            pwd = request.POST.get('password')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            data = EMPMODEL(
                first_name=fname,
                last_name=lname,
                user_name=uname,
                password=pwd,
                mobile=mobile,
                email=email,

            )
            data.save()
            rform =  RegistrationForm()
            return render(request, 'pro2.html', {'rform': rform})
        else:
            return HttpResponse('user invalid data')
    else:
        rform = RegistrationForm()
        return render(request, 'pro2.html', {'rform': rform})


def loginview(request):
    if request.method=='POST':
        lform=loginform(request.POST)
        if lform.is_valid():
            uname=request.POST.get('user_name')
            pwd = request.POST.get('password')
            user = EMPMODEL.objects.filter(user_name=uname)
            password = EMPMODEL.objects.filter(password=pwd)

            if user and password:
                return redirect('/shop/index')
            else:
                return redirect('/shop/loginhandle')
        else:
            return HttpResponse('user invalid data')
    else:

        lform = loginform()
        return render(request, 'pro3.html', {'lform': lform})



def logoutview(request):
    if request.method=='POST':
        lform=loginform(request.POST)
        if lform.is_valid():
            uname=request.POST.get('user_name')
            pwd = request.POST.get('password')
            user = EMPMODEL.objects.filter(user_name=uname)
            password = EMPMODEL.objects.filter(password=pwd)

            if user and password:
                return redirect('/shop/logout')
            else:
                return HttpResponse('Fail')
        else:
            return HttpResponse('user invalid data')
    else:

        lform = loginform()
        return render(request, 'logout.html', {'lform': lform})


def loginhandle(request):
    return render(request,'loginhandle.html')