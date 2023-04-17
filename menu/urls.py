from django.urls import path

from menu.views import HomeView

urlpatterns = [
    path('', HomeView.as_view())
]

# Show as example
urlpatterns += [
    path('dashboard/', HomeView.as_view(), name='dashboard'),
    path('dashboard/profile/', HomeView.as_view(), name='profile'),
    path('dashboard/summary/', HomeView.as_view()),
    path('employees/', HomeView.as_view()),
    path('employees/staff/', HomeView.as_view(), name='staff'),
    path('employees/cashier/', HomeView.as_view()),
    path('employees/staff/terminals/', HomeView.as_view())
]
