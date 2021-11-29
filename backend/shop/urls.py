from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('latest/<int:limit>/<int:page>/', LatestProducts.as_view()),
    path('popular/<int:limit>/<int:page>/', PopularProducts.as_view()),
    path('<int:pk>/', SingleProduct.as_view()),

    path('categories/', Categories.as_view()),
    path('showcases/', Showcases.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
