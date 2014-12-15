from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
class Skill(models.Model):
    id = models.AutoField(primary_key = True)
    skill_name = models.CharField(max_length=256)
    skill_desc = models.CharField(max_length=1024, blank=True, null=True)
    skill_catagory = models.CharField(max_length=45)
 
    def __unicode__(self):
        return u'%s' % self.skill_name
    
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skill'
 
class Party_Skill(models.Model):
    id = models.AutoField(primary_key = True)
    skill = models.ForeignKey(Skill)
    skill_lvl = models.CharField(max_length=45, blank=True, null=True)
    skill_start_date = models.DateField(blank=True, null=True)
    skill_year = models.IntegerField(blank=True, null=True)
    skill_notes = models.CharField(max_length=1024, blank=True, null=True)
   
    def toJSON(self):
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])
 
    def __unicode__(self):
        return u'%s' % self.skill

    class Meta:
        verbose_name = 'Party_Skill'
        verbose_name_plural = 'Party_Skill'

class Party(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, blank=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(verbose_name='e-mail', blank=True)
    phone = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=256, blank=True)
    state = models.CharField(max_length=45, blank=True)
    zip = models.IntegerField(max_length=10, blank=True)
    visa_status = models.CharField(max_length=45, blank=True)
    portfolio_link = models.CharField(max_length=256, blank=True)
    linkedin = models.URLField(blank=True)
    source = models.CharField(max_length=256, blank=True)
    resume_link = models.URLField(blank=True)
    ts_update = models.DateField(blank=True, null=True)
    skills = models.ManyToManyField(Party_Skill, blank=True, null=True)
 
    def candidate_skills(self):
        return "\n".join([s.skill.skill_name for s in self.skills.all()])
 
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
   
    def toJSON(self):
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])
 
    def formatting(self):
        self.first_name = self.first_name.title().strip()
        self.last_name = self.last_name.title().strip()
        self.city = self.city.title().strip()
        self.state = self.state.upper().strip()
        self.save()

    class Meta:
        verbose_name = 'Party'
        verbose_name_plural = 'Party'
 
class Hours(models.Model):
    id = models.AutoField(primary_key = True)
    hours = models.CharField(max_length=45)
    hours_desc = models.CharField(max_length=1024, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.hours

    class Meta:
        verbose_name = 'Hours'
        verbose_name_plural = 'Hours'

class EmpType(models.Model):
    id = models.AutoField(primary_key = True)
    emp_type = models.CharField(max_length=45)
    emp_type_desc = models.CharField(max_length=1024, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.emp_type

    class Meta:
        verbose_name = 'EmpType'
        verbose_name_plural = 'EmpType'

class Category(models.Model):
    id = models.AutoField(primary_key = True)
    category = models.CharField(max_length=45)
    category_desc = models.CharField(max_length=1024, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.category

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

class Priority(models.Model):
    id = models.AutoField(primary_key = True)
    priority = models.CharField(max_length=45)
    priority_desc = models.CharField(max_length=1024, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.priority

    class Meta:
        verbose_name = 'Priority'
        verbose_name_plural = 'Priority'

class ReqStatus(models.Model):
    id = models.AutoField(primary_key = True)
    req_status = models.CharField(max_length=45)
    req_status_desc = models.CharField(max_length=1024, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.req_status

    class Meta:
        verbose_name = 'ReqStatus'
        verbose_name_plural = 'ReqStatus'

class Client(models.Model):
    id = models.AutoField(primary_key = True)
    client = models.CharField(max_length=45)
    client_desc = models.CharField(max_length=1024, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.client

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Client'

class Requisition(models.Model):
    id = models.AutoField(primary_key = True)
    req_date = models.DateField(blank=True, null=True)
    req_status = models.ForeignKey(ReqStatus)
    client = models.ForeignKey(Client, blank=True, null=True)
    recruiter = models.ForeignKey(Party, blank=True, null=True)
    job_id = models.CharField(max_length=45,blank=True, null=True)
    job_title = models.CharField(max_length=225,blank=True, null=True)
    emp_type = models.ForeignKey(EmpType, blank=True, null=True)
    hours = models.ForeignKey(Hours, blank=True, null=True)
    loc = models.CharField(max_length=45,blank=True, null=True)
    duration = models.CharField(max_length=45,blank=True, null=True)
    rate = models.CharField(max_length=45, blank=True, null=True)
    openings = models.IntegerField(blank=True, null=True)
    job_description = models.TextField(max_length=20000, blank=True, null=True)
    req_contact = models.CharField(max_length=45, blank=True, null=True)
    req_contact_notes = models.TextField(max_length=20000,blank=True, null=True)
    city = models.CharField(max_length=45,blank=True, null=True)
    state = models.CharField(max_length=45,blank=True, null=True) 
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    req_approved = models.DateField(blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    priority = models.ForeignKey(Priority, blank=True, null=True)
    keywords = models.ManyToManyField(Skill, blank=True, null=True)

   
 
    def __unicode__(self):
        return u'%s' % self.job_id
 
    def get_keywords(self):
        return "\n".join([s.skill_name for s in self.keywords.all()])
 
    def toJSON(self):
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])
   
    def formatting(self):
        self.job_title = self.job_title.title().strip()
        self.city = self.city.title().strip()
        self.req_contact = self.req_contact.title().strip()
        self.loc = self.loc.upper().strip()
        self.state = self.state.upper().strip()
        self.save()
 
    class Meta:
        verbose_name = 'Requisition'
        verbose_name_plural = 'Requisition'

 
 
class Submittal(models.Model):
    id = models.AutoField(primary_key = True)
    candidate = models.ForeignKey(Party, related_name='candidate')
    recruiter = models.ForeignKey(Party, related_name='recruiter')
    job_id = models.ForeignKey(Requisition)
    date = models.DateTimeField(auto_now_add=True)
    hourly_rate = models.CharField(max_length=45)
    current_year_rate = models.CharField(max_length=45)
    expected_year_rate = models.CharField(max_length=45)
    interview_available = models.CharField(max_length=45)
    start_available = models.CharField(max_length=45)
    interview_feedback = models.TextField(max_length=1000)
    status = models.CharField(max_length=45)
    interview_date = models.DateField()
 
    class Meta:
        verbose_name = 'Submittal'
        verbose_name_plural = 'Submittal'

class TimeSheet(models.Model):
    id = models.AutoField(primary_key = True)
    consultant = models.ForeignKey(Party)
    status = models.CharField(max_length=45)
    account = models.CharField(max_length=45)
    site = models.CharField(max_length=45)
    week_end = models.DateField()
    st_hrs = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    ot_hrs = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    dt_hrs = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    nb_hrs = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    other_hrs = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    notes = models.TextField(max_length=20000, blank=True, null=True)


    class Meta:
        verbose_name = 'TimeSheet'
        verbose_name_plural = 'TimeSheet'
