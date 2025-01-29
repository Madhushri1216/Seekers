from django.shortcuts import render
from app.models import AdminMaster
from app.models import Register
from app.models import Courses
from app.models import University
from app.models import College
from app.models import CoursesDetails
from app.models import CollegeStaff
from app.models import CollegeRequest
from app.models import Institution
from app.models import InstitutionCourse
from app.models import InstituteStaff
from app.models import InstitutionRequest
from app.models import Review

from django.http import HttpResponse

from django.http import JsonResponse
import datetime
# Create your views here.
def webHome(request):
    return render(request,'web/index.html');

def webAbout(request):
    return render(request,'web/about.html');

def webContact(request):
    return render(request,'web/contact.html');

def webUniversity(request):
    return render(request,'web/university.html');

def webInstitution(request):
    return render(request,'web/institution.html');

def webSingleInstitution(request):
    if 'web_email' in request.session:
        return render(request,'web/single_institution.html');
    else:
        return render(request,'web/login.html');

def webLogin(request):
    return render(request,'web/login.html');

# admin
def adminAdminindex(request):
	return render(request,'admin/adminindex.html');
	
def adminAddCollege(request):
	return render(request, 'admin/addCollege.html');

def adminAdd_University(request):
	return render(request, 'admin/add_University.html');

def adminContactDetails(request):
	return render(request, 'admin/contactDetails.html');

def adminUserDetails(request):
	return render(request, 'admin/userDetails.html');

def adminManageCollege(request):
	return render(request,'admin/manageCollege.html');

def adminManageUniversity(request):
	return render(request,'admin/manageUniversity.html');

def adminAddMaster(request):
	return render(request,'admin/add_admin_master.html');

def adminManageMaster(request):
	return render(request,'admin/manage_admin_master.html');

def courseAddMaster(request):
	return render(request,'admin/add_course_master.html');

def courseManageMaster(request):
	return render(request,'admin/manage_course_master.html');

def courseCollegeManageMaster(request):
    return render(request,'college/manage_course_details.html');

def adminAdd_Institution(request):
    return render(request,'admin/add_institution.html');

def adminManageInstitution(request):
    return render(request,'admin/manageInstitution.html');

def adminLogin(request):
	return render(request,'admin_login.html');

def manage_request(request):
    return render(request,'college/manage_request.html');

def logout(request):
    request.session.delete()
    return render(request, 'admin_login.html', {})

def logoutWeb(request):
    request.session.delete()
    return render(request, 'web/index.html', {})

def logout(request):
    request.session.delete()
    return render(request, 'admin_login.html', {})

def loginAdminDetails(request):
    if AdminMaster.objects.filter(ad_email=request.POST['txtEmail'], ad_password=request.POST['txtPassword'], ad_status=0).exists():
        data = AdminMaster.objects.filter(ad_email=request.POST['txtEmail']).values()
        data = list(data)
        dictValue = data[0]
        request.session['email'] = dictValue['ad_email']
        request.session['role'] = dictValue['ad_role']
        request.session['name'] = dictValue['ad_name']
        return HttpResponse(dictValue['ad_role'])
    else:
        return HttpResponse("0")  
# vendor
def courseCollegeMaster(request):
	return render(request, 'college/course_master.html');



def customerAddseat(request):
	return render(request, 'college/addseat.html');

def customerAdmissiondetail(request):
	return render(request, 'college/admissiondetail.html');

def customerBooking(request):
	return render(request, 'college/booking.html');

def customerFeesdetail(request):
	return render(request, 'college/feesdetail.html');

def customerLogout(request):
	return render(request, 'college/logout.html');

def customerManageadmissiondetail(request):
	return render(request, 'college/manageadmissiondetail.html');

def customerManageinfo(request):
	return render(request, 'college/manageinfo.html');

def customerManageseat(request):
	return render(request, 'college/manageseat.html');


def addStaff(request):
    return render(request, 'college/add_staff.html');

def staffCollegeManageMaster(request):
    return render(request, 'college/manage_staff_details.html');

def college_list(request):
    return render(request, 'web/college_list.html');

def view_college(request):
    if 'web_email' in request.session:
        return render(request, 'web/view_college.html');
    else:
        return render(request, 'web/login.html');

def register(request):
    return render(request, 'web/register.html');

def paySuccess(request):
    return render(request, 'web/pay_success.html');


# Institution
def courseInstitutionMasters(request):
    return render(request, 'institution/incourse_masters.html');

def courseInstitutionManageMaster(request):
    return render(request, 'institution/inmanage_course_detail.html');

def addStaffs(request):
    return render(request, 'institution/inadd_staffs.html');

def staffInstitutionDeatils(request):
    return render(request, 'institution/inmanage_staff_detail.html');

def institutionRequestDetails(request):
    return render(request, 'institution/inmanage_requests.html');


def my_request_status(request):
    # print(request.session['web_email']);
    if 'web_email' in request.session:
        return render(request, 'web/my_request_status.html');
    else:
        return render(request, 'web/login.html');

def adminMasterDetails(request):
    if request.POST['action'] == "add":
        AdminMaster.objects.create(
            ad_name = request.POST['txtName'],
            ad_mobile = request.POST['txtContact'],
            ad_email = request.POST['txtEmail'], 
            ad_password = request.POST['txtPassword'], 
        ad_key=request.POST['txtSecretKey'],
            ad_role = request.POST['txtRole'])	

    elif request.POST['action'] == "getData":
        data = AdminMaster.objects.filter(ad_status='0').values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values
        
    elif request.POST['action'] == "update":
        data = AdminMaster.objects.filter(ad_id=request.POST['id']).update(ad_name = request.POST['txtName1'],ad_mobile = request.POST['txtContact1'],ad_email = request.POST['txtEmail1'], ad_role = request.POST['txtRole1']);
        
    elif request.POST['action'] == "delete":
        data = AdminMaster.objects.filter(ad_id=request.POST['id']).update(ad_status='1')
    
    return HttpResponse()

def courseMasterDetails(request):
    if request.POST['action'] == "add":
        Courses.objects.create(
            co_name = request.POST['txtName']
        )  

    elif request.POST['action'] == "getData":
        data = Courses.objects.filter(co_status='0').values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values
        
    elif request.POST['action'] == "update":
        data = Courses.objects.filter(co_id=request.POST['id']).update(co_name = request.POST['txtName1']);
        
    elif request.POST['action'] == "delete":
        data = Courses.objects.filter(co_id=request.POST['id']).update(co_status='1')
    
    return HttpResponse()


def universityDetails(request):
    if request.POST['action'] == "add":
        University.objects.create(
            un_image = request.FILES['lclImage'],
            un_name = request.POST['txtName'],
            un_mobile = request.POST['txtContact'],
            un_email = request.POST['txtEmail'], 
            un_address = request.POST['txtAddress'], 
            un_total_college = request.POST['txtTotalColleges'],
            un_about = request.POST['txtAbout'],
        )  

    elif request.POST['action'] == "getData":
        data = University.objects.filter(un_status='0').values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values
        
    elif request.POST['action'] == "update":
        data = University.objects.filter(un_id=request.POST['id']).update(
            un_name = request.POST['txtName1'],
            un_mobile = request.POST['txtContact1'],
            un_email = request.POST['txtEmail1'], 
            un_address = request.POST['txtAddress1'], 
            un_total_college = request.POST['txtTotalColleges1'],
            un_about = request.POST['txtAbout1'],
        );
        
    elif request.POST['action'] == "delete":
        data = University.objects.filter(un_id=request.POST['id']).update(un_status='1')
    
    return HttpResponse()

