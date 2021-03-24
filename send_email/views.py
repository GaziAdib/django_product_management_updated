from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def send_my_mail(request):
    send_mail(
        'This is the subject of my mail hello everybody',
        'This is the test message body from django product management website',
        'greatadib82@gmail.com',
        ['adibcse10@gmail.com'],
        fail_silently=False
    )

    return render(request, 'sendMail/sendMail.html')
