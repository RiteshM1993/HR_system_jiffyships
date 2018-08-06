from hrms_employee.models import hremployee


from decimal import *
from datetime import datetime
from datetime import timedelta
#
#
#
class getcount:
    @classmethod
    def getcountdata(cls):
        try:
            empcountqry = hremployee.objects.count()

            data = {
                'empCount': empcountqry,

            }

            return data

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj
