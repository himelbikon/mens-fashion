from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('products', ProductsOrderBy.as_view()),
    path('products/<int:pk>/', SingleProduct.as_view()),

    path('categories/', Categories.as_view()),
    path('showcases/', Showcases.as_view()),

    path('orders/', OrdersView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
