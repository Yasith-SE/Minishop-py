from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    # Get all available products
    products = Product.objects.filter(is_available=True)
    return render(request, 'index.html', {'products': products})

def product_detail(request, slug):
    # Get one specific product or return a 404 error if it doesn't exist
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, 'detail.html', {'product': product})

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, UserProfile
from .forms import CustomerSignUpForm, SellerSignUpForm

# ... keep your existing home and product_detail views ...

def signup_view(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Save the seller role
            is_seller = form.cleaned_data.get('is_seller')
            UserProfile.objects.create(user=user, is_seller=is_seller)
            # Log them in automatically
            login(request, user)
            return redirect('core:home')
    else:
        form = CustomSignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('core:home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('core:home')
    

    
def customer_signup_view(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, is_seller=False)
            login(request, user)
            return redirect('core:home')
    else:
        form = CustomerSignUpForm()
    return render(request, 'signup.html', {'form': form})

def seller_signup_view(request):
    if request.method == 'POST':
        form = SellerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Save the extra seller data to the profile
            UserProfile.objects.create(
                user=user, 
                is_seller=True,
                date_of_birth=form.cleaned_data.get('date_of_birth'),
                phone_number=form.cleaned_data.get('phone_number'),
                home_address=form.cleaned_data.get('home_address'),
                postal_code=form.cleaned_data.get('postal_code')
            )
            login(request, user)
            return redirect('core:home')
    else:
        form = SellerSignUpForm()
    return render(request, 'seller_signup.html', {'form': form})