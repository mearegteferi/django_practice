from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale
from django.db import connection
from django.utils import timezone
from pprint import pprint


def run():

    # restaurant = Restaurant()
    # restaurant.name = 'Mekelle cafe'
    # restaurant.latitude = 50.3
    # restaurant.longitude = 50.2
    # restaurant.date_opened = timezone.now()
    # restaurant.restaurant_type = restaurant.TypeChoices.OTHER
    # restaurant.save()

    # Restaurant.objects.create(
    #     name='Wukro Cafe',
    #     date_opened=timezone.now(),
    #     latitude=60.2,
    #     longitude=60.3,
    #     restaurant_type=Restaurant.TypeChoices.ITALIAN
    # )

    # restaurant = Restaurant.objects.count()
    # print(restaurant)
    # print(connection.queries)

    # user = User.objects.first()
    # restaurant = Restaurant.objects.all()[1]
    # Rating.objects.create(user=user, restaurant=restaurant, rating=10)

    # ratings = Rating.objects.filter(rating=6)
    # print(ratings)

    # ratings = Rating.objects.exclude(rating__lt=6)
    # print(ratings)

    # restaurant = Restaurant.objects.last()
    # print(restaurant)

    # restaurant.name = 'Agulae Cafe'
    # restaurant.save()
    # pprint(connection.queries)

    # rating = Rating.objects.first()
    # print(rating.restaurant)
    # pprint(connection.queries)

    # Sale.objects.create(
    #     restaurant=Restaurant.objects.first(),
    #     income=150.00,
    #     datetime=timezone.now()
    # )

    # restaurant = Restaurant.objects.first()
    # print(restaurant.sales.all())
    
    # restaurant = Restaurant.objects.first()
    # restaurant.name = 'Shire Cafe'
    # restaurant.save()

    # user = User.objects.first()
    # restaurant = Restaurant.objects.first()

    # print(Rating.objects.get_or_create(
    #     user=user,
    #     restaurant=restaurant,
    #     rating=3
    # ))

    # restaurant1 = Restaurant.objects.first()
    # restaurant.name = 'Axum Cafe'
    # restaurant.save()

    # restaurant1.latitude = 70.2
    # restaurant1.save(update_fields=['latitude'])

    # restaurant = Restaurant.objects.all()
    # restaurant.update(date_opened=timezone.now())

    restaurant = Restaurant.objects.filter()
    res
    pprint(connection.queries)
