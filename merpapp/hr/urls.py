from django.urls import path
from . import views
urlpatterns = [
    path('hr/',views.index,name='hr'),

]