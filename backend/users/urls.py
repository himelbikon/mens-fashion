from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', Registration.as_view()),
    path('email-confirmation/', EamailConfirmationAPIView.as_view()),

    path('subscribe/', Subscribe.as_view()),
    path('profile/', Profile.as_view()),
    # path('all/', AllUsers.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
