from django.conf.urls import url

from hrms_admin.dashboard.dashboardController import dashboardController

from hrms_admin.login.logincontroller import logincontroller




urlpatterns =[



    # Session login logout
    url('^api/userlogin/$', logincontroller.login),
    url('^dashboard/api/checksession/$', logincontroller.checksession),
    url('^dashboard/api/signout/$', logincontroller.logout),

    url('^dashboard/api/fetchdashboardvalues/$', dashboardController.fetchDashboardValues),

]