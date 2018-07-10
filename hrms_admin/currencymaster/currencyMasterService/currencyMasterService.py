from hrms_admin.models import currencymaster

class currencyMaster:
    @classmethod
    def addCurrency(cls, currencyname, currencylogo, created_date, created_by):
        try:
            saveqry = currencymaster(currency_name=currencyname, currency_logo=currencylogo, created_date=created_date, created_by=created_by)
            saveqry.save()

            saveqrysuccessobj = {
                'response': "success"
            }
            return saveqrysuccessobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    def listCurrency(self):
        try:
            getqry = currencymaster.objects.all()

            datalist = []

            for values in getqry:
                datalist.append({
                    'currency_id': values.currency_id,
                    'currency_name': values.currency_name,
                    'currency_logo': values.currency_logo,
                })

            return datalist

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    def deleteCurrency(self,id):
        try:
            delqry = currencymaster.objects.get(currency_id=id)

            delqry.delete()
            saveqrysuccessobj = {
                'response': "success"
            }
            return saveqrysuccessobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    def getCurrencyEditData(self,id):
        try:
            getqry = currencymaster.objects.get(currency_id=id)

            dataobj = {
                'currency_id': getqry.currency_id,
                'currency_name': getqry.currency_name,
                'currency_logo': getqry.currency_logo,
            }

            return dataobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    def updateCurrency(self, id, currencyname, currencylogo,updated_by,updated_date):
        try:
            getqry = currencymaster.objects.get(currency_id=id)
            getqry.currency_name = currencyname
            getqry.currency_logo = currencylogo
            getqry.updated_by = updated_by
            getqry.updated_date = updated_date

            getqry.save()

            saveqryobj = {
                'response': "success"
            }
            return saveqryobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj
