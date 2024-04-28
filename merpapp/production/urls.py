from django.urls import path
from . import views
urlpatterns = [
    path('production/',views.index,name='production'),

]