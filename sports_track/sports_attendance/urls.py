from django.urls import path
from . import views 
from .views import user_login, user_logout

urlpatterns = [
    
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path('', views.dashboard, name='dashboard'),  # Default to dashboard
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/update/<int:pk>/', views.student_update, name='student_update'),
    #path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),

    path('departments/', views.department_list, name='department_list'),
    path('departments/create/', views.department_create, name='department_create'),
    path('departments/update/<int:pk>/', views.department_update, name='department_update'),
    #path('departments/delete/<int:pk>/', views.department_delete, name='department_delete'),

    path('programmes/', views.programme_list, name='programme_list'),
    path('programmes/create/', views.programme_create, name='programme_create'),
    path('programmes/update/<int:pk>/', views.programme_update, name='programme_update'),
    #path('programmes/delete/<int:pk>/', views.programme_delete, name='programme_delete'),

    path('items/', views.item_list, name='item_list'),
    path('items/create/', views.item_create, name='item_create'),
    path('items/update/<int:pk>/', views.item_update, name='item_update'),
    
    #path('items/delete/<int:pk>/', views.item_delete, name='item_delete'),
]
