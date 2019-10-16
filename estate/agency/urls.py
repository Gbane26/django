from django.urls import path
from agency import views
from rest_framework.routers import DefaultRouter
from .apiviews import CategorieViewSet, HouseViewSet, ArticleViewSet, LocationViewSet, Info_houseViewSet

router = DefaultRouter()
router.register('apicategory', CategorieViewSet, base_name='category')
router.register('apiagency', HouseViewSet, base_name='house')
router.register('apiarticle', ArticleViewSet, base_name='article')
router.register('apilocation', LocationViewSet, base_name='location')
router.register('apiinfohou', Info_houseViewSet, base_name='info_house')


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('news/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('developments/', views.developments, name="developments"),
    path('property', views.property, name="property"),
]

urlpatterns += router.urls