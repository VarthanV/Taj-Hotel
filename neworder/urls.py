from django.urls import path
from .import views
urlpatterns = [
    path('items/', views.ItemView.as_view()),
    path('order/', views.OrderView.as_view()),
    path('customers/',views.CustomerSearchView.as_view()),
    path('daily/',views.DailyItemView.as_view()),
<<<<<<< HEAD
    path('subitems/',views.SubItemsView.as_view()),
    path('orderid/',views.OrderByIdView.as_view())
=======
    path('subitems/',views.SubItemsView.as_view())
>>>>>>> c27b0082056f4046bfd20335d73aae5a0e201635
]
