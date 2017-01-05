from django.shortcuts import render
import json
from rest_framework import viewsets, permissions, status, views
from models import Account
from serializers import AccountSerializer
from rest_framework.response import Response
from permissions import IsAccountOwner


class AccountViewSet(viewsets.ModelViewSet):
	look_field = 'username'
	queryset = Account.objects.all()
	serializer_class = AccountSerializer

	def get_permission(self):
		if self.request.method in permissions.SAFE_METHODS:
			return (permissions.AllowAny(),)

		if self.request.method == 'POST':
			return (permissions.AllowAny(),)

		return (permissions.IsAuthenticated(), IsAccountOwner(),)

	def create(self, request):
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			Account.objects.create_user(**serializer.validated_data)

		return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
		return Response({'status': 'Bad request','message': 'Account could not be created with received data.'}, status=status.HTTP_400_BAD_REQUEST)