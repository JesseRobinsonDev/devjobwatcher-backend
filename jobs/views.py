from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from jobs.models import Job
from jobs.serializers import JobSerializer
from rest_framework.decorators import api_view
from django.db.models import Q

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

@api_view(['GET'])
def search_jobs(request):
    tags = ['react', 'javascript', 'nodejs']
    if request.method == 'GET':
        limit = int(request.GET.get('limit')) if type(request.GET.get('limit')) == type('') else 10
        offset = int(request.GET.get('offset')) if type(request.GET.get('offset')) == type('') else 0
        salaryMin = int(request.GET.get('salaryMin')) if type(request.GET.get('salaryMin')) == type('') else 0
        salaryMax = int(request.GET.get('salaryMax')) if type(request.GET.get('salaryMax')) == type('') else 1000000
        technologies = request.GET.get('technologies').split(',') if type(request.GET.get('technologies')) == type('') else []
        levels = request.GET.get('levels').split(',') if type(request.GET.get('levels')) == type('') else []
        industries = request.GET.get('industries').split(',') if type(request.GET.get('industries')) == type('') else []
        types = request.GET.get('types').split(',') if type(request.GET.get('types')) == type('') else []
        q_objects = Q()
        q_technologies = Q()
        for t in technologies:
            q_technologies &= Q(jobTechnologies__contains=t)
        q_objects &= q_technologies
        q_levels = Q()
        for l in levels:
            q_levels |= Q(jobLevel=l)
        q_objects &= q_levels
        q_industries = Q()
        for i in industries:
            q_industries |= Q(jobIndustry__contains=i)
        q_objects &= q_industries
        q_types = Q()
        for t in types:
            q_types |= Q(jobType__contains=t)
        q_objects &= q_types
        q_salary = Q()
        q_salary &= Q(jobSalaryLow__gte=salaryMin)
        q_salary &= Q(jobSalaryLow__lte=salaryMax)
        q_objects &= q_salary
        jobs = Job.objects.filter(q_objects)[offset:(offset + limit)]
        job_serializer = JobSerializer(jobs, many=True)
        return JsonResponse(job_serializer.data, safe=False)
