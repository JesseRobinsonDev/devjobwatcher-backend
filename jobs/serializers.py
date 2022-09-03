from rest_framework import serializers 
from jobs.models import Job
 
 
class JobSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    jobTitle = serializers.CharField()
    jobBody = serializers.CharField()
    jobCompany = serializers.CharField()
    jobType = serializers.ListField()
    jobLevel = serializers.CharField()
    jobIndustry = serializers.ListField()
    jobSalaryLow = serializers.IntegerField()
    jobSalaryHigh = serializers.IntegerField()
    jobSalaryFrequency = serializers.CharField()
    jobRemote = serializers.BooleanField()
    jobTechnologies = serializers.ListField()
    jobLink = serializers.CharField()
    jobSiteID = serializers.CharField()

    def create(self, validated_data):
        return Job.objects.create(**validated_data)