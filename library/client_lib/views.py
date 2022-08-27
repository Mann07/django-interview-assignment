
from django.shortcuts import render,redirect
from django.http import  HttpResponseRedirect
from .models import user,books
from django.contrib import messages
from django.urls import reverse


def admin_redirect(request):
    return redirect('admin/')

def login(request):
    return render(request,'login.html')

def user_signup_page(request):
    return render(request,'user_signup.html')  

def user_signup(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        user_id = request.POST['user_id']
        user_pass = request.POST['user_password']

        newuser = user(name=user_name,user_id=user_id,user_pass = user_pass)
        newuser.save()
        return HttpResponseRedirect('login')

def user_view(request):
    try:
        userobj = user_login.var
        if userobj:
            user_name = getattr(userobj,'name')
            book_data = books.objects.all().values() 
            return render(request,'user_view.html',{'book_data' : book_data,'user_name':user_name})
        else :
            return HttpResponseRedirect('login')
    except:
        return HttpResponseRedirect('login')

def user_login(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        userpass = request.POST['pass']

        try:
            user_login.var= user.objects.get(user_id = userid, user_pass= userpass)
            userobj=user_login.var
            user_name = getattr(userobj,'name')
            book_data = books.objects.all().values() 
            return render(request,'user_view.html',{'book_data' : book_data,'user_name':user_name})
            
        except Exception as e:
            print(e)
            messages.info(request,"Invalid details")
            return render(request,"user_login.html")

    else:
        return render(request,"user_login.html")    
        
def borrowed(request,id):
    if request.method == 'GET':
        if id is not None:
            book= books.objects.get(id=id)
            book.status = 0
            userobj=user_login.var
            user_name = getattr(userobj,'name')
            book.borrower_name = user_name  
            book.save()
            book.refresh_from_db()
            book_data = books.objects.all().values() 
            return HttpResponseRedirect(reverse('client_lib:user_view') )

def borrowed_book(request):
    if request.method == 'GET':
        try:
            userobj = user_login.var
            if userobj :
                user_name=getattr(userobj,'name')
                book_list = books.objects.filter(borrower_name = user_name).values()
                return render(request,"borrowed_book.html",{'book_list' : book_list})
        except:
            return HttpResponseRedirect('login')

def return_book(request,title):
    if request.method == 'GET':
        book_title = title
        book = books.objects.get(title=book_title)
        book.status = True
        book.borrower_name = "None"
        book.save()
        userobj = user_login.var
        user_name=getattr(userobj,'name')
        book_list = books.objects.filter(borrower_name = user_name).values()
        return HttpResponseRedirect(reverse('client_lib:borrowed_book'))

def logout(request):
    user_login.var = None
    return  HttpResponseRedirect('login')

            