from django.urls import path
from . import views
app_name='facebookhome'

urlpatterns = [
    path('',views.homepage ),
    path('signup',views.signup, name='signup'),
    path('page',views.page name='page'),

  

    
]
