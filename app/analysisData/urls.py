from django.urls import path

from app.analysisData.views import index

urlpatterns = [
    path(r'',index,name='index')
]