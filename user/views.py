from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from django.contrib.auth.hashers import make_password


# Create your views here.
class Join(APIView):
    def get(self, request):
        return render(request, "user/join.html")

    def post(self, request):
        request.data.get("email")

        email = request.data.get("email", None)
        nickname = request.data.get("nickname", None)
        name = request.data.get("name", None)
        password = request.data.get("password", None)

        User.objects.create(email=email,
                            nickname=nickname,
                            name=name,
                            password=make_password(password),
                            profile_image='default.jpg'
                            )

        return Response(status=200)

class Login(APIView):
    def get(self, request):
        return render(request, "user/login.html")

    def post(self, request):
        email = request.data.get("email", None)
        password = request.data.get("password", None)
        user = User.objects.filter(email=email).first()
        user_pw = user.password
        if user is None:
            return Response(status=404, data=dict(message="User not found"))


        if user.check_password(password):
            return Response(status=200)
        else:
            return Response(status=404)

            return Response(status=200)
