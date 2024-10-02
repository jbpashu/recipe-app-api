"""
Views for the user API.
"""

from rest_framework import generics

from user.serializers import UserSerializer

from django.shortcuts import render


class CreateUserView(generics.CreateAPiView):
    """Create a new uuser in the system"""
    seralizer_class = UserSerializer