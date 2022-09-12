from django.urls import path
from .views import *
# (CustomerSignupView,
# ReportUserSignupView,
# CustomAuthToken, LogoutView, CustomerOnlyView, ReportUserOnlyView)
from user.api import views

urlpatterns=[
    path('signup/report-user/', ReportUserSignupView.as_view()),
    path('signup/customer/', CustomerSignupView.as_view()),
    path('login/',CustomAuthToken.as_view(), name='auth-token'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('logout/', views.LogoutView, name='logout-view'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    # path('logout/', views.LogoutView, name='logout-view'),
    # path('logout/', LogoutView.as_view(), name='logout')
    path('report-user/dashboard/', ReportUserOnlyView.as_view(), name='report-user-dashboard'),
    path('customer/dashboard/', CustomerOnlyView.as_view(), name='coustomer-dashboard'),
]