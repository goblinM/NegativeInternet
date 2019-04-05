from django.urls import path

from app.web.views import index

urlpatterns = [
    path(r'',index,name='index')
]