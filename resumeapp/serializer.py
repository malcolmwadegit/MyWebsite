from rest_framework import serializers
from django.contrib.auth.models import Contact


class ContactSerializer (serializers.Serializer):
    class Meta:
        model = Contact

        fields = ['email', 'message']