def staffCollegeDetails(request):
    if request.POST['action'] == "add":
        CollegeStaff.objects.create(
            cs_name = request.POST['txtName'],
            cs_department = request.POST['txtDepartment'],
            cs_designation = request.POST['txtDesignation'],
            cs_created_by = request.session['email'],
        )  

    elif request.POST['action'] == "getData":
        data = CollegeStaff.objects.filter(cs_status='0', cs_created_by=request.session['email']).values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values
        
    elif request.POST['action'] == "update":
        data = CollegeStaff.objects.filter(cs_id=request.POST['id']).update(
            cs_name = request.POST['txtName1'],
            cs_department = request.POST['txtDepartment1'],
            cs_designation = request.POST['txtDesignation1']
        );
        
    elif request.POST['action'] == "delete":
        data = CollegeStaff.objects.filter(cs_id=request.POST['id']).update(cs_status='1')
    
    return HttpResponse()

def collegeDetails(request):
    if request.POST['action'] == "add":
        College.objects.create(
            cl_image = request.FILES['lclImage'],
            cl_university_name = request.POST['selUniversity'],
            cl_name = request.POST['txtName'],
            cl_mobile = request.POST['txtContact'],
            cl_email = request.POST['txtEmail'], 
            cl_address = request.POST['txtAddress'],
            cl_about = request.POST['txtAbout'],
            cl_rank = request.POST['selRank'],
            cl_naac = request.POST['txtNaac'],
        )  

    elif request.POST['action'] == "getData":
        data = College.objects.filter(cl_status='0').values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values
        
    elif request.POST['action'] == "update":
        data = College.objects.filter(cl_id=request.POST['id']).update(
            cl_university_name = request.POST['selUniversity1'],
            cl_name = request.POST['txtName1'],
            cl_mobile = request.POST['txtContact1'],
            cl_email = request.POST['txtEmail1'], 
            cl_address = request.POST['txtAddress1'], 
            cl_about = request.POST['txtAbout1'],
            cl_rank = request.POST['selRank1'],
            cl_naac = request.POST['txtNaac1'],
        );
        
    elif request.POST['action'] == "delete":
        data = College.objects.filter(cl_id=request.POST['id']).update(cl_status='1')
    
    return HttpResponse()


def courseCollegeDetails(request):
    if request.POST['action'] == "add":
        CoursesDetails.objects.create(
            cd_college_name = request.session['name'],
            cd_college_email = request.session['email'],
            cd_name = request.POST['txtName'], 
            cd_fees = request.POST['txtFees'],
            cd_total_seats_gov = request.POST['txtTotalSeatsGovernment'],
            cd_total_seats_mng = request.POST['txtTotalSeatsManagement'],
            cd_available_seats_gov = request.POST['txtTotalSeatsGovernment'],
            cd_available_seats_mng = request.POST['txtTotalSeatsManagement'],
            cd_created_by = request.session['email'],
        )  

    elif request.POST['action'] == "getData":
        data = CoursesDetails.objects.filter(cd_status='0', cd_created_by=request.session['email']).values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values
        
    elif request.POST['action'] == "update":
        data = CoursesDetails.objects.filter(cd_id=request.POST['id']).update(
            cd_name = request.POST['txtName1'], 
            cd_fees = request.POST['txtFees1']
        );
        
    elif request.POST['action'] == "delete":
        data = CoursesDetails.objects.filter(cd_id=request.POST['id']).update(cd_status='1')
    
    return HttpResponse()


def courseInstitutionDetails(request):
    if request.POST['action'] == "add":
        InstitutionCourse.objects.create(
            # ic_institute_name = request.session['name'],
            ic_institute_name = request.POST['txtName'], 
            ic_fees = request.POST['txtFees'],
            ic_created_by = request.session['email'], 
        )  

    elif request.POST['action'] == "getData":
        data = InstitutionCourse.objects.filter(ic_status='0', ic_created_by=request.session['email']).values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values
        
    elif request.POST['action'] == "update":
        data = InstitutionCourse.objects.filter(ic_id=request.POST['id']).update(
            ic_institute_name = request.POST['txtName1'], 
            ic_fees = request.POST['txtFees1']
        );
        
    elif request.POST['action'] == "delete":
        data = InstitutionCourse.objects.filter(ic_id=request.POST['id']).update(ic_status='1')
    
    return HttpResponse()



def newRegister(request):

    if Register.objects.filter(rg_email=request.POST['txtEmail'], rg_mobile=request.POST['txtMobileNo']).exists():
        return HttpResponse('10')
    else:
        lclID = Register.objects.count()
        status = "0"
        lclNewID = lclID + 1

        Register.objects.create (
            rg_id = lclNewID,
            rg_name = request.POST['txtName'],
            rg_mobile = request.POST['txtMobileNo'],
            rg_email = request.POST['txtEmail'],
            rg_password = request.POST['txtPassword'],
            rg_address = request.POST['txtAddress'],

        )

        return HttpResponse('0')

def checkWebLogin(request):
    if Register.objects.filter(rg_email=request.POST['txtEmail'], rg_password=request.POST['txtPassword']).exists():
        request.session['web_email'] = request.POST['txtEmail']
        return HttpResponse("1")
    else:
        return HttpResponse("10")

def userRequest(request):

    if 'web_email' in request.session:
        if CollegeRequest.objects.filter(cr_email=request.POST['txtEmail'], cr_created_by=request.POST['txtCollegeEmail']).exists():
            return HttpResponse('10')
        else:
            CollegeRequest.objects.create (
                cr_seat_type = request.POST['selSeatType'],
                cr_department = request.POST['selDepartment'],
                cr_name = request.POST['txtName'],
                cr_email = request.session['web_email'],
                cr_mobile = request.POST['txtMobileNo'],
                cr_address = request.POST['txtAddress'],
                cr_previous_education = request.POST['txtPrevEducation'],
                cr_percentage = request.POST['txtPrevPercentage'],
                cr_year_passing = request.POST['txtYearPassing'],
                cr_created_by = request.POST['txtCollegeEmail'],

            )

            return HttpResponse('0')
    else:
        return HttpResponse('20')

def institutionRequest(request):

    if 'web_email' in request.session:
        if InstitutionRequest.objects.filter(ir_email=request.POST['txtEmail'], ir_created_by=request.POST['txtCollegeEmail']).exists():
            return HttpResponse('10')
        else:
            InstitutionRequest.objects.create (
                # cr_seat_type = request.POST['selSeatType'],
                ir_department = request.POST['selDepartment'],
                ir_name = request.POST['txtName'],
                ir_email = request.session['web_email'],
                ir_mobile = request.POST['txtMobileNo'],
                ir_address = request.POST['txtAddress'],
                ir_previous_education = request.POST['txtPrevEducation'],
                ir_percentage = request.POST['txtPrevPercentage'],
                ir_year_passing = request.POST['txtYearPassing'],
                ir_created_by = request.POST['txtCollegeEmail'],

            )

            return HttpResponse('0')
    else:
        return HttpResponse('20')

def updatePaymentRequest(request):
    dataUpdate = CollegeRequest.objects.filter(cr_id=request.POST['id']).update(cr_payment_status='Success');
    data = CollegeRequest.objects.filter(cr_id=request.POST['id']).values();
    getAvailableQTY = CoursesDetails.objects.filter(cd_created_by=request.POST['collegeEmail'], cd_name=request.POST['department']).values();
    jsonData = list(getAvailableQTY);
    dictValue = jsonData[0];

    checkRequestData = list(data);
    checkRequestData1 = checkRequestData[0];
    if checkRequestData1['cr_seat_type'] == "Government":
        avaQty = int(dictValue['cd_available_seats_gov']) - 1;
        data = CoursesDetails.objects.filter(cd_id=dictValue['cd_id']).update(cd_available_seats_gov=avaQty);
    else:
        avaQty = int(dictValue['cd_available_seats_mng']) - 1;
        data = CoursesDetails.objects.filter(cd_id=dictValue['cd_id']).update(cd_available_seats_mng=avaQty);

    return HttpResponse()


