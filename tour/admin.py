from django.contrib import admin
from .models import Booking, Car, Review, Tour, TourGroupDetail, TourThemes, TourType, Image, ImageCar

admin.site.register(Booking)
admin.site.register(Car)
admin.site.register(Tour)
admin.site.register(Review)
admin.site.register(TourGroupDetail)
admin.site.register(TourThemes)
admin.site.register(TourType)
admin.site.register(Image)
admin.site.register(ImageCar)