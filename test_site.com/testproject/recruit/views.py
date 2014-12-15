from recruit.models import  Requisition, Skill, Party, Party_Skill, Submittal, TimeSheet, Hours, EmpType, Category, Priority, ReqStatus, Client

from django.shortcuts import render_to_response,render, get_object_or_404 
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib.auth.models import User 
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required

from recruit.forms import LoginForm, RegistrationForm

import datetime

'''
Register, Login & Logout
'''
def register(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render_to_response('register.html', RequestContext(request, {'form' : form,}))
    else:
        form = RegistrationForm(request.POST)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password2']
        email = form.cleaned_data['email']
        if form.is_valid():
            user = User.objects.create_user(
                username = username,
                password = password,
                email = email
                )
            return HttpResponseRedirect('/login/')
        else:
            form = RegistrationForm()
            variable = RequestContext(request, {'form' : form})
            return render_to_response('register.html', variable)

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.html', RequestContext(request, {'form' : form,}))
    else :
        form = LoginForm(request.POST)
    if form.is_valid():
        username = request.POST.get('username', '')
        if username:
            request.session['username'] = username
            username = request.session.get('username','')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                if user.is_staff:
                    return HttpResponseRedirect('/requisition/')
                else:
                    return HttpResponseRedirect('/requisition_cu/')
            else :
                return render_to_response('login.html', RequestContext(request, {'form' : form, 'password_is_wrong' : True}))
        else :
            return render_to_response('login.html', RequestContext(request, {'form' : form,}))

@login_required
def logout(request):
    try:
        del request.session['username']
        auth.logout(request)
    except KeyError:
        pass
    return HttpResponseRedirect("/login")


'''
List for every table
'''
def datediff(begin, end):
    oneday = datetime.timedelta(days=1)
    count = 0
    while begin != end:
        end = end - oneday
        count += 1
    return count


@login_required
def requisitionlist(request):
    try:
        all_info = Requisition.objects.all()
        data = {}
        data['draw'] = 1
        data['recordsTotal'] = '%s' % len(all_info)
        data['recordsFiltered'] = '%s' % len(all_info)
        data['data'] = []
        i = 1
        for info in all_info:
            tmp_list = []
            info_json = {}
            info_json['DT_RowId']  = 'row_%d' % i;
            info_json['id']        = '%s' % info.id
            info_json['job_id']    = '%s' % info.job_id.encode("utf-8")
            info_json['job_title'] = '%s' % info.job_title.encode("utf-8")
            info_json['category']  = '%s' % info.category
            info_json['emp_type']  = '%s' % info.emp_type
            info_json['hours']     = '%s' % info.hours
            info_json['recruiter'] = '%s' % info.recruiter
            info_json['priority']  = '%s' % info.priority
            info_json['req_status']= '%s' % info.req_status
            info_json['req_date']  = '%s' % info.req_date
            info_json['req_approved'] = '%s' % info.req_approved
            if info_json['req_status'] == 'Submitted' and info.req_approved != None:
                today = datetime.date.today()
                days_left = datediff(info.req_approved, today)
                info_json['days_left'] = '%s' % days_left
            else:
                info_json['days_left'] = 'None'
            info_json['loc']        = '%s' % info.loc.encode("utf-8")
            info_json['city']       = '%s' % info.city.encode("utf-8")
            info_json['state']      = '%s' % info.state.encode("utf-8")
            info_json['start_date'] = '%s' % info.start_date
            info_json['end_date']   = '%s' % info.end_date
            info_json['duration']   = '%s' % info.duration.encode("utf-8")
            info_json['rate']       = '%s' % info.rate.encode("utf-8")
            info_json['job_description']   = '%s' % '<br/>' + info.job_description.replace('\n', '<br/>').encode("utf-8")
            info_json['req_contact']       = '%s' % info.req_contact.replace('\n', '<br/>').encode("utf-8")
            info_json['req_contact_notes'] = '%s' % '<br/>' + info.req_contact_notes.replace('\n', '<br/>').encode("utf-8")
            info_json['openings'] = '%s' % info.openings
            for skill in info.keywords.all():
                tmp_list.append(skill.skill_name)
            info_json['keywords'] = '%s' % '<br>'. join(tmp_list).encode("utf-8")
            info_json['client']   = '%s' % info.client
            data['data'].append(info_json)
            i += 1
        ## process filter :
        fdict = {}
        fdict['job_title'] = list(set([x.job_title for x in all_info]))
        fdict['loc'] = list(set([x.loc for x in all_info]))
        fdict['city'] = list(set([x.city for x in all_info]))
        fdict['req_contact'] = list(set([x.req_contact for x in all_info]))
        fdict['state'] = list(set([x.state for x in all_info]))
        fdict['recruiter'] = list(set([x.recruiter for x in all_info]))

        ps = []
        for x in Party.objects.all():
            if x.user.is_staff:
                ps.append(x)

        return render_to_response('requisition.html', {'name' : request.user, 
                                                       'data': str(data), 
                                                       'fdict': fdict, 
                                                       'keywords':Skill.objects.all(), 
                                                       'hours' : Hours.objects.all(),
                                                       'empType' : EmpType.objects.all(),
                                                       'category' : Category.objects.all(),
                                                       'priority' : Priority.objects.all(),
                                                       'reqStatus' : ReqStatus.objects.all(),
                                                       'client' : Client.objects.all(),
                                                       'party': ps})
    except Exception, e:
        print e
        return HttpResponseRedirect("/login")


@login_required
def requisition_cu_list(request):
    try:
        a = 2
        return render_to_response('requisition_cu.html', {'name' : request.user, 'a' : a})
    except Exception, e:
        print e
        return HttpResponseRedirect("/login")

@login_required
def partylist(request):
    try:
        all_info = Party.objects.all()
        data = {}
        data['draw'] = 1
        data['recordsTotal'] = '%s' % len(all_info)
        data['recordsFiltered'] = '%s' % len(all_info)
        data['data'] = []
        i = 1
        for info in all_info:
            info_json = {}
            info_json['DT_RowId']       = 'row_%d' % i;
            info_json['id']             = '%s' % info.id
            info_json['type']           = '%s' % info.type.encode("utf-8")
            info_json['first_name']     = '%s' % info.first_name.encode("utf-8")
            info_json['last_name']      = '%s' % info.last_name.encode("utf-8")
            info_json['email']          = '%s' % info.email.encode("utf-8")
            info_json['phone']          = '%s' % info.phone.encode("utf-8")
            info_json['address']        = '%s' % info.address.encode("utf-8")
            info_json['city']           = '%s' % info.city.encode("utf-8")
            info_json['state']          = '%s' % info.state.encode("utf-8")
            info_json['zip']            = '%s' % info.zip
            info_json['visa_status']    = '%s' % info.visa_status.encode("utf-8")
            info_json['portfolio_link'] = '%s' % info.portfolio_link.encode("utf-8")
            info_json['linkedin']       = '%s' % info.linkedin.encode("utf-8")
            info_json['source']         = '%s' % info.source.encode("utf-8")
            info_json['resume_link']    = '%s' % info.resume_link.encode("utf-8")
            info_json['ts_update']      = '%s' % info.ts_update
            #manytomany
            info_json['skills']         = '%s' % info.candidate_skills().replace('\n', '<br/>').encode("utf-8")

            submittallist = Submittal.objects.filter(candidate = info)
            if len (submittallist) != 0 and submittallist is not None :
                alist = []
                for x in submittallist:
                    alist.append(str(x.job_id))
                info_json['job_ids'] =  '%s' % '<br/>'.join(alist)
            else :
                info_json['job_ids'] = ''


            data['data'].append(info_json)
            i += 1
        return render_to_response('candidate.html', {'name' : request.user, 'data': str(data), 'all_objects' : all_info, 'skills': Skill.objects.all(), 'requisition': Requisition.objects.all(), 'party': Party.objects.all()})
    except Exception, e:
        print e
        return HttpResponseRedirect("/login")

@login_required
def submittallist(request):
    try:
        all_info = Submittal.objects.all()
        data = {}
        data['draw'] = 1
        data['recordsTotal'] = '%s' % len(all_info)
        data['recordsFiltered'] = '%s' % len(all_info)
        data['data'] = []
        i = 1
        for info in all_info:
            info_json = {}
            info_json['DT_RowId']               = 'row_%d' % i;
            info_json['id']                 = '%s' % info.id
            #this two element come from one foreignkey(Party)
            info_json['candidate']          = '<font style="color:#2157b1;">%s</font>' % info.candidate
            info_json['recruiter']          = '<font style="color:#2157b1;">%s</font>' % info.recruiter

            #foreignkey(Requisition)
            info_json['job_id']         = '<font style="color:#2157b1;">%s</font>' % info.job_id
                
            info_json['date']               = '%s' % info.date
            info_json['hourly_rate']        = '%s' % info.hourly_rate.encode("utf-8")
            info_json['current_year_rate']  = '%s' % info.current_year_rate.encode("utf-8")
            info_json['expected_year_rate'] = '%s' % info.expected_year_rate.encode("utf-8")
            info_json['interview_available']    = '%s' % info.interview_available.encode("utf-8")
            info_json['start_available']        = '%s' % info.start_available.encode("utf-8")
            info_json['interview_feedback'] = '%s' % '<br/>' + info.interview_feedback.replace('\n', '<br/>').encode("utf-8")
            info_json['status']             = '%s' % info.status.encode("utf-8")
            info_json['interview_date']     = '%s' % info.interview_date


            data['data'].append(info_json)
            i += 1
        return render_to_response('submittal.html', {'name' : request.user, 'data': str(data), 'all_objects' : all_info, 'party': Party.objects.all(), 'requisition': Requisition.objects.all()})
    except Exception, e:
        print e
        return HttpResponseRedirect("/login")
'''
TimeSheet unfinished
'''
# @login_required
# def timesheetlist(request):
#     try:
#         all_info = TimeSheet.objects.all()
#         data = {}
#         data['draw'] = 1
#         data['recordsTotal'] = '%s' % len(all_info)
#         data['recordsFiltered'] = '%s' % len(all_info)
#         data['data'] = []
#         i = 1
#         for info in all_info:
#             info_json = {}
#             info_json['DT_RowId']  = 'row_%d' % i;
#             info_json['id']        = '%s' % info.id
    
#             #foreignkey(Party)
#             info_json['consultant']= '%s' % info.consultant
#             info_json['status']    = '%s' % info.status.encode("utf-8")
#             info_json['account']   = '%s' % info.account.encode("utf-8")
                
#             info_json['site']      = '%s' % info.site.encode("utf-8")
#             info_json['week_end']  = '%s' % info.week_end
#             info_json['st_hrs']    = '%s' % info.st_hrs
#             info_json['ot_hrs']    = '%s' % info.ot_hrs
#             info_json['dt_hrs']    = '%s' % info.dt_hrs
#             info_json['nb_hrs']    = '%s' % info.nb_hrs
#             info_json['other_hrs'] = '%s' % info.status
#             info_json['notes']     = '%s' % '<br/>' + info.notes.replace('\n', '<br/>').encode("utf-8")


#             data['data'].append(info_json)
#             i += 1
#         return render_to_response('timesheet.html', {'name' : request.user, 'data': str(data), 'all_objects' : all_info, 'party': Party.objects.all()})
#     except Exception, e:
#         print e
#         return HttpResponseRedirect("/login")

# @login_required
# def add_timesheet_consultant(request):
#     try:
#         consultant = request.POST.get('consultant', '')
#         status     = request.POST.get('status', '')
#         account    = request.POST.get('account', '')
#         site       = request.POST.get('site', '')
#         week_end   = request.POST.get('week_end', '')
        
#         new_submittal = Submittal(consultant = Party.objects.get(id=consultant),\
#                                   status = status, \
#                                   site = site,\
#                                   week_end = hourly_rate)
#         new_submittal.save()
#         c = Requisition.objects.get(id=ipg_req_id)
#         c.status = 'Submitted'
#         c.approved_date = new_submittal.date
#         c.save()
#         return HttpResponseRedirect("/submittal/")
#     except Exception, e:
#         print e
#         return HttpResponseRedirect("/login")


# @login_required
# def add_timesheet_time(request):
#     try:
#         candidate           = request.POST.get('candidate', '')
#         recruiter           = request.POST.get('recruiter', '')
#         ipg_req_id          = request.POST.get('ipg_req_id', '')
#         hourly_rate         = request.POST.get('hourly_rate', '')
#         current_year_rate   = request.POST.get('current_year_rate', '')
#         expected_year_rate  = request.POST.get('expected_year_rate', '')
#         interview_available = request.POST.get('interview_available', '')
#         start_available     = request.POST.get('start_available', '')
#         interview_feedback  = request.POST.get('interview_feedback', '')
#         status              = request.POST.get('status', '')
#         interview_date      = request.POST.get('interview_date', '')
#         new_submittal = Submittal(candidate = Party.objects.get(id=candidate),\
#                                   recruiter = Party.objects.get(id=recruiter), \
#                                   ipg_req_id = Requisition.objects.get(id=ipg_req_id),\
#                                   hourly_rate = hourly_rate, \
#                                   current_year_rate = current_year_rate,\
#                                   interview_available = interview_available,
#                                   start_available = start_available,\
#                                   interview_feedback = interview_feedback, \
#                                   status = status, \
#                                   interview_date = interview_date)
#         new_submittal.save()
#         c = Requisition.objects.get(id=ipg_req_id)
#         c.status = 'Submitted'
#         c.approved_date = new_submittal.date
#         c.save()
#         return HttpResponseRedirect("/submittal/")
#     except Exception, e:
#         print e
#         return HttpResponseRedirect("/login")

'''
Add data for every table
'''
@login_required
def add_party(request):
    try:
        t               = request.POST.get('type', '')
        first_name      = request.POST.get('first_name', '')
        last_name       = request.POST.get('last_name', '')
        email           = request.POST.get('email', '')
        phone           = request.POST.get('phone', '')
        address         = request.POST.get('address', '')
        city            = request.POST.get('city', '')
        state           = request.POST.get('state', '')
        zip             = request.POST.get('zip', 0)
        visa_status     = request.POST.get('visa_status', '')
        portfolio_link  = request.POST.get('portfolio_link', '')
        linkedin        = request.POST.get('linkedin', '')
        source          = request.POST.get('source', '')
        resume_link     = request.POST.get('resume_link', '')
        ts_update       = request.POST.get('ts_update', '')

        new_party       = Party(type=t, \
                                first_name=first_name, \
                                last_name=last_name, \
                                email=email, \
                                phone=phone, \
                                address=address, \
                                user = request.user, \
                                city=city, \
                                state=state, \
                                zip=zip, \
                                visa_status=visa_status, \
                                portfolio_link=portfolio_link, \
                                linkedin=linkedin, \
                                source=source, \
                                resume_link=resume_link, \
                                ts_update=ts_update
                                )
        new_party.save()
        for (k, v) in request.POST.items():
            if k.find('skill_name') != -1:
                skill = Skill.objects.get(skill_name=v.strip())
                new_pk = Party_Skill(skill = skill, \
                                     skill_lvl = request.POST.get('skill_lvl%s' % k[10:], ''), \
                                     skill_start_date = request.POST.get('skill_start_date%s' % k[10:], ''), \
                                     skill_year = request.POST.get('skill_year%s' % k[10:], ''), \
                                     skill_notes = request.POST.get('skill_notes%s' % k[10:], '')
                                    )
                new_pk.save()
                new_party.skills.add(new_pk)
        new_party.save()
        new_party.formatting()
        return HttpResponseRedirect("/candidate")
    except Exception, e:
        print e
        return HttpResponseRedirect("/login")

@login_required
def add_submittal(request):
    try:
        candidate           = request.POST.get('candidate', '')
        recruiter           = request.POST.get('recruiter', '')
        job_id          = request.POST.get('job_id', '')
        hourly_rate         = request.POST.get('hourly_rate', '')
        current_year_rate   = request.POST.get('current_year_rate', '')
        expected_year_rate  = request.POST.get('expected_year_rate', '')
        interview_available = request.POST.get('interview_available', '')
        start_available     = request.POST.get('start_available', '')
        interview_feedback  = request.POST.get('interview_feedback', '')
        status              = request.POST.get('status', '')
        interview_date      = request.POST.get('interview_date', '')
        new_submittal = Submittal(candidate = Party.objects.get(id=candidate),\
                                  recruiter = Party.objects.get(id=recruiter), \
                                  job_id = Requisition.objects.get(id=job_id),\
                                  hourly_rate = hourly_rate, \
                                  current_year_rate = current_year_rate,\
                                  interview_available = interview_available,
                                  start_available = start_available,\
                                  interview_feedback = interview_feedback, \
                                  status = status, \
                                  interview_date = interview_date)
        new_submittal.save()
        c = Requisition.objects.get(id=job_id)
        c.status = 'Submitted'
        c.approved_date = new_submittal.date
        c.save()
        return HttpResponseRedirect("/submittal/")
    except Exception, e:
        print e
        return HttpResponseRedirect("/login")


@login_required
def add_requisition(request):
    try:
        if request.method == 'POST':
            job_id              = request.POST.get('job_id', '')
            job_title      = request.POST.get('job_title', '')
            category_id            = request.POST.get('category', 0)
            if category_id == 0:
                category = None
            else :
                category = Category.objects.get(id=category_id)

            loc                 = request.POST.get('loc', '')
            city                = request.POST.get('city', '')
            state               = request.POST.get('state', '')
            start_date          = request.POST.get('start_date', '')
            end_date            = request.POST.get('end_date', '')
            duration            = request.POST.get('duration', '')
            rate                = request.POST.get('rate', '')
            job_description     = request.POST.get('job_description', '')
            req_contact            = request.POST.get('req_contact', '')
            req_contact_notes      = request.POST.get('req_contact_notes', '')
            number_of_openings  = request.POST.get('openings', 0)
            keywords            = request.POST.get('keywords', '')
            client_id           = request.POST.get('client', 0)
            if client_id == 0:
                client = None 
            else :
                client = Client.objects.get(id=client_id)
            req_date            = request.POST.get('req_date', '')
            req_status_id       = request.POST.get('req_status', 0)
            if req_status_id == 0:
                req_status = None 
            else :
                req_status = ReqStatus.objects.get(id=req_status_id)
            recruiter_id        = request.POST.get('recruiter', 0)
            if recruiter_id == 0:
                recruiter = None 
            else :
                recruiter = Party.objects.get(id=recruiter_id)
            emp_type_id         = request.POST.get('emp_type', 0)
            if emp_type_id == 0:
                emp_type = None 
            else :
                emp_type = EmpType.objects.get(id=emp_type_id)
            hours_id            = request.POST.get('hours', 0)
            if hours_id == 0:
                hours = None 
            else :
                hours = Hours.objects.get(id=hours_id)
            req_approved        = request.POST.get('req_approved', '')
            priority_id         = request.POST.get('priority', 0)
            if priority_id == 0:
                priority = None 
            else :
                priority = Priority.objects.get(id=priority_id)


            new_requesion = Requisition(job_id = job_id, \
                                        recruiter = recruiter, \
                                        req_date = req_date,\
                                        emp_type = emp_type,\
                                        job_title=job_title,  \
                                        category=category, \
                                        req_status=req_status, \
                                        loc=loc, \
                                        city=city, \
                                        state=state,\
                                        duration=duration, \
                                        rate=rate, \
                                        job_description=job_description,\
                                        req_contact=req_contact, \
                                        req_contact_notes=req_contact_notes,\
                                        openings=number_of_openings, \
                                        client=client,\
                                        start_date=start_date, \
                                        end_date=end_date,\
                                        req_approved = req_approved,\
                                        priority = priority,\
                                        hours = hours
                                        )
            new_requesion.save()
            for skill in keywords.split(','):
                rs = Skill.objects.filter(skill_name=skill.strip(' '))
                if len(rs) != 0:
                    new_requesion.keywords.add(rs[0])
            new_requesion.save()
            new_requesion.formatting()

            return HttpResponseRedirect("/requisition/")
        else:
            raise Exception("forbbiden")
    except Exception, e:
        print e
        return HttpResponseRedirect("/login")



'''
Get data for every table to help other function
'''
@login_required
def get_requisition(request):
    """
    """
    try:
        data={}
        id = request.GET.get('id', 0)
        if id == 0:
            raise Exception(" error")
        sobj = Submittal.objects.get(id=id)
        obj = sobj.job_id
        js = obj.toJSON()
        unneed = ['type', 'category', 'rate', 'duration', 'job_desc', 'req_contact_notes']
        data['data'] = []
        for (k, v) in js.items():
            if k not in unneed: 
                tmp = []
                tmp.append(k)
                tmp.append(str(v).encode("utf-8"))
                data['data'].append(tmp)
        return HttpResponse(str(data).encode("utf-8").replace('\'', '\"'))
    except Exception, e:
        print e
        return HttpResponseRedirect("/login")


@login_required
def get_candidate(request):
    """
    """
    try:
        data={}
        id = request.GET.get('id', 0)
        if id == 0:
            raise Exception(" error")
        sobj = Submittal.objects.get(id=id)
        obj = sobj.candidate
        js = obj.toJSON()
        
        data['data'] = []
        for (k, v) in js.items():
            tmp = []
            tmp.append(k)
            tmp.append(str(v).encode("utf-8"))
            data['data'].append(tmp)
        return HttpResponse(str(data).encode("utf-8").replace('\'', '\"'))
    except Exception, e:
        print e
        return HttpResponseRedirect("/login")


@login_required
def get_recruiter(request):
    """
    """
    try:
        data={}
        id = request.GET.get('id', 0)
        if id == 0:
            raise Exception(" error")
        sobj = Submittal.objects.get(id=id)
        obj = sobj.recruiter
        js = obj.toJSON()
        
        data['data'] = []
        for (k, v) in js.items():
            tmp = []
            tmp.append(k)
            tmp.append(str(v).encode("utf-8"))
            data['data'].append(tmp)
        return HttpResponse(str(data).encode("utf-8").replace('\'', '\"'))
    except Exception, e:
        print e
        return HttpResponseRedirect("/login")


@login_required
def get_party_skill(request):
    """
    """
    try:
        print 'get_party_skill'
        id = request.GET.get('id', default = 0)
        if id == 0 :
            raise Exception(" error")
        pobj = Party.objects.get(id=id)
        objs = pobj.skills.all()
        data = {}
        data['data'] = []
        for pskill in objs:
            tmp = []
            tmp.append(str(pskill.id))
            tmp.append(str(pskill.skill.skill_name))
            tmp.append(str(pskill.skill_lvl))
            tmp.append(str(pskill.skill_start_date))
            tmp.append(str(pskill.skill_year))
            tmp.append(str(pskill.skill_notes))
            data['data'].append(tmp)
        return HttpResponse(str(data).encode("utf-8").replace('\'', '\"'))   
    except Exception, e:
        print e
        return HttpResponseRedirect("/login")


@login_required
def get_skill(request):
    """
    """
    try:
        id = request.GET.get('id', default=0)

        if id == 0 :
            raise Exception(" error")
        robjs = Requisition.objects.get(id=id)
        objs = robjs.keywords.all()
        data = {}
        data['data'] = []
        for s in objs:
            tmp = []
            tmp.append(str(s.id))
            tmp.append(str(s.skill_name))
            tmp.append(str(s.skill_desc))
            tmp.append(str(s.skill_catagory))
            data['data'].append(tmp)
        return HttpResponse(str(data).encode("utf-8").replace('\'', '\"'))   
    except Exception, e:
        print e
        return HttpResponseRedirect("/login")

@login_required
def get_submittal_tarck(request):
    """
    """
    try:
        id = request.GET.get('id', default=0)
        if id == 0 :
            raise Exception(" error")
        robjs = Party.objects.get(id=id)
        

        objs = Submittal.objects.filter(candidate=robjs)
        data = {}
        data['data'] = []
        for s in objs:
            tmp = []
            tmp.append(str(s.job_id))
            tmp.append(str(s.job_id.position_title))
            tmp.append(str(s.recruiter))
            tmp.append(str(s.date))
            data['data'].append(tmp)
        return HttpResponse(str(data).encode("utf-8").replace('\'', '\"'))   
    except Exception, e:
        print e
        return HttpResponseRedirect("/login")

# @login_required
# def changepwd(request):
#     if request.method == 'GET':
#         form = ChangepwForm()
#         return render_to_response('changepwd.html', RequestContext(request, {'form' : form,}))
#     else:
#         form = ChangepwForm(request.POST)
#         if form.is_valid():
#             username = request.uer.username
#             old_password = request.POST.get('old_password', '')
#             user = auth.authenticate(username=username, password=old_password)
#       if user is not None and user.is_active:
#           new_password = request.POST.get('new_password', '')
#       user.set_password(new_password)
#           user.save()
#       return render_to_response('index.html', RequestContext(request, {'changepwd_success' : True}))
#             else :
#       return render_to_response('changepwd.html', RequestContext(request, {'form' : form, 'old_password_is_wrong' : True}))
#   else :
#       return render_to_response('changepwd.html', RequestContext(request, {'form' : form,}))


