from django.db import models
from datetime import datetime
from authapp.models import User
from django.utils import timezone
class Rider(models.Model):
    TravelMediumType = models.TextChoices('TravelMedium', 'BUS CAR TRAIN')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="rider_user")
    from_location = models.CharField(max_length=200,blank=False)
    to_location = models.CharField(max_length=200,blank=False)
    datetime = models.DateTimeField(blank=False)
    is_flexible = models.BooleanField(default=True)
    travel_medium = models.CharField(blank=False, choices=TravelMediumType.choices, max_length=10)
    quantity_of_assets = models.IntegerField(default=1)

    def __str__(self):
        return f'Req id {self.id} =====  {self.from_location} | {self.to_location} | {self.datetime}==== User id {self.user.id}'



class Requester(models.Model):
    AssetType = models.TextChoices('AssetType', 'LAPTOP TRAVEL_BAG PACKAGE')
    AssetSensitivityType = models.TextChoices('AssetSensitivityType', 'HIGHLY_SENSITIVE SENSITIVE NORMAL')
    StatusType = models.TextChoices('StatusType', 'PENDING EXPIRED')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="requester_user")
    from_location = models.CharField(max_length=200,blank=False)
    to_location = models.CharField(max_length=200,blank=False)
    date_time = models.DateTimeField(blank=False)
    is_flexible = models.BooleanField(default=True)
    quantity_of_assets = models.IntegerField(default=1)
    asset_type = models.CharField(blank=False, choices=AssetType.choices, max_length=10)
    asset_sensitivity = models.CharField(blank=False, choices=AssetSensitivityType.choices, max_length=20)
    deliver_to = models.CharField(max_length=200,blank=True,default=None)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE,related_name="rider",blank=True,null=True)
    

    @property
    def status(self) -> StatusType:
        if timezone.now() > self.date_time:
            return "EXPIRED"
        else:
            return "PENDING"

    

    def __str__(self):
        return f'Req id {self.id} ===== Name {self.user.first_name} ==== User id {self.user.id}'
    