def updatePaymentRequest1(request):
    InstitutionRequest.objects.filter(ir_id=request.POST['id']).update(ir_payment_status='Success');
    return HttpResponse()

def getHomeDetails(request):
    getData = University.objects.filter(un_status=0).values();
    jsonData = list(getData);
    return JsonResponse(jsonData, safe=False)

def getInstitutionDetails(request):
    getData = Institution.objects.filter(in_status=0).values();
    jsonData = list(getData);
    return JsonResponse(jsonData, safe=False)

def getWebInstitutionsDetails(request):
    getData = Institution.objects.filter(in_email = request.POST['txtID'],in_status=0).values();
    jsonData = list(getData);
    return JsonResponse(jsonData, safe=False)
    
def getWebInstitutionCourseDetails(request):
    getData = InstitutionCourse.objects.filter(ic_status=0, ic_created_by=request.POST['txtID']).values();
    jsonData = list(getData);
    return JsonResponse(jsonData, safe=False)

def getWebInstitutionStaffDetails(request):
    getData = InstituteStaff.objects.filter(is_status=0, is_created_by=request.POST['txtID']).values();
    jsonData = list(getData);
    return JsonResponse(jsonData, safe=False)

def getWebCollegeList(request):
    getData = College.objects.filter(cl_status=0, cl_university_name=request.POST['txtID']).values();
    jsonData = list(getData);
    return JsonResponse(jsonData, safe=False)

def getWebCollegeDetails(request):
    getData = College.objects.filter(cl_status=0, cl_email=request.POST['txtID']).values();
    jsonData = list(getData);
    return JsonResponse(jsonData, safe=False)

def getWebCourseDetails(request):
    getData = CoursesDetails.objects.filter(cd_status=0, cd_created_by=request.POST['txtID']).values();
    jsonData = list(getData);
    return JsonResponse(jsonData, safe=False)

def getWebStaffDetails(request):
    getData = CollegeStaff.objects.filter(cs_status=0, cs_created_by=request.POST['txtID']).values();
    jsonData = list(getData);
    return JsonResponse(jsonData, safe=False)

def getCollegeRequest(request):
    getData = CollegeRequest.objects.filter(cr_created_by=request.session['email']).values();
    jsonData = list(getData);
    return JsonResponse(jsonData, safe=False)

def updateRequest(request):

    if request.POST['action'] == "Accepted":
        data = CollegeRequest.objects.filter(cr_id=request.POST['id']).update(
            cr_status = request.POST['action']
        );

    else:
        data = CollegeRequest.objects.filter(cr_id=request.POST['id']).update(
            cr_status = request.POST['action']
        );

    return HttpResponse()

def getInstitutionRequest(request):
    getData = InstitutionRequest.objects.filter(ir_created_by=request.session['email']).values();
    jsonData = list(getData);
    return JsonResponse(jsonData, safe=False)

def getInstituteUpdateRequest(request):

    if request.POST['action'] == "Accepted":
        data = InstitutionRequest.objects.filter(ir_id=request.POST['id']).update(
            ir_status = request.POST['action']
        );

    else:
        data = InstitutionRequest.objects.filter(ir_id=request.POST['id']).update(
            ir_status = request.POST['action']
        );

    return HttpResponse()

def myRequestStatusDetails(request):
    getData = CollegeRequest.objects.filter(cr_email=request.session['web_email']).values();
    jsonData = list(getData);
    return JsonResponse(jsonData, safe=False)

def myRequestStatusInstitutionDetails(request):
    getData = InstitutionRequest.objects.filter(ir_email=request.session['web_email']).values();
    jsonData = list(getData);
    return JsonResponse(jsonData, safe=False)


