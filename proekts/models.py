# import uuid
#
# from django.db import models
# from users.models import User
#
#
# class Balance(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=15, default=0, decimal_places=3)
#     updated_at = models.DateTimeField(auto_now=True)
#
#
# class Category(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.name
#
#
# class Transaction(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     balance = models.ForeignKey(Balance, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=15, default=0, decimal_places=3)
#     created_at = models.DateTimeField(auto_now_add=True)
