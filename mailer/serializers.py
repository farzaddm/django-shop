from rest_framework import serializers


class SendEmailSerializer(serializers.Serializer):
    to = serializers.EmailField()
    subject = serializers.CharField(max_length=255)
    message = serializers.CharField(style={"base_template": "textarea.html"})