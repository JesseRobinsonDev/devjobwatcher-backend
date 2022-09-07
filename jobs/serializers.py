from rest_framework import serializers 
from jobs.models import Job
 
 
class JobSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    jobTitle = serializers.CharField()
    jobBody = serializers.CharField()
    jobCompany = serializers.CharField()
    jobType = serializers.ListField(allow_null=True)
    jobLevel = serializers.CharField(allow_blank=True, allow_null=True)
    jobIndustry = serializers.ListField(allow_null=True)
    jobSalaryLow = serializers.IntegerField(allow_null=True)
    jobSalaryHigh = serializers.IntegerField(allow_null=True)
    jobSalaryFrequency = serializers.CharField(allow_blank=True, allow_null=True)
    jobRemote = serializers.BooleanField(allow_null=True)
    jobTechnologies = serializers.ListField(allow_null=True)
    jobLink = serializers.CharField()
    jobSiteID = serializers.CharField()

    def create(self, validated_data):
        return Job.objects.create(**validated_data)