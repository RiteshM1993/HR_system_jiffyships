from hrms_admin.models import purchase_order

from hrms_admin.models import po_payment
from decimal import Decimal


class purchaseOrder:

    @classmethod
    def savePo(self, projectName,purchaseOrderNumber,startDate,endDate,purchaseOrderAmount,purchaseordercurrency,createdby,createdDate):
        try:
            saveqry = purchase_order(project_id=projectName,po_number=purchaseOrderNumber,po_start_date=startDate,po_end_date=endDate,po_amount = purchaseOrderAmount,po_currency_id=purchaseordercurrency,created_date=createdDate,created_by=createdby)

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
    def listpo(cls):
        try:
            listqry = purchase_order.objects.raw('select a.po_amount,a.po_id,a.project_id,a.po_number, b.customer_id ,b.project_name,c.customer_name,d.currency_name,d.currency_logo from purchase_order a inner join project_master b on a.project_id = b.project_id inner join customer_table c on b.customer_id = c.customer_id  inner join currency_master d on d.currency_id = a.po_currency_id')
            datalist = []
            for values in listqry:
                datalist.append({
                    'po_amount': values.currency_logo +' '+values.po_amount,
                    'po_id': values.po_id,
                    'po_number': values.po_number,
                    'po_start_date': values.po_start_date,
                    'po_end_date': values.po_end_date,
                    'project_name': values.project_name,
                    'currency_name': values.currency_name,
                    'customer_id': values.project_name + " (" + (values.customer_name)+")",
                })
            return datalist

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def delpo(cls, id):
        try:
            delqry = purchase_order.objects.get(po_id=id)
            delqry.delete()
            successobj = {
                'successmsg': "success",
            }
            return successobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def getEditData(cls, id):
        try:

            getqry = purchase_order.objects.raw(
                'select a.po_amount,a.po_id,a.project_id,a.po_number, b.customer_id ,b.project_name,c.customer_name,d.currency_name from purchase_order a inner join project_master b on a.project_id = b.project_id inner join customer_table c on b.customer_id = c.customer_id  inner join currency_master d on d.currency_id = a.po_currency_id where a.po_id='+id)
            for data in getqry:
                dataobj = {
                    'project_id': data.project_id,
                    'customer_id': data.project_name + " (" + (data.customer_name) + ")",
                    'po_amount': int(data.po_amount),
                    # 'po_project_cost': float(data.po_project_cost),
                    # 'po_billing_per_hour': data.po_billing_per_hour,
                    'po_id': data.po_id,
                    'po_number': data.po_number,
                    'po_start_date': data.po_start_date,
                    'po_end_date': data.po_end_date,
                    # 'po_resource_count': data.po_resource_count,
                    'project_name': data.project_name,
                    # 'project_type_name': data.project_type_name,
                    'currency_name': data.currency_name,
                    # 'po_billing_type': data.po_billing_type,
                    'po_currency_id': data.po_currency_id,

                }

            return dataobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def updatePo(cls,id,projectId,poNumber,startDate,endDate,poAmount,currencyId,updated_by,updated_date):
        try:
            updateqry = purchase_order.objects.get(po_id=id)

            updateqry.project_id=projectId
            updateqry.po_number=poNumber
            updateqry.po_start_date=startDate
            updateqry.po_end_date=endDate
            # updateqry.po_resource_count=resourceCount
            # updateqry.po_billing_type=billingType
            updateqry.po_amount=poAmount
            # updateqry.po_billing_per_hour=billperhour
            # updateqry.po_project_cost=projectCost
            updateqry.po_currency_id = currencyId
            updateqry.updated_by = updated_by
            updateqry.updated_date= updated_date

            updateqry.save()

            dataobj = {'data': 'success'}

            return dataobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def savepopayment(cls,id,CheckTransactionDetails,receiveddate,Description,createdby,createdDate):
        try:
            saveqry = po_payment(po_id=id, cheque_tnx_no=CheckTransactionDetails, description=Description,received_date=receiveddate, created_date=createdDate, created_by=createdby)

            saveqry.save()

            po_status_change = purchase_order.objects.get(po_id=id)
            po_status_change.payment_received_flag=1
            po_status_change.save()

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
    def getpopayment(cls):
        try:
            listqry=po_payment.objects.all()
            ListpoPayment=[]

            for values in listqry:
                ListpoPayment.append({

                    'paymentId':values.payment_id,
                    'poId':values.po_id,
                    'receivedDate':values.received_date,
                    'chequetransno':values.cheque_tnx_no,
                    'description':values.description,
                })

            return ListpoPayment

        except Exception, err:
            saveqryfailureobj = {

                'response':'Failure'

            }
            return {'failureobj':saveqryfailureobj}









