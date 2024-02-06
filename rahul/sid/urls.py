from django.urls import path
from .views import QuoteListCreateAPIView, QuoteRetrieveUpdateDestroyAPIView, CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('sid/', QuoteListCreateAPIView.as_view(), name='quote-list'),
    path('sid/<int:pk>/', QuoteRetrieveUpdateDestroyAPIView.as_view(), name='quote-detail'),
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),
]
