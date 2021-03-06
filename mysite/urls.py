"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls.resolvers import URLPattern 


# if settings.DEBUG:
#         URLPattern += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# import market
from market import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('main_info/', include('market.urls')),
    path('course_info', views.course_info,name='main_info'),
    path('dev_contact/', views.dev_contacts, name='dev_contact'),
    path('team_members/', views.team_members, name='team_members'),
    path('main', views.main_page, name='main_page'),
    path('login_page', views.login_page, name='login_page'),
    path('reg_page', views.reg_page, name='reg_page'),
    path('', include("django.contrib.auth.urls")),
    path('delivery_page', views.delivery_page, name="delivery_page"),
    path('profile_page', views.profile_page, name="profile_page"),
    path('catalogue_page', views.catalogue_page, name="catalogue_page"),
    path('create_product', views.create_prod, name='create_product'),
    path('<int:pk>', views.ProductsDetailed.as_view(), name='detail_prod'),
    path('<int:pk>/update', views.ProductsUpdate.as_view(), name='update_prod'),
    path('<int:pk>/delete', views.ProductsDelete.as_view(), name='del_prod'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)