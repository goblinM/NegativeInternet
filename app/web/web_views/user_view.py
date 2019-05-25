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
            return Response("failed")

    @action(detail=False,methods=["POST"])
    def get_user_infor(self,request):
        """
        获取用户的信息
        :param request:
        :return: 用户的信息
        """
        user_id = request.data.get("user_id")
        print(user_id)
        if user_id:
            userinfo = User.objects.filter(id=user_id)
            # print(userinfo)
            user_serializer = UserSerializer(userinfo, many=True)
            return Response(user_serializer.data)
        else:
            userinfo = User.objects.all()
            user_serializer = UserSerializer(userinfo,many=True)
            # print(user_serializer.data)
            return Response(user_serializer.data)

    @action(detail=False,methods=["POST"])
    def delete_user(self,request):
        """
        删除用户
        :param request:
        :return: 成功ok 失败failed
        """
        data = request.data
        uid = data.get("user_id")
        try:
            User.objects.filter(id=uid).delete()
            return Response("ok")
        except:
            return Response("failed")

    @action(detail=False,methods=["POST"])
    def add_user(self,request):
        """
        新增用户
        :param request:
        :return: 成功ok 失败failed
        """
        data = request.data
        username = data.get("username")
        password = data.get("password")
        user_type = data.get('user_type')
        email = data.get("email")
        phone = data.get("phone")
        try:
            User.objects.create_user(username=username,user_type=user_type,email=email,user_phone=phone)
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            return Response("ok")
        except Exception as e:
            print(e)
            return Response("failed")

    @action(detail=False,methods=["POST"])
    def update_user(self,request):
        """
        修改用户
        :param request:
        :return: 成功ok 失败failed
        """
        data = request.data
        username = data.get("username")
        password = data.get("password")
        user_type = data.get('user_type')
        email = data.get("email")
        phone = data.get("phone")
        try:
            if password:
                user = User.objects.filter(username=username)[0]
                user.set_password(password)
                user.save()
                User.objects.filter(username=username).update(user_type=user_type, email=email, user_phone=phone)
            else:
                User.objects.filter(username=username).update(user_type=user_type,email=email,user_phone=phone)
            return Response("ok")
        except:
            return Response("failed")


