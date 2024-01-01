from django.urls import path
from . import views as vw
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('branchform/', login_required(vw.BranchFormView.as_view()), name='branchform'),
    path('updatebranch/<int:pk>', login_required(vw.BranchUpdateview.as_view()), name='updatebranch'),
    path('deletebranch/<int:pk>', login_required(vw.BranchDeleteView.as_view()), name='deletebranch'),
]