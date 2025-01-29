"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.webHome),
    path('index/',views.webHome),
    path('about/',views.webAbout),
    path('login/',views.webLogin),
    path('university/',views.webUniversity),
    path('contact/',views.webContact),
    path('institution/',views.webInstitution),
    path('single_institution/',views.webSingleInstitution),
    path('logout/',views.logout),

    # admin
    path('adminindex/', views.adminAdminindex),
    path('addColleges/', views.adminAddCollege),
    path('add_University/', views.adminAdd_University),
    path('contactDetails/',views.adminContactDetails),
    path('logout_web/',views.logoutWeb),
    path('manageCollege/',views.adminManageCollege),
    path('manageUniversity/', views.adminManageUniversity),
    path('add_institution/', views.adminAdd_Institution),
    path('manageInstitution/', views.adminManageInstitution),
    path('userDetails/', views.adminUserDetails),
    path('add_admin_master/', views.adminAddMaster),
    path('manage_admin_master/', views.adminManageMaster),

    path('add_course_master/', views.courseAddMaster),
    path('manage_course_master/', views.courseManageMaster),

    path('admin_login/', views.adminLogin),
    path('admin_login_details/', views.loginAdminDetails, name='login'),

    path("admin_details/", views.adminMasterDetails),
    path("course_details/", views.courseMasterDetails),
    path("university_details/", views.universityDetails),
    path("college_details/", views.collegeDetails),
    path("institution_details/", views.institutionDetails),


    # vender
    path('course_master/',views.courseCollegeMaster),
    path('manage_course_details/',views.courseCollegeManageMaster),
    path('course_college_details/',views.courseCollegeDetails),

    path('add_staff/',views.addStaff),
    path('manage_staff_details/',views.staffCollegeManageMaster),
    path('staff_college_details/',views.staffCollegeDetails),

    # Institution
    path('incourse_masters/',views.courseInstitutionMasters),
    path('inmanage_course_detail/',views.courseInstitutionManageMaster),

    path('inadd_staffs/',views.addStaffs),
    path('inmanage_staff_detail/',views.staffInstitutionDeatils),
    path('inmanage_requests/',views.institutionRequestDetails),

    path('staff_institution_details/',views.staffInstitutionDetails),
    path('course_institution_details/',views.courseInstitutionDetails),
    path('get_institute_request/',views.getInstitutionRequest),
    path('get_institute_update_request/',views.getInstituteUpdateRequest),


    path('register/',views.register),
    path('add_register/', views.newRegister, name='home'),

    # path('web_login/', views.openWebLogin, name='web_login'),
    path('check_web_login/', views.checkWebLogin, name='web_login'),

    path('user_request/', views.userRequest, name='home'),
    path('manage_request/', views.manage_request, name='home'),
    path('get_college_request/', views.getCollegeRequest, name='home'),
    path('update_request/', views.updateRequest, name='home'),
    path('my_request_status/', views.my_request_status, name='home'),
    path('my_request_status_details/', views.myRequestStatusDetails, name='home'),
    path('my_request_institution_status_details/', views.myRequestStatusInstitutionDetails, name='home'),
    path('update_payment_request/', views.updatePaymentRequest, name='home'),
    path('update_payment_request1/', views.updatePaymentRequest1, name='home'),




    # path('addinfo/',views.customerAddinfo),
    # path('addseat/',views.customerAddseat),
    # path('admissiondetail/',views.customerAdmissiondetail),
    # path('booking/',views.customerBooking),
    # path('feesdetail/',views.customerFeesdetail),
    # path('logout/',views.customerLogout),
    # path('manageadmissiondetail/',views.customerManageadmissiondetail),
    # path('manageinfo/',views.customerManageinfo),
    # path('manageseat/',views.customerManageseat)
     path('get_home_details/', views.getHomeDetails, name='home'),
     path('get_institution_details/', views.getInstitutionDetails, name='home'),
     path('get_web_institutions_details/', views.getWebInstitutionsDetails, name='home'),
     path('get_web_institution_course_details/', views.getWebInstitutionCourseDetails, name='home'),
     path('get_web_institution_staff_details/', views.getWebInstitutionStaffDetails, name='home'),
     path('institution_request/', views.institutionRequest, name='home'),
     path('college_list/', views.college_list, name='home'),
     path('view_college/', views.view_college, name='home'),
     path('get_web_college_list/', views.getWebCollegeList, name='home'),

     path('get_web_college_details/', views.getWebCollegeDetails, name='home'),
     path('get_web_course_details/', views.getWebCourseDetails, name='home'),
     path('get_web_staff_details/', views.getWebStaffDetails, name='home'),

     path('pay_success/', views.paySuccess, name='home'),

    path('submit_review/', views.submitReview, name='home'),
    path('get_review/', views.getReview, name='home'),

    path('web_forgot_password/', views.webForgotPassword, name='web_forgot_password'),
    path('web_update_password/', views.webUpdatePassword, name='web_forgot_password'),
    path('user_check_email/', views.checkEmail, name='user_check_email'),
    path('update_password/', views.updatePassword, name='update_password'),
path('forgot_password/',views.forgotPassword),
   path('check_password/',views.checkPassword),
   path('get_update_password/',views.adminupdatePassword),
   path('reset_password/',views.resetPassword),

]
