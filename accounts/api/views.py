from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from accounts.api.serializers import UserCreateSerializer, UserLoginSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserLoginAPIView(APIView):
    queryset = User.objects.all()
    serializer_class=UserLoginSerializer

    def post(self,request):
        data = request.data
        serializer = UserLoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
