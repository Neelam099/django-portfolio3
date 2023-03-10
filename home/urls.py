from django.urls import path,include
from home  import views


urlpatterns = [
    path('',views.portfolio,name='portfolio'),
    path('djangoProjects',views.djangoProjects,name='djangoProjects'),
    path('contact/',views.contact,name='contact'),
]

