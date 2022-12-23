from django.contrib import admin

from .models import Category, Post, Tag, Good, Shop, Merchandise,\
    Device, Building, Room, DeviceType, Plan, Data

#admin.site.register(Category)
#admin.site.register(Post)
#admin.site.register(Tag)
#admin.site.register(Good)
#admin.site.register(Shop)
#admin.site.register(Merchandise)
admin.site.register(Building)
admin.site.register(Room)
admin.site.register(DeviceType)
admin.site.register(Plan)
admin.site.register(Device)
admin.site.register(Data)

