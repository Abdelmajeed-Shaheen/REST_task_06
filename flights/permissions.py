from rest_framework.permissions import BasePermission
from datetime import date


class BookingOwner(BasePermission):
	message = "must be the owner of this booking"

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.user == request.user):
			return True
		else:
			return False


class DateChangable(BasePermission):
	message = "you dont have a 3 days befor you trip"

	def has_object_permission(self, request, view, obj):
		days_left = (obj.date - date.today()).days
		if  days_left > 3:
			return True
		else:
			return False
