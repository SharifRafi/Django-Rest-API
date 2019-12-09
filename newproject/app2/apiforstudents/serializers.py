from rest_framework import serializers
from app2.models import student
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
#from books.models import Book
#from books.apibooks.serializers import BookSerializer

class StudentUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = student
		fields = ('pk','student_name', 'department', 'contact')

class StudentSerializer(serializers.ModelSerializer):
	#personalinfo = BookSerializer(many=True)
	class Meta:
		model = student
		fields = ('pk','student_name', 'department', 'contact')

class  StudentCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = student
		fields = ('student_name', 'department', 'contact')

	def save(self):
		try:
			student_name      = self.validated_data['student_name']
			department        = self.validated_data['department']
			contact           = self.validated_data['contact']

			studentinfo = student(
								student_name=student_name,
								department=department,
								contact=contact
								)
			studentinfo.save()
			return studentinfo
		except KeyError:
			raise serializers.ValidationError({"response": "this invalid somethings!!!!!"})
