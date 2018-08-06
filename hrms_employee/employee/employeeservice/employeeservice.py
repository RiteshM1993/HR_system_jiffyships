
from hrms_employee.models import hremployee

from django.core.files.storage import FileSystemStorage
from datetime import datetime


class dmemployee:
    @classmethod
    def saveEmployee(self,firstName, middleName,lastName, email, empmobnum,empcurrentaddr,empexperience, empperaddr,dmempid, myfile, empRole,created_date,created_by):

        try:
            if middleName == 'undefined':
                middleName = None

            saveqry=hremployee(first_name=firstName, middle_name=middleName,last_name=lastName, email_id=email, mobile_number=empmobnum,address=empcurrentaddr,year_exp=empexperience, permanent_address=empperaddr,employee_no=dmempid,emp_image= myfile, emp_role=empRole,created_date=created_date,created_by=created_by)

            saveqry.save()

            fs = FileSystemStorage()

            filename = fs.save(myfile.name, myfile)

            uploaded_file_url = fs.url(filename)

            saveqrysuccessobj = {
                'response': "success",
                'url' : uploaded_file_url,
            }
            return saveqrysuccessobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return {'failureobj': saveqryfailureobj}

    @classmethod
    def listEmployee(self):
        try:
            listqry = hremployee.objects.all()
            employeeList = []

            for values in listqry:
                employeeList.append({
                    'emp_id' : values.emp_id,
                    'emp_name' : ' 'if values.middle_name is 'Null' else ' '.join(filter(None, (values.first_name, values.middle_name, values.last_name))),
                    'employee_id': values.employee_no,
                    'mobile_number' : values.mobile_number,
                    'emp_email' : values.email_id,
                    'emp_curr_addr' : values.address,
                    'emp_per_addr' : values.permanent_address,
                    'year_exp' : values.year_exp,
                    'empImg' : values.emp_image,
                })
            return employeeList

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def delEmployee(self,id):
        try:
            delqry = hremployee.objects.get(emp_id=id)
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
    def geteditEmployeedata(cls,id):
        try:
            getqry = hremployee.objects.get(emp_id=id)

            dataobj = {
                    'emp_id' : getqry.emp_id,
                    'first_name' : getqry.first_name,
                    'middle_name': getqry.middle_name,
                    'last_name' : getqry.last_name,
                    'mobile_number':int(getqry.mobile_number),
                    'emp_email' : getqry.email_id,
                    'emp_curr_addr' : getqry.address,
                    'emp_per_addr' : getqry.permanent_address,
                    'year_exp' : getqry.year_exp,
                    'EmpId' : getqry.employee_no,
                    'emp_image' : getqry.emp_image,
                    'emp_role' : getqry.emp_role,
            }
            return dataobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def updateEmployee(self, id,empFirstName, empMiddleName, empLastName, empEmail,empMobNum,experience,empCurrAddr, empPermaAddr, myfile,empRole,updated_date,updated_by):
        try:

            getqry = hremployee.objects.get(emp_id=id)

            getqry.email_id = empEmail
            getqry.mobile_number = empMobNum
            getqry.year_exp = experience
            getqry.first_name = empFirstName
            getqry.middle_name = '' if empMiddleName is None else empMiddleName
            getqry.last_name = empLastName
            getqry.address = empCurrAddr
            getqry.permanent_address = empPermaAddr
            getqry.emp_role = empRole
            getqry.updated_date = updated_date
            getqry.updated_by = updated_by

            uploaded_file_url = ''

            if myfile != '':
                getqry.emp_image = myfile.name

                fs = FileSystemStorage()

                filename = fs.save(myfile.name, myfile)

                uploaded_file_url = fs.url(filename)

            getqry.save()

            saveqrysuccessobj = {
                'response': "success",
                'url': uploaded_file_url,
            }

            return saveqrysuccessobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return {'failureobj': saveqryfailureobj}






    @classmethod
    def empManagerName(cls, name):
        try:
            name_str = name
            employeeList = []
            if ' ' in name_str:
                name_str = name_str.replace(' ', '%%')
                listqry = employee.objects.raw("Select emp_id, email_id,CONCAT(first_name,' ',middle_name,' ',last_name) as employee_name from employee where lower( CONCAT(first_name,' ',middle_name,' ',last_name)) like '%%"+name_str+"%%'")

            else:
                listqry = employee.objects.raw("Select emp_id, email_id,CONCAT(first_name,' ',middle_name,' ',last_name) as employee_name from employee where lower( CONCAT(first_name,' ',middle_name,' ',last_name)) like  '%%" +name_str+"%%'")


            for values in listqry:
                employeeList.append({
                    "emp_name": values.employee_name,
                    "emp_id": values.emp_id,
                    "email_id": values.email_id,
                })

            return employeeList

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj


