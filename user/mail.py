from django.core.mail import send_mail
from random import randint
from django.conf import settings
from django.template.loader import render_to_string
from backend.config import config


def send_otp_email(email):
    otp = randint(1000, 9999)
    context = {"otp": otp}
    html_message = render_to_string(        
        "emailTemplates/otpEmail.html",
        context,
    )
    send_mail(
        "Email Verification OTP",
        "",
        settings.EMAIL_HOST_USER,
        [email],
        html_message=html_message,
        fail_silently=False,
    )
    return otp


def send_kyc_email():
    context = {"user_url": config["USER_URL"]}
    html_message = render_to_string(
        "emailTemplates/kycEmail.html",
        context,
    )
    send_mail(
        "KYC application",
        "",
        settings.EMAIL_HOST_USER,
        config["KYC_APPROVERS"],
        html_message=html_message,
        fail_silently=False,
    )
