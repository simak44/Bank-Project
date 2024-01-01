from django.contrib.auth.decorators import login_required
from . import views
from django.urls import path


urlpatterns = [
    path('updatebank/<int:pk>', login_required(views.BankUpdateview.as_view()), name='updatebank'),
    path('deletebank/<int:pk>', login_required(views.BankDeleteView.as_view()), name='deletebank'),
    path('banks/', login_required(views.BankFormView.as_view()), name='banks'),
]