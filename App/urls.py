from django.urls import path
from App import views


urlpatterns =[
    path('',views.home, name='home'),
    path('predict/',views.predict, name='predict'),
    path('predict-form/',views.pred_for, name='predict-form'),
    path('about/', views.about, name='about')
]
