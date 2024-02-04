from django.shortcuts import render , redirect 
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.authtoken.models import Token
import random
from django.core.mail import send_mail
#home
@login_required(login_url='login')
def home(request, category_slug=None, author_slug=None):
    books_url='http://127.0.0.1:8000/api/books/'
    authors_url='http://127.0.0.1:8000/api/authors/'
    categories_url='http://127.0.0.1:8000/api/categories/'

    user = request.user
    token = Token.objects.get(user=user)
    headers = {'Authorization': f'Token {token.key}'}

    books = requests.get(url=books_url,headers=headers,).json()
    authors =requests.get(url=authors_url,headers=headers).json()
    categories =requests.get(url=categories_url,headers=headers).json()

    if(category_slug != None):
        books = requests.get(f'http://127.0.0.1:8000/api/books/?search={category_slug}',headers=headers,).json()

    if(author_slug != None):
        books = requests.get(f'http://127.0.0.1:8000/api/books/?search={author_slug}',headers=headers,).json()
    
    cartitems = requests.get(f'http://127.0.0.1:8000/api/cartitems/?search={user.id}',headers=headers,).json()
    book_id = [item['book'] for item in cartitems]
    for book in books:  
        if book['id'] in book_id:
            book['in_cart'] = True
    res = {'books':books,'authors':authors,'categories':categories ,'book_id':book_id,}

    #page
    paginator = Paginator(res['books'], 6)

    page = request.GET.get('page')
    try:
        p_books= paginator.page(page)
    except PageNotAnInteger:
        p_books = paginator.page(1)
    except EmptyPage:
        p_books = paginator.page(paginator.num_pages)
    data = {'books':p_books,'authors':authors,'categories':categories}
    cart_value=car_value(user.id,headers)
    return render(request, 'bstore/index.html',{'data':data,'cart_value':cart_value,} )

#signup
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    error_message = ""

    if request.method == 'POST':
        uname = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('cpassword')

        if pass1 != pass2:
            error_message = 'Your password and confirm password are not the same!'
        else:
            try:
                user = User.objects.get(email=email)
                error_message = 'Email already registered!'
            except User.DoesNotExist:
                try:
                    my_user = User.objects.create_user(uname, email, pass1)
                    my_user.first_name = fname
                    my_user.last_name = lname
                    my_user.save()
                    return redirect('login')
                except IntegrityError as e:
                    error_message = 'Username is not available!'

    return render(request, 'bstore/signup.html', {'error_message': error_message})

#login
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            error_message = "Invalid username!"
            return render(request, 'bstore/login.html', {'error_message': error_message})
        

        authenticated_user = authenticate(request, username=username, password=password)
        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect('home')
        else:
            error_message = "Invalid password!"
            return render(request, 'bstore/login.html', {'error_message': error_message})
    
    return render(request, 'bstore/login.html', {})

#logout
def user_logout(request):
    logout(request)
    return redirect('login')

#book
@login_required(login_url='login')
def book(request , book_slug):
    user = request.user
    token = Token.objects.get(user=user)
    headers = {'Authorization': f'Token {token.key}'}

    books_url=f'http://127.0.0.1:8000/api/books/?search={book_slug}'
    books = requests.get(url=books_url,headers=headers,).json()

    authors_url=f'http://127.0.0.1:8000/api/authors/{books[0]['author']}/'
    author=requests.get(url=authors_url,headers=headers,).json()
    cartitems = requests.get(f'http://127.0.0.1:8000/api/cartitems/?search={user.id}',headers=headers,).json()
    book_id = [item['book'] for item in cartitems]
    for book in books:  
        if book['id'] in book_id:
            book['in_cart'] = True
    cart_value=car_value(user.id,headers)
    return render(request, 'bstore/product.html',{'data':books,'author':author,'cart_value':cart_value,} )

#cart
@login_required(login_url='login')
def cart(request):
    user = request.user
    token = Token.objects.get(user=user)
    headers = {'Authorization': f'Token {token.key}'}
    cartitem_url = f'http://127.0.0.1:8000/api/cartitems/?search={user.id},'
    data = requests.get(url=cartitem_url,headers=headers,).json()
    total_price = 0
    for i in range(len(data)):
        book=requests.get(f'http://127.0.0.1:8000/api/books/{data[i]['book']}/',headers=headers,).json()
        author=requests.get(f'http://127.0.0.1:8000/api/authors/{book['author']}/',headers=headers,).json() 
        data[i]['book_title'] = book['title']
        data[i]['book_price'] = book['price']
        data[i]['book_cover'] = str(book['cover_image'])
        data[i]['book_author'] = author['name']
        total_price += float(data[i]['book_price'])

    cart_value=car_value(user.id,headers)
    return render(request, 'bstore/cart.html',{'data':data,'total_price':total_price,'cart_value':cart_value,} )

