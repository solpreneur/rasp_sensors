from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
#user auth
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.password_validation import password_validators_help_texts
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
#forms
from .forms import LoginForm
#object manipulation fxns
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView
#models
from .models import Reading, ReadingTypes

import json
from datetime import date
from django.contrib import messages
from django.db import connection
from .utils import getTypeDetails
from django.http import JsonResponse
from django.core.paginator import Paginator
from urllib.parse import urlencode

# Create your views here.
def login_view(request):
    # if user is already signed in prevent from seeing this page
    if request.user.is_authenticated: 
        return redirect('dashboard')

    #process user submitted form details
    if request.method == 'POST':

        form = LoginForm(request.POST or None)
    
        # authenticate user
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember = request.POST.get('remember')

            user = authenticate(request, username=username, password=password)

            if user != None:
                #log user in
                login(request, user)

                if remember == '1':  # keep user logged in for one day
                    period = 24 * 60 * 60
                    request.session.set_expiry(period)
                    # print(request.session.get_expiry_age())

                if request.user.is_active and request.user.is_staff:
                    return redirect('/admin/')  # redirect to default admin page if user is admin
                return redirect(reverse('dashboard'))
            else:
                # set error message for false credentials
                messages.error(request, 'Invalid Login credentials', extra_tags='alert')
                return render(request, 'htc/login.html', {'form': form, })
        else:

            messages.error(request, 'Invalid Login credentials', extra_tags='alert')
            return render(request, 'htc/login.html', {'form': form, })

    else:

        # check first to see if user is already signed in
        if not request.user.is_authenticated:  

            # create new empty form and send to view
            form = LoginForm()  
            return render(request, 'htc/login.html', {'form': form,})

    #redirect user to Dashboard if logged in already
    return render(request, 'htc/dashboard.html', {'user': User})

@login_required
def logout_view(request):
    logout(request)
    form = LoginForm()  # create new empty form and send to view
    return render(request, 'htc/login.html', {'form': form, })

@login_required
def dashboard(request):
    return render(request,'htc/dashboard.html')

#returns last known reading of any reading type
@login_required 
def reading(request,reading_type=None):
    if request.method == 'GET' and reading_type != None:

        #get query set containing data for reading type including ID which I need below 
        typ_details = ReadingTypes.objects.filter(reading_type=reading_type.capitalize())

        #make sure we actually got some data
        if len(typ_details) > 0 :
            #get  reading QuerySet for today, DESC order
            reading= Reading.objects.filter(read_type_id=typ_details.values()[0]['id']).order_by('-date_time')
        
            #if query set != empty
            if len(reading) > 0 : 
                return JsonResponse(reading.values()[0],safe=False)
            #nothing found
            else: return JsonResponse({'message':'No data available'})

        #nothing found
        else : return JsonResponse({'message':'Required type not found'})

    #reading type and other info needed was not given
    return JsonResponse({'message':'Failed. Required value not provided'})



#return reading for the day so far
@login_required
def read_day(request,reading_type=None):
    if request.method == 'GET' and reading_type != None:

        #get query set containing data for reading type including ID which I need below 
        typ_details = ReadingTypes.objects.filter(reading_type=reading_type.capitalize())

        #make sure we actually got some data
        if len(typ_details) > 0 :
            
            #get  reading QuerySet for today
            reading= Reading.objects.filter(read_type_id=typ_details.values()[0]['id'],date_time__gte=date.today() ).order_by('date_time')
           
            #if query set != empty
            if len(reading) > 0 :
                #convert object to list of dicts 
                resp = [data for data in reading.values() ]
                return JsonResponse(resp,safe=False)
            #nothing found
            else: return JsonResponse({'message':'No data available'})

        #nothing found
        else : return JsonResponse({'message':'Required type not found'})

    #reading type and other info needed was not given
    return JsonResponse({'message':'Failed. Reading Type not provided'})



#display all records, of partial records based on user filter criteria
@login_required
def readings(request):
    #get query set containing data for reading type including ID which I need below 
    #always sent, needed for select field
    types =  [option for option in ReadingTypes.objects.all().values()] #query 1

    
    filter_arguments = {} #for filtering data base on date, time, type
    filtered_data    = None 
    paginated_data   = None
    page             = None

    #data needed in case user add filters and results have morethan 1 page, we need this to loop through the proper pages
    url_params        = {}

    #filter options
    rtype          = request.GET.get('rtype')
    start_datetime = request.GET.get('start_datetime')
    end_datetime   = request.GET.get('end_datetime')
    page_num       = request.GET.get('page')

    if request.method == 'GET':
        #add respective filter params
        if rtype != '' and rtype != None  and rtype != 'all': 
            filter_arguments['read_type_id']= rtype
            url_params['rtype']= rtype
        
        if  start_datetime != '' and start_datetime != None:
            filter_arguments['date_time__gte']=start_datetime
            url_params['start_datetime']= start_datetime

        if  end_datetime != '' and end_datetime != None:
            filter_arguments['date_time__lte']=end_datetime
            url_params['end_datetime']= end_datetime
        

    #check, have any filters been set at all
    if bool(filter_arguments):  
        #yes, then run query with filters
        filtered_data = Reading.objects.filter(**filter_arguments).values() #query 2
    else:
        #no filters, get all data
        filtered_data = Reading.objects.all().order_by('-date_time').values() #query 3

    #create pagination
    paginated_data    = Paginator(filtered_data, 25) # Show 25 contacts per page.

    #if next page or page number is given, display corresponding filtered data page
    if page_num != '':
        page = paginated_data.get_page(page_num)

    #additional url data to send
    query_str = ''
    if bool(url_params):
        query_str = urlencode(url_params, doseq=True)

    return render(request, 'htc/readings.html', {'types':types,'readings':page,'query_str':query_str})