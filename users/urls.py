from users.controllers import user_views
from users.controllers import expense_views

from django.urls import path

app_name = 'user_section'


user_urlpatterns = [
    path('user/', user_views.UserListAPIView.as_view(), name='user-list'),
    path('user/create/', user_views.UserCreateAPIView.as_view(), name='user-create'),
    path('user/update/<int:pk>/', user_views.UserUpdateAPIView.as_view(), name='user-update'),
    path('user/destroy/<int:pk>', user_views.UserDestroyAPIView.as_view(), name='user-destroy'),
    path('user/<int:pk>', user_views.UserRetrieveAPIView.as_view(), name='user-get'),
]


expense_urlpatterns = [
    path('expense/', expense_views.ExpenseListAPIView.as_view(), name='expense-list'),
    path('expense/by-date-range/', expense_views.ExpenseByDateRangeAPIView.as_view(), name='expense-by-date-range'),
    path('expense/summary/', expense_views.ExpenseSummaryAPIView.as_view(), name='expense-summary'),
    path('expense/create/', expense_views.ExpenseCreateAPIView.as_view(), name='expense-create'),
    path('expense/update/<int:pk>/', expense_views.ExpenseUpdateAPIView.as_view(), name='expense-update'),
    path('expense/destroy/<int:pk>', expense_views.ExpenseDestroyAPIView.as_view(), name='expense-destroy'),
    path('expense/<int:pk>', expense_views.ExpenseRetrieveAPIView.as_view(), name='expense-get'),
]

urlpatterns = user_urlpatterns + expense_urlpatterns
