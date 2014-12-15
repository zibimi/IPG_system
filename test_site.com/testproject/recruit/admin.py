from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.
from recruit.models import Party, Party_Skill, Requisition, Skill, Submittal, TimeSheet, Hours, EmpType, Category, Priority, ReqStatus, Client



class RequisitionAdmin(ImportExportModelAdmin):
	list_display  = ('req_date', 'req_status', 'client', 'recruiter', 'job_id', 'job_title', 'emp_type', 
		             'hours','loc', 'duration', 'rate', 'openings','get_keywords',
					 'req_contact', 'city','state','start_date','end_date','req_approved',
					 'category','priority')

	search_fields = ('req_date', 'req_status', 'client', 'recruiter', 'job_id', 'job_title', 'emp_type', 
		             'hours','loc', 'duration', 'rate', 'openings','keywords',
					 'req_contact', 'city','state','start_date','end_date','req_approved',
					 'category','priority')

	list_filter   = ('req_date', 'req_status', 'client', 'recruiter', 'job_id', 'job_title', 
		             'loc', 'duration', 'rate', 'openings',
					 'req_contact', 'city','state','start_date','end_date','req_approved',
					 'category','priority')
	
	fields        = ('req_date', 'req_status', 'client', 'recruiter', 'job_id', 'job_title', 'emp_type', 
		             'hours','loc', 'duration', 'rate', 'openings','keywords',
					 'req_contact', 'city','state','start_date','end_date','req_approved',
					 'category','priority')
	
	filter_horizontal = ('keywords',)
class PartyAdmin(ImportExportModelAdmin):
	list_display  = ('id','user','first_name','last_name','email','phone','address','city','state','zip','visa_status','type','portfolio_link','linkedin','source','resume_link','ts_update',
                     'candidate_skills')
	search_fields = ('user','type','first_name','last_name','email','phone','address','city','state','zip','visa_status','portfolio_link','linkedin','source','resume_link',
                     'ts_update','candidate_skills')
	list_filter   = ('user','type','first_name','last_name','email','phone','address','city','state','zip','visa_status','portfolio_link','linkedin','source','resume_link',
                     'ts_update')
	fields        = ('user','type','first_name','last_name','email','phone','address','city','state','zip','visa_status','portfolio_link','linkedin','source','resume_link','ts_update',
                     'skills')
	filter_horizontal = ('skills',)

class SkillAdmin(ImportExportModelAdmin):
	list_display  = ('id','skill_name','skill_desc','skill_catagory')
	search_fields = ('skill_name','skill_desc','skill_catagory')
	list_filter   = ('skill_name','skill_desc','skill_catagory')
	fields        = ('skill_name','skill_desc','skill_catagory')
	#resource_class = SkillResource

class Party_SkillAdmin(admin.ModelAdmin):
	list_display  = ('skill','skill_lvl','skill_start_date','skill_year','skill_notes')
	search_fields = ('skill','skill_lvl','skill_start_date','skill_year','skill_notes')
	list_filter   = ('skill','skill_lvl','skill_start_date','skill_year','skill_notes')
	fields        = ('skill','skill_lvl','skill_start_date','skill_year','skill_notes')
class SubmittalAdmin(ImportExportModelAdmin):
	list_display  = ('job_id','candidate','recruiter','date','hourly_rate','current_year_rate','expected_year_rate','interview_available','start_available','interview_feedback',
		            'status','interview_date')
	search_fields = ( 'job_id','candidate', 'recruiter','date','hourly_rate','current_year_rate','expected_year_rate','interview_available','start_available','interview_feedback',
					'status','interview_date')	
	list_filter   = ( 'job_id','candidate','recruiter','date','hourly_rate','current_year_rate','expected_year_rate','interview_available','start_available','interview_feedback',
					'status','interview_date')
	fields        = ('job_id','candidate','recruiter','date','hourly_rate','current_year_rate','expected_year_rate','interview_available','start_available','interview_feedback',
		             'status','interview_date')
class TimeSheetAdmin(ImportExportModelAdmin):
	list_display  = ('consultant','status','account','site','week_end','st_hrs','ot_hrs','dt_hrs','nb_hrs','other_hrs','notes')
	search_fields = ('consultant','status','account','site','week_end','st_hrs','ot_hrs','dt_hrs','nb_hrs','other_hrs','notes')	
	list_filter   = ('consultant','status','account','site','week_end','st_hrs','ot_hrs','dt_hrs','nb_hrs','other_hrs','notes')
	fields        = ('consultant','status','account','site','week_end','st_hrs','ot_hrs','dt_hrs','nb_hrs','other_hrs','notes')

class HoursAdmin(ImportExportModelAdmin):
	list_display  = ('id','hours','hours_desc')
	search_fields = ('hours','hours_desc')
	list_filter   = ('hours','hours_desc')
	fields        = ('hours','hours_desc')
class EmpTypeAdmin(ImportExportModelAdmin):
	list_display  = ('id','emp_type','emp_type_desc')
	search_fields = ('emp_type','emp_type_desc')
	list_filter   = ('emp_type','emp_type_desc')
	fields        = ('emp_type','emp_type_desc')
class CategoryAdmin(ImportExportModelAdmin):
	list_display  = ('id','category','category_desc')
	search_fields = ('category','category_desc')
	list_filter   = ('category','category_desc')
	fields        = ('category','category_desc')
class PriorityAdmin(ImportExportModelAdmin):
	list_display  = ('id','priority','priority_desc')
	search_fields = ('priority','priority_desc')
	list_filter   = ('priority','priority_desc')
	fields        = ('priority','priority_desc')
class ReqStatusAdmin(ImportExportModelAdmin):
	list_display  = ('id','req_status','req_status_desc')
	search_fields = ('req_status','req_status_desc')
	list_filter   = ('req_status','req_status_desc')
	fields        = ('req_status','req_status_desc')

class ClientAdmin(ImportExportModelAdmin):
	list_display  = ('id','client','client_desc')
	search_fields = ('client','client_desc')
	list_filter   = ('client','client_desc')
	fields        = ('client','client_desc')



admin.site.register(Party, PartyAdmin)
admin.site.register(Party_Skill, Party_SkillAdmin)
admin.site.register(Requisition, RequisitionAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Submittal, SubmittalAdmin)
admin.site.register(TimeSheet, TimeSheetAdmin)

admin.site.register(Hours, HoursAdmin)
admin.site.register(EmpType, EmpTypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Priority, PriorityAdmin)
admin.site.register(ReqStatus, ReqStatusAdmin)
admin.site.register(Client, ClientAdmin)