def institutionDetails(request):
    if request.POST['action'] == "add":
        Institution.objects.create(
            in_image = request.FILES['lclImage'],
            in_name = request.POST['txtName'],
            in_mobile = request.POST['txtContact'],
            in_email = request.POST['txtEmail'], 
            in_address = request.POST['txtAddress'],
            in_about = request.POST['txtAbout'],
        )  

    elif request.POST['action'] == "getData":
        data = Institution.objects.filter(in_status='0').values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values
        
    elif request.POST['action'] == "update":
        data = Institution.objects.filter(in_id=request.POST['id']).update(
            in_name = request.POST['txtName1'],
            in_mobile = request.POST['txtContact1'],
            in_email = request.POST['txtEmail1'], 
            in_address = request.POST['txtAddress1'], 
            in_about = request.POST['txtAbout1'],
        );
        
    elif request.POST['action'] == "delete":
        data = Institution.objects.filter(in_id=request.POST['id']).update(in_status='1')
    
    return HttpResponse()

def staffInstitutionDetails(request):
    if request.POST['action'] == "add":
        InstituteStaff.objects.create(
            is_name = request.POST['txtName'],
            is_department = request.POST['txtDepartment'],
            is_designation = request.POST['txtDesignation'],
            is_created_by = request.session['email'],
        )  

    elif request.POST['action'] == "getData":
        data = InstituteStaff.objects.filter(is_status='0', is_created_by=request.session['email']).values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values
        
    elif request.POST['action'] == "update":
        data = InstituteStaff.objects.filter(is_id=request.POST['id']).update(
            is_name = request.POST['txtName1'],
            is_department = request.POST['txtDepartment1'],
            is_designation = request.POST['txtDesignation1']
        );
        
    elif request.POST['action'] == "delete":
        data = InstituteStaff.objects.filter(is_id=request.POST['id']).update(is_status='1')
    
    return HttpResponse()


def submitReview(request):

	lclID = Review.objects.count()
	status = "0"
	lclNewID = lclID + 1

	Review.objects.create (
		rv_id = lclNewID,
		rv_cl_id = request.POST['txtID'],
		rv_name = request.POST['txtname'],
		rv_email = request.POST['txtemail'],
		rv_message = request.POST['txtmessage'],
		rv_rating = request.POST['selRating'],
		rv_status = status,
	)

	return HttpResponse()

def getReview(request):
	products_json = Review.objects.filter(rv_cl_id=request.POST['txtID'] ).values()
	data = list(products_json)
	value = JsonResponse(data, safe=False)
	return value

def webForgotPassword(request):
    return render(request, 'web/web_forgot_password.html');

def webUpdatePassword(request):
    return render(request, 'web/web_update_password.html');

def checkEmail(request):
    if Register.objects.filter(rg_email=request.POST['txtEmail'], rg_status='0').count():
        request.session['forgot_email'] = request.POST['txtEmail'];
        return HttpResponse("1");
    else:
        return HttpResponse("10");

def updatePassword(request):
    Register.objects.filter(rg_email=request.session['forgot_email']).update(
        rg_password = request.POST['txtPassword']
    );

    return HttpResponse("1");
    
def forgotPassword(request):
    return render(request, 'admin/forgot_password.html');
        
def adminupdatePassword(request):
    return render(request, 'admin/update_password.html');
    
def checkPassword(request):
    if  request.POST['txtRole'] == "Admin":
        if AdminMaster.objects.filter(ad_email=request.POST['txtEmail'], ad_key=request.POST['txtSecretKey']).count():
            request.session['forgot_email'] = request.POST['txtEmail']
            return HttpResponse("1")
        else:
            return HttpResponse("10")

def resetPassword(request):
    if request.POST['action'] == "update":
        if  request.POST['txtRole1'] == "Admin":
            data = AdminMaster.objects.filter(ad_status='0',ad_email=request.session['forgot_email']).update(
			
			# re_role = request.POST['txtRole1'],
			ad_password = request.POST['txtPassword1'],
			
			);

            return HttpResponse()
        
        
