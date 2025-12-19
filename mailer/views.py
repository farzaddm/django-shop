from django.shortcuts import render
from rest_framework.views import APIView
from django.core.mail import send_mail, EmailMultiAlternatives
from .serializers import *
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from django.template.loader import render_to_string


class SendEmailAPIView(GenericAPIView):
    serializer_class = SendEmailSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        context = {
            "subject": data["subject"],
            "message": data["message"],
        }

        text_content = render_to_string("mailer/email.txt", context)
        html_content = render_to_string("mailer/email.html", context)
        email = EmailMultiAlternatives(
            subject=data["subject"],
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[data["to"]],
        )

        email.attach_alternative(html_content, "text/html")
        email.send()

        return Response(
            {"detail": "Email sent successfully"},
            status=status.HTTP_200_OK
        )
