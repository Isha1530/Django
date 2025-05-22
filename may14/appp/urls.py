from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('table/', views.table, name='table'),
    path('student/',views.student_data, name='student_view'),
]
