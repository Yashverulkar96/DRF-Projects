from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class SendEmail(APIView):
    def post(self, request):
        email=request.data['to']
        emailbody=EmailMessage(
            'This is Subject',
            'This is email description',
            settings.EMAIL_HOST_USER,
            [email]

        )
        # to send attachment add file path in brackets
        emailbody.attach_file('manage.py')
        emailbody.send(fail_silently=False)
        return Response({'status':True,'message':'Email Sent Successfully'})