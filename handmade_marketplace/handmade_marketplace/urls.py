# from django.contrib import admin
# from django.urls import path, include  # Import include

# urlpatterns = [
#     path('admin/', admin.site.urls),  # Admin panel
#     path('', include('marketplace.urls')),  # Include your app’s urls
# ]
from django.contrib import admin
from django.urls import path, include
from marketplace.views import home 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('marketplace.urls')), 
    # path('', include('accounts.urls')), # This ensures '/' goes to marketplace.urls
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')), 
    path("", home, name="home"),

]
# from django.contrib import admin
# from django.urls import path, include
# from marketplace.views import home  # Import home view

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("accounts/", include("accounts.urls")),  # Include login and register URLs
#     path("", home, name="home"),  # Home page URL
# ]
