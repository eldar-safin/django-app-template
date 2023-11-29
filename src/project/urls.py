"""
from my_app import views
path('', views.home, name='home')

from other_app.views import Home
path('', Home.as_view(), name='home')

from django.urls import include, path
path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
