from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
from .serializer import StudentSerializer

# use auth login from django

from .models import Student

@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            studentId = data.get('studentId')
            password = data.get('password')
            print("After data")
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        try:
            student = Student.objects.get(studentId=studentId)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Invalid ID'}, status=400)

        if password == student.password:
            student_serializer = StudentSerializer(student)
            return JsonResponse(student_serializer.data, status=200)
        else:
            return JsonResponse({'error': 'Invalid password'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
@require_http_methods(["POST"])
def signup(request):
    try:
        data = json.loads(request.body)
        student_id = data['studentId']
        studentName = data['name']
        password = data['password']

        if Student.objects.filter(studentId=student_id).exists():
            return JsonResponse({"error": "Student ID already exists"}, status=400)

        # Create and save the new student
        student = Student(
            studentId=student_id,
            name=studentName ,  # Assuming name is not provided in the request
            password=password  # Save the password as plain text (not recommended)
        )
        student.save()

        return JsonResponse({"message": "Sign up successful"}, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    