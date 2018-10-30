from django.conf.urls import url, include

"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sign import views  # 导入sign应用view文件

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),  # 添加index/配置路径
    path('login_action/', views.login_action),  # 添加login_action/配置路径
    path('event_manage/', views.event_manage),  # 添加event_manage/配置路径
    path('search_name/', views.search_name),  # 添加search_name/配置路径
    path('guest_manage/', views.guest_manage),  # 添加guest_manage/配置路径
    # (?P<event_id>[0-9]+) 配置二级目录，发布会 id，要求必须为数字。而且匹配的数字，将会作为 sign_index()视图函数的参数
    # path('sign_index/(?P<event_id>[0-9]+)/$', views.sign_index),
    path('logout/', views.logout),

    path('', views.index),
    path('index/', views.index),
    path('accounts/login/', views.index),
    # path('sign_index/<int:event_id>/', views.sign_index),
    # path('sign_index_action/<int:event_id>/', views.sign_index_action),
    path('api/', include('sign.urls')),
]
