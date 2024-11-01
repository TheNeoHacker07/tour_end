from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Car(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    capacity = models.IntegerField(verbose_name='место')
    description = models.TextField(default='',verbose_name='описание')
    year = models.PositiveIntegerField(default=0000,verbose_name='год')
    wifi = models.BooleanField(default=False)
    car_style = models.CharField(max_length=50, default='sedan', verbose_name='стили')
    air_codinting = models.BooleanField(default=False,verbose_name= 'кондей')
   

    def __str__(self):
        return self.name


class ImageCar(models.Model):
    img = models.ImageField(upload_to='img', verbose_name='фото')
    car = models.ForeignKey(Car, related_name='car_img',on_delete=models.CASCADE,verbose_name='машина') 


    
class TourThemes(models.Model):
    group_themes = models.CharField(max_length=100,verbose_name='темы')  # Added max_length
    description = models.TextField(verbose_name='описание')  # Changed to TextField

    def __str__(self):
        return f"{self.group_themes}--{self.description[:8]}"


class TourType(models.Model):
    with_gid = models.BooleanField(verbose_name='с гидом')
    description = models.TextField(verbose_name='описание')  # Changed to TextField
    

    def __str__(self):
        return f'With Guide: {self.with_gid}'
    


class TourGroupDetail(models.Model):
    group_size = models.CharField(max_length=50,verbose_name='количество')  # Added max_length
    description = models.TextField(verbose_name='описание')  # Changed to TextField

    def __str__(self):
        return f'{self.group_size} - {self.description[:8]}'



class Country(models.Model):
    country = models.CharField(max_length=30, verbose_name='страна')

    def __str__(self):
        return self.country


class Region(models.Model):
    region = models.CharField(max_length=30, verbose_name='область')
    description = models.TextField(default='',verbose_name='описание')
    country =  models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.region


class Tour(models.Model):
    name = models.CharField(max_length=500, default='',verbose_name='имя')
    price = models.DecimalField(decimal_places=2,null=True, blank=True, max_digits=10,verbose_name='цена')
    # car = models.OneToOneField(Car, on_delete=models.CASCADE)
    
    is_active = models.BooleanField(default=False,verbose_name='активен')
    tour_type = models.ForeignKey(TourType, on_delete=models.CASCADE,verbose_name='тип тура')
    themes = models.ForeignKey(TourThemes, on_delete=models.CASCADE,verbose_name='тема')
    group_detail = models.ForeignKey(TourGroupDetail,on_delete=models.CASCADE,verbose_name='детали группы')
    start_date = models.DateTimeField(verbose_name='начало')
    end_date = models.DateTimeField(verbose_name='конец')
    description = models.TextField(default='',verbose_name='описание')
    region = models.ForeignKey(Region,verbose_name='регион' ,on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name} - {self.price}'
    


class Image(models.Model):
    image = models.ImageField(upload_to='img',verbose_name='фото')
    tour = models.ForeignKey(Tour, related_name='images',on_delete=models.CASCADE,verbose_name='туры')




class Booking(models.Model):
    first_name = models.CharField(max_length=20,default='',verbose_name='ФИО')
    description = models.TextField(max_length=1020,default='',verbose_name='описание')
    phone_number = models.CharField(default='',verbose_name='номер телефона')
    duration = models.IntegerField(default=1,verbose_name='количество')
    tour = models.ForeignKey(Tour, default=None, on_delete=models.CASCADE,verbose_name='тур')
    car = models.ForeignKey(Car, default=None,unique=False,on_delete=models.CASCADE,verbose_name='машина')
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.car}--{self.tour}'


class Review(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,related_name="review")
    email = models.EmailField(verbose_name='имейл')
    text = models.TextField(max_length=1000,verbose_name='текст')
    name = models.CharField(max_length=30,verbose_name='имя')
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    mark = models.PositiveIntegerField(choices=RATING_CHOICES,verbose_name='балл')

    def __str__(self):
        return f'{self.name}'
