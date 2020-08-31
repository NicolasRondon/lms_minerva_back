from rest_framework.views import APIView
from .models import MinervaUser, CodeConfirmation
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from core.utils.properties import check_email
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView



class CreateUserView(APIView):

    model = MinervaUser
    def get_queryset(self):
        return self

    def post(self, request, *args, **kwargs):
        data = request.data
        email = data['email']
        password = data['password']
        password_confirm = data['password_confirm']
        if password != password_confirm:
            e = "La contraseña no coincide"
            return Response({"message": e}, status=400)
        validate_email = check_email(email=email)
        print(validate_email)

        values = ['password', 'first_name', 'last_name', 'email', 'password_confirm']
        for value in values:
            if not value in data.keys():
                e = "No hay {} en el body".format(value)
                return Response({"error": e}, status= 400)
        if validate_email == True:
            new_student = MinervaUser.objects.create(
                email = data['email'],
                first_name = data['first_name'],
                last_name= data['last_name'],
                password= make_password(data['password'])
            )
            new_student.groups.add(1)

            return Response({}, status=201)
        else:
            return Response({}, status=400)


class ActivateUserView(APIView):

    model = MinervaUser
    def get_queryset(self):
        return self

    def put(self, request, *args, **kwargs):
        data = request.data
        code_confirmation = data['code']
        if not 'uuid' in kwargs.keys():
            e = "No se envio un usuario para activar"
            return Response({"message": e}, status=400)
        else:
            uuid = self.kwargs.get('uuid')
            try:
                code = CodeConfirmation.objects.get(user=uuid)

                user = MinervaUser.objects.get(institutional_id=uuid)
                if user.is_active == False:
                    user.is_active = True
                    user.save()
                    return Response({}, status=200)
                else:
                    e = "Tu usuario ya fue activado"
                    return Response({"message": e}, status=400)
            except ObjectDoesNotExist:
                e = "El usuario no existe"
                return Response({"message":e}, status=400)
