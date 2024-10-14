from rest_framework import serializers
from .models import Tour, Car, Booking, Review, Image, ImageCar, TourGroupDetail, TourThemes, TourType, Country, Region


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
       model = Image
       fields = ['id', 'image']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    class Meta:
        model = Region
        fields = '__all__'


class TourGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourGroupDetail
        fields = '__all__'

class TourTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourType
        fields = '__all__'

class TourThemesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourThemes
        fields = '__all__'

class TourSerializer(serializers.ModelSerializer):
    tour_type = TourTypeSerializer()  # Вложенный сериализатор
    group_detail = TourGroupSerializer() 
    themes = TourThemesSerializer()
    images = ImageSerializer(many=True, read_only=True)  # Поле должно называться "images", как в модели
    region = RegionSerializer(read_only=True)
    
    class Meta:
        model = Tour
        fields = '__all__'



class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCar
        fields = '__all__'  


class CarSerializer(serializers.ModelSerializer):
    car_img = CarImageSerializer(many=True, read_only=True)
    class Meta:
        model = Car
        fields = '__all__'        

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    

class ReviewSerializer(serializers.ModelSerializer):
    booked_at = serializers.DateTimeField(read_only=True) 

    class Meta:
        model = Review
        fields = '__all__'
   
    def create(self, validated_data):
        validated_data['author']=self.context['request'].user
        post=super().create(validated_data)
        post.save()
        return post

