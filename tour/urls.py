from django.urls import path
from .views import CarList, CarRetrieve, TourList, TourRetrieve, BookingDelete, BookingCreate, BookingUpdate, CreateReview, DeleteReview, GetReview, UpdateReview, RetrieveReview, PlaceGet, PlaceGetList


urlpatterns = [
    path('car_list/', CarList.as_view()),
    path('car_retrieve/<int:pk>/', CarRetrieve.as_view()),
    path('tour_list/', TourList.as_view()),
    path('tour/<int:pk>/', TourRetrieve.as_view()),
    path('booking_create/', BookingCreate.as_view()),
    path('booking_delete/<int:pk>/', BookingDelete.as_view()),
    path('booking_update/<int:pk>/', BookingUpdate.as_view()),
    path('review_create/', CreateReview.as_view()),
    path('review_delete/<int:pk>/', DeleteReview.as_view()),
    path('get_review', GetReview.as_view()),
    path('update_delete/<int:pk>/', UpdateReview.as_view()),
    path('retrieve_review/<int:pk>/', RetrieveReview.as_view()),
    path('tour_place/',PlaceGet.as_view()),
    path('tour_place/<int:pk>/',PlaceGet.as_view())
]


