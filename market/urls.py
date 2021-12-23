from django.conf.urls import include
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static 


# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('course_info', views.course_info, name='course_info'),
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