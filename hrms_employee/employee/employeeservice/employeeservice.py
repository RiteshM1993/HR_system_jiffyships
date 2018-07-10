from hrms_employee.models import employee
from hrms_admin.businessunitmaster.businessUnitMasterService.businessUnitMasterService import businessUnitMaster
from hrms_admin.designationmaster.designationmasterservice.designationmasterservice import dmdesignation
from hrms_admin.officelocation.officeLocationService.officeLocationService import officeLocation
from hrms_admin.models import designationmaster
from hrms_employee.models import employee_project
from hrms_employee.models import employee_designationpackagehistory
from django.core.files.storage import FileSystemStorage
from datetime import datetime


class dmemployee:
    @classmethod
    def saveEmployee(self, firstName, middleName, lastName, email, personalemail, empmobnum,
                      empdob, empstatus, empjobtitle, empDoj, empofficeno, empisactive,
                      empexperience, empbusinessunit, empofficelocation, empcurrentaddr,
                      empperaddr, empmanager, dmempid,myfile,empRole,created_date,created_by):
        try:
            if middleName == 'undefined':
                middleName = None
            if empofficeno == 'null' or empofficeno == 'undefined':
                empofficeno = None
            if empmanager == 'undefined':
                empmanager = None


            saveqry = employee(email_id=email, date_of_joining=empDoj, status_id=empstatus,
                               jobtitle_id=empjobtitle, mobile_number=empmobnum, office_number=empofficeno,
                               isactive=empisactive, year_exp=empexperience, businessunit_id=empbusinessunit,
                               created_date=created_date, personal_email=personalemail, first_name=firstName,
                               middle_name=middleName, last_name=lastName,
                               birth_date=empdob, address=empcurrentaddr, permanent_address=empperaddr,
                               office_location_id=empofficelocation, manager_id=empmanager,
                               created_by=created_by, emp_dm_id=dmempid, emp_image=myfile.name, emp_role=empRole)

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
            listqry = employee.objects.raw('Select a.emp_image,a.emp_id,a.email_id,a.date_of_joining,a.date_of_leaving,a.status_id,a.jobtitle_id,a.mobile_number,a.created_by,a.office_number,a.isactive,a.year_exp, a.businessunit_id,a.personal_email, a.first_name, a.middle_name, a.last_name, a.birth_date, a.address, a.permanent_address,a.office_location_id,a.emp_dm_id, b.first_name as manager_first_name, b.middle_name as manager_middle_name, b.last_name as manager_last_name, a.manager_id from employee a left join employee b on a.manager_id = b.emp_id')
            employeeList = []

            for values in listqry:
                employeeList.append({
                    'emp_id' : values.emp_id,
                    'emp_name' : ' 'if values.middle_name is 'Null' else  ' '.join(filter(None, (values.first_name, values.middle_name, values.last_name))),
                    'mobile_number' : values.mobile_number,
                    'emp_email' : values.email_id,
                    'personal_email' : values.personal_email,
                    'date_of_joining' : values.date_of_joining,
                    'status_id' : values.status_id,
                    'jobtitle_id' : values.jobtitle_id,
                    'emp_dob' : values.birth_date,
                    'emp_curr_addr' : values.address,
                    'emp_per_addr' : values.permanent_address,
                    'office_number' : '' if values.office_number is None else values.office_number,
                    'isactive' : values.isactive,
                    'year_exp' : values.year_exp,
                    'businessunit_id' : values.businessunit_id,
                    'manager_name': '' if values.manager_id is None else ' '.join(filter(None, (values.manager_first_name,
                                                                                                values.manager_middle_name,
                                                                                                values.manager_last_name))),
                    'manager_id' :'' if values.manager_id is None else values.manager_id,
                    'office_location_id' : values.office_location_id,
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
            delqry = employee.objects.get(emp_id=id)
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
            getqry = employee.objects.raw("Select a.emp_image,a.emp_id,a.email_id,a.date_of_joining,a.date_of_leaving,a.status_id,a.jobtitle_id,a.mobile_number,a.office_number,a.isactive,a.year_exp, a.businessunit_id,a.personal_email, a.first_name, a.middle_name, a.last_name, a.birth_date, a.address, a.permanent_address,a.office_location_id,a.emp_dm_id, b.first_name as manager_first_name, b.middle_name as manager_middle_name, b.last_name as manager_last_name, a.manager_id from employee a left join employee b on a.manager_id = b.emp_id where a.emp_id="+id)
            # print 'Select a.emp_image,a.emp_id,a.email_id,a.date_of_joining,a.date_of_leaving,a.status_id,a.jobtitle_id,a.mobile_number,a.created_by,a.office_number,a.isactive,a.modified_by,a.year_exp, a.businessunit_id,a.modified_date, a.created_date,a.personal_email, a.first_name, a.middle_name, a.last_name, a.birth_date, a.address, a.permanent_address,a.office_location_id,a.emp_dm_id, b.first_name as manager_first_name, b.middle_name as manager_middle_name, b.last_name as manager_last_name, a.manager_id from employee a left join employee b on a.manager_id = b.emp_id where a.emp_id='+id

            dataobj = {
                    'emp_id' : getqry[0].emp_id,
                    'first_name' : getqry[0].first_name,
                    'middle_name': getqry[0].middle_name,
                    'last_name' : getqry[0].last_name,
                    # 'mobile_number' : '' if getqry[0].mobile_number is None or 'Null' else int(getqry[0].mobile_number),
                    'mobile_number':int(getqry[0].mobile_number),
                    'emp_email' : getqry[0].email_id,
                    'personal_email' : getqry[0].personal_email,
                    'date_of_joining' : getqry[0].date_of_joining,
                    'date_of_leaving' : getqry[0].date_of_leaving,
                    'status_id' : getqry[0].status_id,
                    'jobtitle_id' : getqry[0].jobtitle_id,
                    # 'jobtitle_name' : getdesigqry.designation_name,
                    'emp_dob' : getqry[0].birth_date,
                    'emp_curr_addr' : getqry[0].address,
                    'emp_per_addr' : getqry[0].permanent_address,
                    'office_number' : '' if getqry[0].office_number is None or 'Null' else int(getqry[0].office_number),
                    'isactive' : getqry[0].isactive,
                    'year_exp' : getqry[0].year_exp,
                    'businessunit_id' : getqry[0].businessunit_id,
                    'manager_name': '' if getqry[0].manager_id is None else ' '.join(filter(None, (getqry[0].manager_first_name, getqry[0].manager_middle_name, getqry[0].manager_last_name))),
                    'manager_id' :'' if getqry[0].manager_id is None else getqry[0].manager_id,
                    'office_location_id' : getqry[0].office_location_id,
                    'dmEmpId' : getqry[0].emp_dm_id,
                    'emp_image' : getqry[0].emp_image,
                    'emp_role' : getqry[0].emp_role,
            }
            return dataobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def updateEmployee(self ,id, empFirstName, empMiddleName, empLastName, empEmail,
                        empPersonalEmail, empMobNum, empDob, status, jobTitle,
                        doj,dol, officeNumber, isActive, experience, businessUnit,
                        manager, officeLocation, empCurrAddr, empPermaAddr, myfile,empRole,updated_date,updated_by):

        try:

            getqry = employee.objects.get(emp_id=id)

            if dol != '':
                getqry.date_of_leaving = dol
            getqry.email_id = empEmail
            getqry.date_of_joining = doj
            getqry.status_id = status
            getqry.jobtitle_id = jobTitle
            getqry.mobile_number = empMobNum
            getqry.office_number =officeNumber
            getqry.isactive = isActive
            getqry.year_exp = experience
            getqry.businessunit_id = businessUnit
            getqry.manager_id = manager
            getqry.personal_email = empPersonalEmail
            getqry.first_name = empFirstName
            getqry.middle_name = '' if empMiddleName is None else empMiddleName
            getqry.last_name = empLastName
            getqry.birth_date = empDob
            getqry.address = empCurrAddr
            getqry.permanent_address = empPermaAddr
            getqry.office_location_id = officeLocation
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
    def advanceSearch(cls,columnName, searchText, dbCondition):
        try:
            if dbCondition == 'like':
                kwargs = {columnName+'__contains': searchText}
                getqry = employee.objects.get(**kwargs)

                dataobj = {
                    'emp_id': getqry.employee_id,
                    'emp_name': getqry.employee_name,
                    'emp_mob_no': getqry.mobile_number,
                    'emp_email': getqry.email,
                    'emp_dob': getqry.dob,
                    'emp_curr_addr': getqry.current_address,
                    'emp_per_addr': getqry.permanent_address,
                    'modified_date': getqry.modified_date,
                }
                return dataobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj


    @classmethod
    def employeedesignationvalues(cls):
        dm_designations = dmdesignation.listDesignation()
        return dm_designations

    @classmethod
    def employeebusinessunitvalues(cls):
        business_unit = businessUnitMaster.listBusinessUnitMaster()
        return business_unit

    @classmethod
    def employeeofficelocationvalues(cls):
        dm_officeLocation = officeLocation.listOfficelocaltion()
        return dm_officeLocation

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

    @classmethod
    def getEmp360IncrementDetails(cls, id):
        try:
            listempIncrement = employee.objects.raw(
                'select * from employee_designationpackagehistory where emp_id=' + id)

            employeeIncrementDataList= []

            for values in listempIncrement:
                employeeIncrementDataList.append({
                    'emp_salary':values.salary,
                    'emp_increment_date': values.from_date,
                })

            return employeeIncrementDataList

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def getEmp360EducationDetails(cls, id):
        try:
            listempEdu = employee.objects.raw('SELECT * FROM employee_education where emp_id=' + id)

            employeeEduDataList = []

            for values in listempEdu:
                employeeEduDataList.append({
                    'school_uni': values.school_univeristy_name,
                    'qualification': values.qualification_degree_name,
                    'completed_on': values.date_of_completion,
                })

            return employeeEduDataList

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj




    @classmethod
    def getEmp360Details(cls, id):
        try:
            empProjectCount = employee_project.objects.filter(emp_id=id)

            empIncrementCount = employee_designationpackagehistory.objects.filter(emp_id=id)

            employeeList = []

            empId=id
            if empId != '1':
                listqry = employee.objects.raw('Select a.date_of_joining,e.customer_name,d.designation_name,a.emp_image,a.emp_id,a.year_exp, a.first_name, a.middle_name, a.last_name,a.emp_dm_id, c.project_name, b.start_date,b.end_date from employee a inner join employee_project b on a.emp_id=b.emp_id inner join project_master c on b.project_id=c.project_id inner join designation_master d on a.jobtitle_id=d.designation_id inner join customer_table e on c.customer_id=e.customer_id  where a.emp_id='+id)
                for values in listqry:
                    employeeList.append({
                        'emp_id': values.emp_id,
                        'emp_name': ' '.join(filter(None, (values.first_name, values.middle_name, values.last_name))),
                        'emp_dm_id': values.emp_dm_id,
                        'year_exp': values.year_exp,
                        'empImg': values.emp_image,
                        'project_name': values.project_name if values.project_name else '',
                        'project_start_date': values.start_date if values.start_date else '',
                        'project_end_date': values.end_date if values.end_date else '',
                        'emp_designation': values.designation_name,
                        'project_customer': values.customer_name if values.customer_name else '',
                        'emp_project_count': len(empProjectCount),
                        'emp_increment_count': len(empIncrementCount),
                        'date_of_joining': values.date_of_joining,

                    })
            else:
                listqry = employee.objects.raw(
                    'Select a.date_of_joining,d.designation_name,a.emp_image,a.emp_id,a.year_exp, a.first_name, a.middle_name, a.last_name,a.emp_dm_id from employee a inner join designation_master d on a.jobtitle_id=d.designation_id where a.emp_id=' + id)

                for values in listqry:
                    employeeList.append({
                        'emp_id': values.emp_id,
                        'emp_name': ' '.join(filter(None, (values.first_name, values.middle_name, values.last_name))),
                        'emp_dm_id': values.emp_dm_id,
                        'year_exp': values.year_exp,
                        'empImg': values.emp_image,
                        'emp_designation': values.designation_name,
                        'emp_project_count': len(empProjectCount),
                        'emp_increment_count': len(empIncrementCount),
                        'date_of_joining': values.date_of_joining

                    })

            return employeeList

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj




