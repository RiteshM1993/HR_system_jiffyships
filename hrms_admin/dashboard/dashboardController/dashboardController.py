import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
import time
from hrms_admin.dashboard.dashboardService.dashboardService import getcount
#
#
@api_view(['GET'])
def fetchDashboardValues(request):
    get_count = getcount()

    result = get_count.getcountdata()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

#
