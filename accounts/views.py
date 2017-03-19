from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib import messages

def send_login_email(request):
    email = request.POST['email']
    #send_mail('subject','to_list','from_email','body')
    print(type(send_mail))
    send_mail(
        'Your login link for Superlists',
        'body text tbc',
        'noreply@superlists',
        [email],
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )

    return redirect('/')
