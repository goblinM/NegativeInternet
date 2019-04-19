'''
created by goblinM(莫敏欣) by 2019-04-18
序列化文件
'''
import serializers as serializers
from rest_framework import serializers

from app.web.models import User


class UserSerializer(serializers.ModelSerializer):
    # user = User.objects.all()

    class Meta:
        fields = '__all__'
        model = User