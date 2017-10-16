from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer




class UserDetailSerializer(ModelSerializer):

    class Meta:

        model=User
        fields=['username','email','first_name','last_name']




class UserCreateSerializer(ModelSerializer):
    email2 = serializers.EmailField(label='Confirm Email')
    email = serializers.EmailField(label='Email')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]

        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get('email')
        email2 = value

        if email1 != email2:
            raise ValidationError('Emails must match')

        email = data['email']
        user_qs = User.objects.filter(email=email)

        if user_qs.exists():
            raise ValidationError('User already exists')

        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']

        user_obj = User(username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()

        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(allow_blank=True,required=False)
    email = serializers.EmailField(label='Email',allow_blank=True,required=False)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',
        ]

        extra_kwargs = {"password":
                            {"write_only": True}
                        }


    def validate(self,data):
        user_obj=None
        email=data.get('email')
        username=data.get('username')
        password=data['password']

        if not username and not email:
            raise ValidationError('Enter username or email')


        user=User.objects.filter(

            Q(email=email)|
            Q(username=username)

        ).distinct()
        user=user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count()==1:
            user_obj=user.first()

        else:
            raise ValidationError('Username/email is not valid.')

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('Incorrect Credintials')


        data['token']='Some random token.'

        return data




