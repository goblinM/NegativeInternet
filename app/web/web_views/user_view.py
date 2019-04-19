'''
created by goblinM(莫敏欣) 2019-04-18
这个是用户登录的函数
使用viewsets
'''
from django.contrib import auth
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response

from app.web.models import User
from app.web.webSerializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def get_permissions(self):
    #     pass


    @action(detail=False,methods=["POST"])
    def login(self,request):
        """
        这个验证登录用户
        :param request: username登录的用户，password登录的密码
        :return: 返回用户的基本信息
        """
        data = request.data
        username = data.get("username")
        password = data.get("password")
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            # 设置token,没有则生成
            if Token.objects.filter(user=user) == False:
                # token = Token.objects.get(user=user)
                # token.delete()
                Token.objects.create(user=user)
            userinfo = User.objects.filter(username=username)
            user_serializer = UserSerializer(userinfo,many=True)
            return Response(user_serializer.data[0])
        else:
            return Response("Failed")