#order placed
@login_required(login_url='login')
def order(request):
    
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')

    random_part = str(random.randint(100000, 999999))
    order_id = f'AKRN{random_part}'
    delivery_data={'name':name,'email':email,'address':address ,'order_id':order_id}
    user = request.user
    token = Token.objects.get(user=user)
    headers = {'Authorization': f'Token {token.key}'}
    cartitem_url = f'http://127.0.0.1:8000/api/cartitems/?search={user.id},'
    cart_items = requests.get(url=cartitem_url,headers=headers,).json()
    total_price = 0
    for i in range(len(cart_items)):

        order_items={ "book": cart_items[i]['book'],"order_user": user.id}
        requests.post('http://127.0.0.1:8000/api/orderitems/',headers=headers,data=order_items)

        requests.delete(f'http://127.0.0.1:8000/api/cartitems/{cart_items[i]['id']}/',headers=headers)

        book=requests.get(f'http://127.0.0.1:8000/api/books/{cart_items[i]['book']}/',headers=headers,).json()
        author=requests.get(f'http://127.0.0.1:8000/api/authors/{book['author']}/',headers=headers,).json()
        cart_items[i]['book_title'] = book['title']
        cart_items[i]['book_price'] = book['price']
        cart_items[i]['book_author'] = author['name']
        total_price += float(cart_items[i]['book_price'])

    #send mail
    subject = 'Order Details'
    context = {'data': cart_items, 'total_price': total_price, 'delivery_data': delivery_data}
    email_content = render(request, 'bstore/mail_order.html', context).content.decode('utf-8')
    message = 'Thank you for your order!'
    recipient_list = [context['delivery_data']['email']]
    from_email = ""
    send_mail(subject, message, from_email, recipient_list, html_message=email_content)

    cart_value=car_value(user.id,headers)
    return render(request, 'bstore/order.html',{'data':cart_items,'total_price':total_price,'cart_value':cart_value,'delivery_data':delivery_data} ) 


#profile
@login_required(login_url='login')
def profile(request):
    user = request.user
    token = Token.objects.get(user=user)
    headers = {'Authorization': f'Token {token.key}'}

    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        if len(pass1)>3:
            data= {"first_name":fname,"last_name":lname,"email":email, 'password':pass1 }
            requests.put(f'http://127.0.0.1:8000/api/users/{user.id}/',headers=headers,data=data)
            logout(request)
            return redirect('login')
            
        else:
            data= {"first_name":fname,"last_name":lname,"email":email}
        
        requests.put(f'http://127.0.0.1:8000/api/users/{user.id}/',headers=headers,data=data)


    orderitem_url = f'http://127.0.0.1:8000/api/orderitems/?search={user.id}'
    data = requests.get(url=orderitem_url,headers=headers,).json()
    for i in range(len(data)):
        book=requests.get(f'http://127.0.0.1:8000/api/books/{data[i]['book']}/',headers=headers,).json()
        author=requests.get(f'http://127.0.0.1:8000/api/authors/{book['author']}/',headers=headers,).json()
        
        data[i]['book_title'] = book['title']
        data[i]['book_price'] = book['price']
        data[i]['book_cover'] = str(book['cover_image'])
        data[i]['book_author'] = author['name']

    cart_value=car_value(user.id,headers)
    return render(request, 'bstore/profile.html',{'data':data,'cart_value':cart_value,} )

#cart_value
def car_value(user_id,header):
    cartitem_url = f'http://127.0.0.1:8000/api/cartitems/?search={user_id}'
    data = requests.get(url=cartitem_url,headers=header,).json()
    return len(data)

#add cart
def add_to_cart(request,book_id):
    user = request.user
    token = Token.objects.get(user=user)
    headers = {'Authorization': f'Token {token.key}'}
    book_add = requests.get(f'http://127.0.0.1:8000/api/books/{book_id}/',headers=headers,).json()
    data={ "book": book_add['id'],"cart_user": user.id}
    requests.post('http://127.0.0.1:8000/api/cartitems/',headers=headers,data=data)
    
    referring_url = request.META.get('HTTP_REFERER')
    return redirect(referring_url)

#delete cart
def delete_cart(request, cart_id):
    user = request.user
    token = Token.objects.get(user=user)
    headers = {'Authorization': f'Token {token.key}'}
    requests.delete(f'http://127.0.0.1:8000/api/cartitems/{cart_id}/',headers=headers)
    return redirect('cart')

#delete order
def delete_order(request, order_id):
    user = request.user
    token = Token.objects.get(user=user)
    headers = {'Authorization': f'Token {token.key}'}
    requests.delete(f'http://127.0.0.1:8000/api/orderitems/{order_id}/',headers=headers)
    return redirect('profile')


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
