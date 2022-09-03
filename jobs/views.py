from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from jobs.models import Job
from jobs.serializers import JobSerializer
from rest_framework.decorators import api_view

@api_view(['POST'])
def create_job(request):
    if request.method == 'POST':
        job_data = JSONParser().parse(request)
        print(job_data)
        job_serializer = JobSerializer(data=job_data)
        if job_serializer.is_valid():
            job_serializer.save()
            return JsonResponse(job_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(job_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_job(request, pk):
    try: 
        job = Job.objects.get(pk=pk) 
    except Job.DoesNotExist: 
        return JsonResponse({'message': 'The job does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        job_serializer = JobSerializer(job) 
        return JsonResponse(job_serializer.data)  

@api_view(['DELETE'])
def delete_job(request, pk):
    try: 
        job = Job.objects.get(pk=pk) 
    except Job.DoesNotExist: 
        return JsonResponse({'message': 'The job does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'DELETE':
        job.delete() 
        return JsonResponse({'message': 'Job was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)