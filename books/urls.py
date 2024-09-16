from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.book_list_view),
    path('book_list/<int:id>/', views.book_detail_view),
]
