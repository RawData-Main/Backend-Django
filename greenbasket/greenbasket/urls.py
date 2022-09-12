"""greenbasket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django .conf .urls.static import static
from django.urls import path
from django.urls import include
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


# User.objects.get(username='report_user')
# # current_user = request.user
# print(u)
# if str(u) == 'report_user':
# # if current_user.username == 'report_user':
#     admin.site.site_header = "Green Basket Report User"
#     admin.site.site_title = "Report User Portal"
#     admin.site.index_title = "Welcome to Green Basket Reports"

# def sample_view(request):
#     current_user = request.user
#     if current_user.username == 'report_user':
#         admin.site.site_header = "Green Basket Report User"
#         admin.site.site_title = "Report User Portal"
#         admin.site.index_title = "Welcome to Green Basket Reports"
#     else:
#         admin.site.site_header = "Green Basket Admin"
#         admin.site.site_title = "Green Basket Admin Portal"
#         admin.site.index_title = "Welcome to Green Basket Portal"
admin.site.site_header = "Green Basket Admin"
admin.site.site_title = "Green Basket Admin Portal"
admin.site.index_title = "Welcome to Green Basket Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('master/', include('master.urls')),
    path('product/', include('product.api.urls')),
    path('user/', include('user.api.urls')),
    path('cart/', include('cart.urls')),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
