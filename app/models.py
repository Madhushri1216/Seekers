from django.db import models

# Create your models here.

class AdminMaster(models.Model):
	ad_id = models.AutoField(primary_key=True, unique = True)
	ad_name = models.CharField(max_length=100)
	ad_mobile = models.CharField(max_length=100)
	ad_email = models.CharField(max_length=100)
	ad_password = models.CharField(max_length=100)
	ad_key = models.CharField(max_length=100,default="")
	ad_role = models.CharField(max_length=100, default="")
	ad_status = models.IntegerField(default=0)
	ad_created_by = models.CharField(max_length=100)

class Register(models.Model):
	rg_id = models.AutoField(primary_key=True, unique = True)
	rg_name = models.CharField(max_length=100)
	rg_mobile = models.CharField(max_length=100)
	rg_email = models.CharField(max_length=100)
	rg_password = models.CharField(max_length=100)
	rg_address = models.CharField(max_length=100, default="")
	rg_status = models.IntegerField(default=0)

class College(models.Model):
	cl_id = models.AutoField(primary_key=True, unique = True)
	cl_image = models.FileField(upload_to="app/static/media/images")
	cl_university_name = models.CharField(max_length=100, default="")
	cl_name = models.CharField(max_length=100)
	cl_mobile = models.CharField(max_length=100)
	cl_email = models.CharField(max_length=100)
	cl_address = models.CharField(max_length=100)
	cl_about = models.CharField(max_length=100)
	cl_rank = models.CharField(max_length=100, default="")
	cl_naac = models.CharField(max_length=100, default="")
	cl_status = models.IntegerField(default=0)
	cl_created_by = models.CharField(max_length=100)

class Institution(models.Model):
	in_id = models.AutoField(primary_key=True, unique = True)
	in_image = models.FileField(upload_to="app/static/media/images")
	in_name = models.CharField(max_length=100)
	in_mobile = models.CharField(max_length=100)
	in_email = models.CharField(max_length=100)
	in_address = models.CharField(max_length=100)
	in_about = models.CharField(max_length=100)
	in_status = models.IntegerField(default=0)
	in_created_by = models.CharField(max_length=100)

class University(models.Model):
	un_id = models.AutoField(primary_key=True, unique = True)
	un_image = models.FileField(upload_to="app/static/media/images")
	un_name = models.CharField(max_length=100)
	un_mobile = models.CharField(max_length=100)
	un_email = models.CharField(max_length=100)
	un_address = models.CharField(max_length=100)
	un_total_college = models.CharField(max_length=100)
	un_about = models.CharField(max_length=100, default="")
	un_status = models.IntegerField(default=0)
	un_created_by = models.CharField(max_length=100)

class Courses(models.Model):
	co_id = models.AutoField(primary_key=True, unique = True)
	co_name = models.CharField(max_length=100)
	co_status = models.IntegerField(default=0)
	co_created_by = models.CharField(max_length=100)

class CoursesDetails(models.Model):
	cd_id = models.AutoField(primary_key=True, unique = True)
	cd_college_name = models.CharField(max_length=100)
	cd_college_email = models.CharField(max_length=100)
	cd_name = models.CharField(max_length=100)
	cd_fees = models.CharField(max_length=100)
	cd_total_seats_gov = models.CharField(max_length=100, default=0)
	cd_total_seats_mng = models.CharField(max_length=100, default=0)
	cd_available_seats_gov = models.CharField(max_length=100, default=0)
	cd_available_seats_mng = models.CharField(max_length=100, default=0)
	cd_status = models.IntegerField(default=0)
	cd_created_by = models.CharField(max_length=100)

class CollegeRequest(models.Model):
	cr_id = models.AutoField(primary_key=True, unique = True)
	cr_seat_type = models.CharField(max_length=100, default="")
	cr_name = models.CharField(max_length=100)
	cr_email = models.CharField(max_length=100)
	cr_mobile = models.CharField(max_length=100)
	cr_address = models.CharField(max_length=100, default="")
	cr_previous_education = models.CharField(max_length=100, default="")
	cr_percentage = models.CharField(max_length=100, default="")
	cr_year_passing = models.CharField(max_length=100, default="")
	cr_message = models.CharField(max_length=100, default="")
	cr_status = models.CharField(max_length=100, default="Pending")
	cr_payment_status = models.CharField(max_length=100, default="Pending")
	cr_department = models.CharField(max_length=100, default="")
	cr_amount = models.CharField(max_length=100, default="5000")
	cr_created_by = models.CharField(max_length=100)

class CollegeStaff(models.Model):
	cs_id = models.AutoField(primary_key=True, unique = True)
	# cs_image = models.FileField(upload_to="app/static/media/images")
	cs_name = models.CharField(max_length=100)
	cs_department = models.CharField(max_length=100)
	cs_designation = models.CharField(max_length=100)
	cs_status = models.IntegerField(default=0)
	cs_created_by = models.CharField(max_length=100)

class InstitutionCourse(models.Model):
	ic_id = models.AutoField(primary_key=True, unique = True)
	ic_institute_name = models.CharField(max_length=100)
	ic_fees = models.CharField(max_length=100)
	ic_status = models.IntegerField(default=0)
	ic_created_by = models.CharField(max_length=100,default="")

class InstituteStaff(models.Model):
	is_id = models.AutoField(primary_key=True, unique = True)
	# is_image = models.FileField(upload_to="app/static/media/images")
	is_name = models.CharField(max_length=100)
	is_department = models.CharField(max_length=100)
	is_designation = models.CharField(max_length=100)
	is_status = models.IntegerField(default=0)
	is_created_by = models.CharField(max_length=100)

class InstitutionRequest(models.Model):
	ir_id = models.AutoField(primary_key=True, unique = True)
	# ir_seat_type = models.CharField(max_length=100, default="")
	ir_name = models.CharField(max_length=100)
	ir_email = models.CharField(max_length=100)
	ir_mobile = models.CharField(max_length=100)
	ir_address = models.CharField(max_length=100, default="")
	ir_previous_education = models.CharField(max_length=100, default="")
	ir_percentage = models.CharField(max_length=100, default="")
	ir_year_passing = models.CharField(max_length=100, default="")
	ir_message = models.CharField(max_length=100, default="")
	ir_status = models.CharField(max_length=100, default="Pending")
	ir_payment_status = models.CharField(max_length=100, default="Pending")
	ir_department = models.CharField(max_length=100, default="")
	ir_amount = models.CharField(max_length=100, default="5000")
	ir_created_by = models.CharField(max_length=100)


class Review(models.Model):
	rv_id = models.AutoField(primary_key=True, unique = True)
	rv_cl_id = models.CharField(max_length=100, default="")
	rv_name = models.CharField(max_length=100)
	rv_email = models.CharField(max_length=100)
	rv_message = models.CharField(max_length=100)
	rv_rating = models.CharField(max_length=100)
	rv_status = models.CharField(max_length=100)
	rv_created_by = models.CharField(max_length=100, default="")
