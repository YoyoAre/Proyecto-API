from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('agregar/<str:nombre>',views.agregar,name='agregar'),
    path('actualiza/<int:id>/<str:nombre>',views.actualiza,name='actualiza'),
]