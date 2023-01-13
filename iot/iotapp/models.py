from django.db import models

# Create your models here.

class Category(models.Model):
    #Id не надо, он уже сам появиться
    name = models.CharField(max_length= 16, unique=True)
    description = models.TextField(blank= True)
    '''
    # Основные типы полей
    # data
    models.DateField
    models.DateTimeField
    models.TimeField
    # число
    models.IntegerField
    models.PositiveIntegerField
    models.PositiveSmallIntegerField
    models.FloatField
    models.DecimalField
    # логический
    models.BooleanField
    # Байты
    models.BinaryField
    # Картинка
    models.ImageField
    # Файл
    models.FileField
    # Url, email
    models.URLField
    models.EmailField
    '''
    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length= 32, unique= True)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now= True)
    # Связь с категорией
    # один ко многим
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    # Связь с тегами
    # многим ко многим
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

class Good(models.Model):
    name = models.CharField(max_length=32, unique=True)
    def __str__(self):
        return self.name
#название магазина
class Shop(models.Model):
    #Id не надо, он уже сам появиться
    name = models.CharField(max_length= 32, unique=True)
    def __str__(self):
        return self.name
class Merchandise(models.Model):
    good = models.CharField(max_length= 32)
    name = models.TextField()
    imageUrl = models.URLField()
    priceBefore = models.FloatField()
    priceAfter = models.FloatField()
    amount = models.FloatField()
    discount = models.IntegerField()
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    market_name = models.CharField(max_length= 32)
    # Связь с категорией
    # один ко многим
    market = models.ForeignKey(Shop, on_delete= models.CASCADE)
    def __str__(self):
        return ("{0:2d}% скидка в магазине {1} на товар: {2}.".format(self.discount, self.market_name, self.name))

class Building(models.Model):
    name = models.TextField()
    address = models.TextField()
    disabled = models.BooleanField()
    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Room(models.Model):
    name = models.TextField()
    mqttPath = models.TextField()
    disabled = models.BooleanField()
    createdAt = models.DateTimeField(auto_now_add=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class DeviceType(models.Model):
    name = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Plan(models.Model):
    name = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Device(models.Model):
    name = models.TextField()
    mqttPath = models.TextField()
    positionX = models.FloatField()
    positionY = models.FloatField()
    enabled = models.BooleanField()
    createdAt = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    '''class Meta:
        db_table = "devices"'''
class Data(models.Model):
    name = models.TextField()
    value = models.FloatField()
    createdAt = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    def __str__(self):
        return ("{0:5.2f} ед. на датчике : {1} - {2}".format(self.value , self.name, self.createdAt))
class User(models.Model):
    name = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name





