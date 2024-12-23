from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from datetime import datetime

import pyotp
import requests
# email verification
from django.core.mail import EmailMultiAlternatives


from .utils import send_otp
from .forms import RegistrationForm
from .models import Account

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            

            user = Account.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,  password=password)

            user.phone_number = phone_number
            #user.is_active = True
            user.save()

            # send otp
            
            send_otp(request, user=user, email=email)
            request.session['username'] = username
            

            messages.success(request, "Successful registration. An activation code was sent to your email.")
            '''
            messages.success(request, "Successful registration. An activation code was sent to your email.")
            '''
            return redirect('activate')
           # return redirect('login')
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }

    return render(request, 'account/register.html', context)



def login_view(request):
    next_url = request.GET.get('next', '/')
    # already logged in
    if request.user.is_authenticated:
        #messages.warning(request, f"You are already logged in.")
        return redirect("home")
    #login user
    if request.method == 'POST':
        # collect credentials
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            ## redirecting user to previous page after login
            # get url of previous page
            try:
                url = request.META.get('HTTP_REFERER')
                
                query = requests.utils.urlparse(url).query
                print(f'Query: {query}')
                # dict of the url parameters
                params = dict(x.split('=') for x in query.split('&'))
                if "next" in params:
                    nextPage = params['next']
                    print(nextPage)
                    return redirect(nextPage)
            #messages.success(request, 'login successful!')
            except:
                pass
            return redirect("home")
            #return redirect("home")
        else:
            messages.error(request, "Invalid credentials or user does not exist (create an account).")
            return redirect("login")

    context = {}
    return render(request, 'account/login.html', context)


@login_required(login_url="login")
def logout_view(request):
    logout(request)
    messages.success(request, "logout successful.")
    return redirect("login")


def forgot_password(request):
    if request.method == "POST":
        username = request.POST.get('username').strip()
        request.session['username'] = username
        
        account_exists = Account.objects.filter(username=username).exists()

        if account_exists:
            user = Account.objects.get(username__exact=username)
            print(user)

            return redirect('new_password')
        else:
            messages.error(request, "User does not exist!")
            return redirect('forgot_password')

    return render(request, 'account/forgot_password.html')



# new password with OTP
def create_new_password(request):
    if request.method == 'POST':
        username = request.session['username']
        #current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = Account.objects.get(username__exact=username)

        if new_password == confirm_password:
            try:
                validate_password(confirm_password)
                user.set_password(new_password)
                user.save()

                messages.success(request, "Password changed.")
                return redirect("login")
            except:
                messages.error(request, "'This password is too short. It must contain at least 8 characters.', 'This password must contain at least 8 characters, one uppercase letter, one lowercase letter, one digit and one symbol.'")
                return redirect("new_password")
        else:
            messages.error(request, "Please match passwords.")
            return redirect("new_password")

    
    return render(request, 'account/create_new_password.html')


#account verification
def activate_view(request):
    # activate with OTP
    if request.method == 'POST':

        otp = request.POST['otp']
        username = request.session['username']

        otp_2 = request.session['otp']
        otp_secret_key = request.session['otp_secret_key']
        otp_valid_until = request.session['otp_valid_date']

        if otp_secret_key and otp_valid_until is not None:
            valid_until = datetime.strptime(otp_valid_until, '%Y-%m-%d %H:%M:%S')

            if valid_until > datetime.now():
                t_otp = pyotp.TOTP(otp_secret_key, interval=60)
                #if t_otp.verify(otp):
                if otp == otp_2:
                    user = get_object_or_404(Account, username=username)

                    user.is_active = True
                    user.save()

                    # delete sessions
                    del request.session['otp_secret_key']
                    del request.session['otp_valid_date']
                    del request.session['otp']

                    return redirect('login')
                else:
                    error_message = 'Invalid OTP.'
                    messages.error(request, "Invalid OTP.")
            else:
                error_message = 'OTP has expired.'
                messages.error(request, "OTP has expired. Register again!")
                user = get_object_or_404(Account, username=username)
                user.delete()
        else:
            error_message = 'Something went wromg.'
            messages.error(request, "Something went wrong.")
        


    return render(request, 'account/account-verification.html')

    
