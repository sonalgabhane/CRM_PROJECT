import django_filters
from .models import Lead
class LeadFilter(django_filters.FilterSet):
    
    class Meta:
        model = Lead
        fields = {'leadno':['exact'],'priority':['exact'],'status':['exact'],'assigned':['exact'],'firstname':['exact'],
                  'lastname':['exact'],'email':['exact'],'number':['exact'],'tags':['exact']}
        