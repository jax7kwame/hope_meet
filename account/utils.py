import pyotp
from datetime import datetime, timedelta
from django.core.mail import EmailMultiAlternatives


def send_otp(request, user, email):
    # time based one time password
    t_otp = pyotp.TOTP(pyotp.random_base32(), interval=60)
    otp = t_otp.now()

    #print(f'otp 2 - {otp}')
    request.session['otp'] = otp
    request.session['otp_secret_key'] = t_otp.secret

    valid_date = datetime.now() + timedelta(minutes=10)
    request.session['otp_valid_date'] = valid_date.strftime("%Y-%m-%d %H:%M:%S")#str(valid_date)
    # send email
    msg = EmailMultiAlternatives(
                "Activate commineon account.", 
                f"Hi { user.first_name }",
                "commineon@gmail.com",
                [email])
    msg.attach_alternative(f'<p>Hi <strong>{user.first_name}</strong></p><p>Thank you for joining us. Here is your OTP: <strong>{ otp }</strong></p><p>For any feedback: <b>commineon@gmail.com</b></p>', "text/html")
    
    msg.send()


def send_otp_forgot_password(request, user, email):
    # time based one time password
    t_otp = pyotp.TOTP(pyotp.random_base32(), interval=60)
    otp = t_otp.now()

    #print(f'otp 2 - {otp}')
    request.session['otp'] = otp
    request.session['otp_secret_key'] = t_otp.secret

    valid_date = datetime.now() + timedelta(minutes=10)
    request.session['otp_valid_date'] = valid_date.strftime("%Y-%m-%d %H:%M:%S")#str(valid_date)
    # send email
    msg = EmailMultiAlternatives(
                "Forgot password OTP", 
                f"Hi { user.first_name }",
                "commineon@gmail.com",
                [email])
    msg.attach_alternative(f'<p>Hi <strong>{user.first_name}</strong></p><p>Use the OTP to create a new password. Here is your OTP: <strong>{ otp }</strong></p><p>For any feedback: <b>commineon@gmail.com</b></p>', "text/html")
    
    msg.send()