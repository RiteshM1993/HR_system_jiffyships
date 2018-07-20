from hrms_admin.models import customer_table
from bigchaindb_shared import api

class dmcustomermaster:
    @classmethod
    def saveCustomer(self, CustomerName,CustomerAddress,startDate,ContactPersonName,ContactPersonEmailid,active, created_by, created_date):
        try:
            saveqry = customer_table(customer_name=CustomerName,customer_address=CustomerAddress,start_date=startDate,contact_person_name=ContactPersonName,contact_person_emailid=ContactPersonEmailid,created_by=created_by,created_date=created_date,active=active)
            saveqry.save()
            saveqrysuccessobj = {
                'response': "success"
            }
            return saveqrysuccessobj
        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return {'failureobj': saveqryfailureobj}

    @classmethod
    def listcustomer(self):
        try:
            listqry = customer_table.objects.all()
            CustomerList = []

            for values in listqry:
                CustomerList.append({
                    'customer_id': values.customer_id,
                    'customer_name': values.customer_name,
                    'customer_address': values.customer_address,
                    'start_date': values.start_date,
                    'contact_person_name': values.contact_person_name,
                    'contact_person_emailid': values.contact_person_emailid,
                    'active': values.active

                })
            return CustomerList

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj


    @classmethod
    def geteditCustomer(cls, id):
        try:
            getqry = customer_table.objects.get(customer_id=id)
            dataobj = {
                'customer_id': getqry.customer_id,
                'customer_name':getqry.customer_name,
                'customer_address': getqry.customer_address,
                'start_date': getqry.start_date,
                'contact_person_name': getqry.contact_person_name,
                'contact_person_emailid': getqry.contact_person_emailid,
                'active': getqry.active
            }
            return dataobj
        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def updateCustomerMaster(self, id, customer_name,customer_address,start_date,contact_person_name,contact_person_emailid,active,updated_by,updated_date):
        try:
            getqry = customer_table.objects.get(customer_id=id)

            getqry.customer_name = customer_name
            getqry.customer_address = customer_address
            getqry.start_date = start_date
            getqry.contact_person_name = contact_person_name
            getqry.contact_person_emailid = contact_person_emailid
            getqry.active = active
            getqry.updated_by = updated_by
            getqry.updated_date = updated_date

            getqry.save()

            saveqrysuccessobj = {
                'response': "success"
            }
            return saveqrysuccessobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return {'failureobj': saveqryfailureobj}




