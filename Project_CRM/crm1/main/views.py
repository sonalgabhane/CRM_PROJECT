from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from Useraccount.models import User
from django.views import generic
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import LeadModelSerializer, CustomerModelSerializer, SupplierModelSerializer, SightseeingModelSerializer
from .serializers import HotelModelSerializer, PackageModelSerializer, UserModelSerializer, VehicleModelSerializer
from rest_framework import status
from django.contrib.auth.decorators import login_required
from .forms import *
from Useraccount.forms import UserForm
from django.shortcuts import render
from django.views import generic
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from random import random
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView


#################################### Front Display  #########################################

def maincontent(Request):
    return render(Request, "maincontent.html")

def about(Request):
    return render(Request, "about.html")


def features(Request):
    return render(Request, "travocrm.html")


def calendy(Request):
    return render(Request, "calendy.html")


def clients(Request):
    return render(Request, "clients.html")


def contactus(Request):
    return render(Request, "contactus.html")


def pricing(Request):
    return render(Request, "pricing.html")


def privacypolicy(Request):
    return render(Request, "privacypolicy.html")


def termsandconditions(Request):
    return render(Request, "termsandconditions.html")

#################################### End Front Display ###################################



#################################### Dashboard Start ###################################

def dashboard(Request):
    d2 = Lead.objects.filter(priority="Hot")
    d3 = Lead.objects.filter(priority="Hot").count()
    d4 = Lead.objects.all().count()
    d5 = Lead.objects.filter(status="Booked").count()
    d6 = Lead.objects.filter(status="Lost").count()
    whatsappnumber =WhatsAppNumber.objects.all().last()
    return render(Request, "dashboard.html",{'d2':d2,'d3':d3,'d4':d4,'d5':d5,'d6':d6,'whatsappnumber':whatsappnumber})

def logoutPage(Request):
    logout(Request)
    return redirect("/login")

def viewProfile(Request,id):
    d = User.objects.get(id=id)
    return render(Request, "viewprofile.html", {"d": d})


#################################### End Dashboard ###################################

#################################### Start Lead  ###################################

def leads(Request):
    type = Request.user.type
    if type == "Admin":
        data = Lead.objects.all()
        d1 = User.objects.all()
        if Request.method == 'POST':
        # from_date = Request.POST.get('from')
        # to_date = Request.POST.get('to')
            priority = Request.POST.get('priority')
            status = Request.POST.get('status')
            triptype = Request.POST.get('triptype')
            assigned = Request.POST.get('assigned')
            # enquiry_type = Request.POST.get('enquiry')
            leadno = Request.POST.get('leadnumber')
            firstname = Request.POST.get('firstname')
            lastname = Request.POST.get('lastname')
            number = Request.POST.get('mobilenumber')
            email = Request.POST.get('email')
            tags = Request.POST.get('tags')
            data = Lead.objects.filter(Q(priority=priority)|Q(status=status)|Q(triptype=triptype)|Q(assigned=assigned)|Q(leadno=leadno)
                               |Q(firstname=firstname)|Q(lastname=lastname)|Q(number=number)|Q(email=email)|Q(tags=tags))
            return render(Request, "leads.html", {'d1':d1,'data':data})
        return render(Request, "leads.html", {'d1':d1,'data':data})
    else:
        #data = Lead.objects.all()
        data = Lead.objects.filter(assigned=Request.user)
        d1 = User.objects.get(email = Request.user.email)
        if Request.method == 'POST':
        # from_date = Request.POST.get('from')
        # to_date = Request.POST.get('to')
            priority = Request.POST.get('priority')
            status = Request.POST.get('status')
            triptype = Request.POST.get('triptype')
            assigned = Request.POST.get('assigned')
            # enquiry_type = Request.POST.get('enquiry')
            leadno = Request.POST.get('leadnumber')
            firstname = Request.POST.get('firstname')
            lastname = Request.POST.get('lastname')
            number = Request.POST.get('mobilenumber')
            email = Request.POST.get('email')
            tags = Request.POST.get('tags')
            print(Request.POST)
            data = Lead.objects.filter(Q(priority=priority)|Q(status=status)|Q(triptype=triptype)|Q(assigned=assigned)|Q(leadno=leadno)
                               |Q(firstname=firstname)|Q(lastname=lastname)|Q(number=number)|Q(email=email)|Q(tags=tags))
            return render(Request, "leads.html", {'d1':d1,'data':data})
        return render(Request, "leads.html", {'d1':d1,'data':data})


# def addleads(Request):
        
#         d1 = User.objects.get(email = Request.user.email)

#         if (Request.method == "POST"):
#             customertype = Request.POST.get('customertype')
#             number = Request.POST.get('number')
#             email = Request.POST.get('email')
#             salutation = Request.POST.get('salutation')
#             firstname = Request.POST.get('firstname')
#             lastname = Request.POST.get('lastname')
#             address = Request.POST.get('address')
#             city = Request.POST.get('city')
#             alternatenumber = Request.POST.get('alternatenumber')
#             alternateemail = Request.POST.get('alternateemail')
#             leadsource = Request.POST.get('leadsource')
#             priority = Request.POST.get('priority')
#             status = Request.POST.get('status')
#             adults = Request.POST.get('adults')
#             child = Request.POST.get('child')
#             infants = Request.POST.get('infants')
#             tags = Request.POST.get('tags')
#             triptype = Request.POST.get('triptype')
#             assigned = Request.POST.get('assigned')
#             created = Request.POST.get('setdate')
#             data = Lead(customertype=customertype, number=number, email=email, salutation=salutation, firstname=firstname, lastname=lastname, address=address,
#                         city=city, alternatenumber=alternatenumber, alternateemail=alternateemail, leadsource=leadsource, priority=priority, status=status,
#                         adults=adults, child=child, infants=infants, tags=tags,triptype=triptype, assigned=Request.user, created=created)

#             data.save()
#             subject = 'Your Lead is added. : Team Travvolt CRM'
#             message = "Hello,"+data.firstname +data.lastname + \
#                     "\nThanks to add lead with us\nNow You Can Manage Leads :Team Travvolt CRM"
#             email_from = settings.EMAIL_HOST_USER
#             recipient_list = [data.email, ]
#             send_mail(subject, message, email_from, recipient_list)
#         return render(Request, "addleads.html",{'d1':d1})


from django.shortcuts import render, redirect
from .forms import LeadForm

def addleads(request):
    print('addleads view called')
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        print(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.assigned = request.user  # Set the user who created the lead as the assigned user
            lead.save()
            print(lead)
        else:
            print(form.errors)

        return redirect('addflightbook')
    else:
        # lead_no = generate_lead_no()
        # form = LeadForm(initial={'leadno': lead_no})
        return render (request,'add_lead.html', {'error': form.errors})
    return render(request, 'add_lead.html', {'form': form})



def editleads(Request, id):
    # d1 = User.objects.get(first_name=Request.user.first_name)
    data = Lead.objects.get(id=id)
    if (Request.method == "POST"):
        data.customertype = Request.POST.get('customertype')
        data.number = Request.POST.get('number')
        data.email = Request.POST.get('email')
        data.salutation = Request.POST.get('salutation')
        data.firstname = Request.POST.get('firstname')
        data.lastname = Request.POST.get('lastname')
        data.address = Request.POST.get('address')
        data.city = Request.POST.get('city')
        data.alternatenumber = Request.POST.get('alternatenumber')
        data.alternateemail = Request.POST.get('alternateemail')
        data.leadsource = Request.POST.get('leadsource')
        data.priority = Request.POST.get('priority')
        data.status = Request.POST.get('status')
        data.adults = Request.POST.get('adults')
        data.child = Request.POST.get('child')
        data.infants = Request.POST.get('infants')
        data.tags = Request.POST.get('tags')
        data.triptype = Request.POST.get('triptype')
        data.destination = Request.POST.get('destination')
        data.save()
        subject = 'Your Lead is updated. : Team Travvolt CRM'
        message = "Hello,"+data.firstname +data.lastname + \
                "\nThanks to add lead with us\nNow You Can Manage Leads :Team Travvolt CRM"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [data.email, ]
        send_mail(subject, message, email_from, recipient_list)
        return redirect("/leads")
    return render(Request, "editleads.html", {"data": data })


def delete(Request, id):
    lead = Lead.objects.get(id=id)
    lead.email = Request.POST.get('email')
    lead.delete()
    subject = 'Your Lead is deleted. : Team Travvolt CRM'
    message ="Add other lead with us\nNow You Can Manage Leads :Team Travvolt CRM"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [lead.email, ]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponseRedirect(reverse('leads'))

def viewlead(Request,id):
    data = Lead.objects.get(id=id)
    return render(Request, "viewlead.html", {"data": data})


#################################### End Lead  ###################################


################################### START ENQUIRY TYPE ############################


from django.shortcuts import render, redirect
from .forms import FlightBookForm

def addflightbook(request):
    flight_book_form = FlightBookForm()
    context = {'flight_book_form': flight_book_form}
    if request.method == 'POST':
        flight_book_form = FlightBookForm(request.POST) 
        if flight_book_form.is_valid():
            flight_book_form.save()
            # return redirect('addleads')
    return render(request, 'addleads.html', context)







#################################### END ENQUIRY TYPE #############################


#################################### Start User  ###################################

def people(Request):
    type = Request.user.type
    if type == "SalesPerson":
        return redirect("/dashboard")
    else:
        data = User.objects.filter(is_internaluser=True)
        print(Request.user)
        return render(Request, "users.html", {'data': data})

class AdduserView(generic.CreateView):
    form_class = UserForm
    template_name = 'adduser.html'
    success_url = reverse_lazy('user')
    
    def form_valid(self,form):
        form.instance.is_internaluser = True
        print(form.instance.id)
        try:
            form.instance.username = str(form.instance.first_name + str(int(random()*10)))
        except:
            form.instance.username =str(form.instance.first_name + str(int(random()*10)))
        return super(AdduserView, self).form_valid(form)
        

def edituser(Request, id):
    data = User.objects.get(id=id)
    if (Request.method == "POST"):
        data.firstname = Request.POST.get('firstname')
        data.lastname = Request.POST.get('lastname')
        data.email = Request.POST.get('email')
        data.number = Request.POST.get('number')
        data.role = Request.POST.get('role')
        data.area = Request.POST.get('area')
        data.save()
        return redirect("/user")
    return render(Request, "edituser.html", {"data": data})

def viewUser(Request,id):
    data = User.objects.get(id=id)
    return render(Request, "viewuser.html", {"data": data})

#################################### End User  ###################################


################################### Start Customer ###################################

def contact(Request):
    # data = customer.objects.all()
    # return render(Request, "contact.html", {'data': data})
    type = Request.user.type
    if type == "Admin":
        data = customer.objects.all()  
    else:
        data = customer.objects.filter(user__email=Request.user.email)
    if Request.method == 'POST':
        salutation = Request.POST.get('salutation')
        firstname = Request.POST.get('firstname')
        lastname = Request.POST.get('lastname')
        number = Request.POST.get('number')
        email = Request.POST.get('email')
        customertype = Request.POST.get('customertype')
        source = Request.POST.get('source')
        tags = Request.POST.get('tags')
        data = customer.objects.filter(Q(salutation=salutation)|Q(firstname=firstname)|Q(lastname=lastname)|Q(number=number)|Q(customertype=customertype)
                            |Q(source=source)|Q(tags=tags)|Q(email=email))
        return render(Request, "contact.html", {'data':data})
    return render(Request, "contact.html", {'data':data})




def addcustomer(Request): 
    if (Request.method == "POST"):
        number = Request.POST.get('number')
        email = Request.POST.get('email')
        salutation = Request.POST.get('salutation')
        firstname = Request.POST.get('firstname')
        lastname = Request.POST.get('lastname')
        address = Request.POST.get('address')
        address2 = Request.POST.get('address2')
        city = Request.POST.get('city')
        pincode = Request.POST.get('pincode')
        alternateaddress = Request.POST.get('alternateaddress')
        alternatemobile = Request.POST.get('alternatenumber')
        alternateemail = Request.POST.get('alternateemail')
        source = Request.POST.get('source')
        customertype = Request.POST.get('customertype')
        accounthead = Request.POST.get('accounthead')
        tags = Request.POST.get('tags')
        flyer = Request.POST.get('flyer')
        food = Request.POST.get('food')
        pan = Request.POST.get('pan')
        passport = Request.POST.get('passport')
        enquirydate = Request.POST.get('enquirydate')
        issuedate = Request.POST.get('issuedate')
        
        data = customer(user=Request.user,number=number, email=email, salutation=salutation, firstname=firstname, lastname=lastname, address=address, address2=address2, city=city,
                        pincode=pincode, alternateaddress=alternateaddress, alternateemail=alternateemail, alternatemobile=alternatemobile, source=source,
                        customertype=customertype, accounthead=accounthead, tags=tags, flyer=flyer, food=food, pan=pan, passport=passport, enquirydate=enquirydate, issuedate=issuedate)
        data.save()

    return render(Request, "addcustomer.html")

def editcustomer(Request,id):
    c = customer.objects.get(id=id)
    if (Request.method == "POST"):
        c.number = Request.POST.get('number')
        c.email = Request.POST.get('email')
        c.salutation = Request.POST.get('salutation')
        c.firstname = Request.POST.get('firstname')
        c.lastname = Request.POST.get('lastname')
        c.address = Request.POST.get('address')
        c.address2 = Request.POST.get('address2')
        c.city = Request.POST.get('city')
        c.pincode = Request.POST.get('pincode')
        c.alternateaddress = Request.POST.get('alternateaddress')
        c.alternatemobile = Request.POST.get('alternatenumber')
        c.alternateemail = Request.POST.get('alternateemail')
        c.source = Request.POST.get('source')
        c.customertype = Request.POST.get('customertype')
        c.accounthead = Request.POST.get('accounthead')
        c.tags = Request.POST.get('tags')
        c.flyer = Request.POST.get('flyer')
        c.food = Request.POST.get('food')
        c.pan = Request.POST.get('pan')
        c.passport = Request.POST.get('passport')
        c.enquirydate = Request.POST.get('enquirydate')
        c.issuedate = Request.POST.get('issuedate')
        c.save()
        return redirect("/customer")
    return render(Request,"editcustomer.html",{'c':c})

def viewcustomer(Request,id):
    d = customer.objects.get(id=id)
    return render(Request, "viewcustomer.html", {"d": d})

################################### End Customer  ################################################

###################################  Start Supplier ##############################################

def Supplier(Request):
    type = Request.user.type
    if type == "Admin":
        data = supplier.objects.all()  
    else:
        data = supplier.objects.filter(user__email=Request.user.email)
    return render (Request,"supplier.html",{'suppliers':data})

def viewsupplier(Request,id):
    s = supplier.objects.get(id=id)
    return render(Request, "viewsupplier.html", {"s": s})


def addsupplier(request):
    form = SupplierForm()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        print("outerform")
        if form.is_valid():
            print('innerform',form)
            instance = form.save(commit=False)
            instance.user=request.user
            instance.save()
        else:
            return render (request,'addsupplier.html', {'error': form.errors})
    return render(request, 'addsupplier.html', {'form': form})


##################################### End Supplier ##############################################


################################### Start Sightseeing ##############################################

def sightseeing(Request):
    type = Request.user.type
    if type == "Admin":
        data = Sightseeing.objects.all()  
    else:
        data = Sightseeing.objects.filter(user__email=Request.user.email)
        if Request.method == 'POST':
            country = Request.POST.get('country')
            city = Request.POST.get('city')
            data = Sightseeing.objects.filter(Q(country=country)|Q(city=city))
            return render(Request,'sightseeing.html',{'sightseen':data})
    return render(Request,'sightseeing.html',{'sightseen':data})

def addsightseeing(Request):
    if Request.method == "POST":
        id = Request.POST.get('id')
        country = Request.POST.get('country')
        city = Request.POST.get('city')
        activity = Request.POST.get('activity')
        description = Request.POST.get('description')
        inclusion = Request.POST.get('inclusion')
        exclusion = Request.POST.get('exclusion')
        duration = Request.POST.get('duration')
        closeday = Request.POST.get('closeday')
        timings = Request.POST.get('timings')
        transport = Request.POST.get('transport')
        time = Request.POST.get('time')
        remark = Request.POST.get('remark')
        internalremark = Request.POST.get('internalremark')
        externalremark = Request.POST.get('externalremark')
        image = Request.FILES.get('image')
        sightseen = Sightseeing(user=Request.user,id=id,country=country,city=city,activity=activity,description=description,inclusion=inclusion,
                                exclusion=exclusion,duration=duration,closeday=closeday,timings=timings,
                                transport=transport,time=time,remark=remark,internalremark=internalremark,
                                externalremark=externalremark,image=image)
        sightseen.save()
    return render(Request,"addsightseeing.html")

def editsightseeing(Request,id):
    s = Sightseeing.objects.get(id=id)
    if Request.method == "POST":
        s.country = Request.POST.get('country')
        s.city = Request.POST.get('city')
        s.activity = Request.POST.get('activity')
        s.description = Request.POST.get('description')
        s.inclusion = Request.POST.get('inclusion')
        s.exclusion = Request.POST.get('exclusion')
        s.duration = Request.POST.get('duration')
        s.closeday = Request.POST.get('closeday')
        s.timings = Request.POST.get('timings')
        s.transport = Request.POST.get('transport')
        s.time = Request.POST.get('time')
        s.remark = Request.POST.get('remark')
        s.internalremark = Request.POST.get('internalremark')
        s.externalremark = Request.POST.get('externalremark')
        s.image = Request.FILES.get('image')
        s.save()
        return redirect("/sightseeing")
    return render(Request,"editsightseeing.html",{'s':s})


def viewsightseeing(Request,id):
    s = Sightseeing.objects.get(id=id)
    return render(Request, "viewsightseeing.html", {"s": s})

################################ End Sightseeing ##############################################


############################### Start Transport ##############################################

def transport(Request):
    type = Request.user.type
    if type == "Admin":
        transport = Vehicle.objects.all()
    else:
        transport = Vehicle.objects.filter(user__email = Request.user.email)
    if Request.method == 'POST':
        country = Request.POST.get('country')
        city = Request.POST.get('city')
        transport = Vehicle.objects.filter(Q(country=country)|Q(city=city))
        return render(Request,"transport.html",{'transport':transport})
    return render(Request,'transport.html',{'transport':transport})
    
    
    
def addtransport(Request):
    if Request.method=="POST":
        id = Request.POST.get('id')
        country = Request.POST.get('country')
        city = Request.POST.get('city')
        vehicletype = Request.POST.get('vehicletype')
        title = Request.POST.get('title')
        description = Request.POST.get('description')
        internalremark = Request.POST.get('internalremark')
        image = Request.FILES.get('image')
        transport = Vehicle(user=Request.user,id=id,country=country,city=city,vehicletype=vehicletype,title=title,description=description,internalremark=internalremark,
                            image=image)
        transport.save()
    return render(Request,"addtransport.html")


def edittransport(Request,id):
    t = Vehicle.objects.get(id=id)
    if Request.method == "POST":
        t.country = Request.POST.get('country')
        t.city = Request.POST.get('city')
        t.vehicletype = Request.POST.get('vehicletype')
        t.title = Request.POST.get('title')
        t.description = Request.POST.get('description')
        t.internalremark = Request.POST.get('internalremark')
        t.image = Request.FILES.get('image')
        t.save()
        return redirect("/transport")
    return render(Request,"edittransport.html",{'t':t})

def viewtransport(Request,id):
    t = Vehicle.objects.get(id=id)
    return render(Request,"viewtransport.html",{'t':t})

################################### End Transport ###################################


################################### Start Packages ###################################

def packages(Request):
    type = Request.user.type
    if type == "Admin":
        data = Package.objects.all()  
    else:
        data = Package.objects.filter(created_by__email=Request.user.email)
    if Request.method == "POST":
        country = Request.POST.get('country')

        data = Package.objects.filter(Q(country=country))
        return render(Request, "packages.html", {"p2": data})
    return render(Request, "packages.html", {"p2": data})


def addpackages(request):
    form = PackageForm()
    formset = BirdFormSet(queryset=Destination.objects.none())
    
    
    if request.method == 'POST':
        formset = BirdFormSet(request.POST)
        
        
        if formset.is_valid():
            list=[]
            for i in formset:
                inst = i.save()
                list.append(inst.id)
        
        form = PackageForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.created_by=request.user
            instance.save()
            m = Package.objects.filter(created_by= request.user).last()
            m.destinations.set(list)
            
        else:
            print("form.errors:",form.errors)
    return render(request, 'addpackages.html', {'form': form,"bird_formset": formset})


class BirdAddView(TemplateView):
    template_name = "addpackages.html"

    def get(self, *args, **kwargs):
        formset = BirdFormSet(queryset=Destination.objects.none())
        form = PackageForm()
        return self.render_to_response({"bird_formset": formset,'form':form})

    def post(self, *args, **kwargs):

        formset = BirdFormSet(data=self.request.POST)

        if formset.is_valid():
           instance2=formset.save()
        form = PackageForm(data=self.request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.created_by=self.request.user
            instance.save()
            m = Package.objects.filter(created_by= self.request.user).last()
            m.destinations.add(instance2.id)
            return redirect(reverse_lazy("bird_list"))

        return self.render_to_response({"bird_formset": formset})


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class GenerateInvoice(View):
    def get(self, request,id, *args, **kwargs):
        order_db = Package.objects.get(created_by=request.user.id,id=id)

        data = {
            'Package_name': order_db.packagename,
            'Country': order_db.country,
            'Destinations':order_db.destinations.all(),
            'Days':order_db.days,
            'Detailed_Itenerary':order_db.detailed_itenerary,
            'Hotel_Details':order_db.hotel_details,
            'Tags':order_db.tags,
            'Meal_Type': order_db.mealtype,
            'Free_WiFi':order_db.free_wi_fi,
            'Airport_Transfers_Private':order_db.airport_transfers_private,
            'Airport_Transfers_SIC':order_db.airport_transfers_sic,
            'Travel_Insurance':order_db.travel_insurance,
            'Visa':order_db.visa,
            'Inter_Hotel_Transfer_Private':order_db.Inter_hotel_transfer_private,
            'Sightseeing_Transfer_Private':order_db.sightseeing_transfer_private,
            'Sightseeing_Transfer_SIC':order_db.sightseeing_transfer_sic,
            'Inter_Hotel_Transfer_SIC':order_db.Inter_hotel_transfer_sic,
            'Candle_Light_Dinner':order_db.candlelight_dinner,
            'Bed_Decorations':order_db.bed_decorations,
            'Honeymoon_Cake':order_db.honeymoon_cake,
            'Private_Ferry':order_db.private_ferry,
            'Private_Cruise':order_db.private_cruise,
            'Scuba_Diving':order_db.scuba_diving,
            'Parasailing':order_db.parasailing,            
            'Sea_Walk':order_db.sea_walk,              
            'Photoshoot_for_Couple':order_db.photoshoot_for_couple,            
            'Candle_Light_Dinner_With_Wine':order_db.candle_light_dinner_with_wine,            
            'Candle_Light_Dinner_Without_Wine':order_db.candle_light_dinner_without_wine,            
            'Jet_Ski':order_db.jet_ski,            
            'Snorkeling':order_db.snorkeling,            
            'Airport_Transfers_Speed_Boat_Sea_Plane':order_db.airport_transfers_speed_boat_seaplane,    
            'Inclusive':order_db.inclusive,
            'Exclusive':order_db.exclusive,
            'Terms_and_Conditions':order_db.terms_and_conditions,
            'Cancellation_Policy':order_db.cancellation_policy,
            'Image': order_db.image,
           
            
            
        }
        pdf = render_to_pdf('packagereciept_pdf.html', data)
        

        # pdf download
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = f"Invoice_{order_db.id}.pdf"
            content = "inline; filename='%s'" %(filename)
            content = "attachment; filename=%s" %(filename)
            response['Content-Disposition'] = content
       
            return response
        return HttpResponse("Not found")

def viewpackages(Request, id):
    data = Package.objects.get(id=id)
    return render(Request, "viewpackages.html", {"p2": data})


class PackageUpdateView(UpdateView):
    template_name = 'editpackages.html'
    model = Package
    fields = ['packagename','country','days','detailed_itenerary','hotel_details',
              'tags','mealtype','free_wi_fi','airport_transfers_private','airport_transfers_sic',
              'travel_insurance','visa','Inter_hotel_transfer_private','sightseeing_transfer_private',
              'sightseeing_transfer_sic','Inter_hotel_transfer_sic','candlelight_dinner','bed_decorations',
              'honeymoon_cake','private_ferry','private_cruise','scuba_diving','parasailing','sea_walk',
              'photoshoot_for_couple','candle_light_dinner_with_wine','candle_light_dinner_without_wine',
              'jet_ski','snorkeling','airport_transfers_speed_boat_seaplane','image','inclusive','exclusive',
              'terms_and_conditions','cancellation_policy']
    success_url ="/packages/"


################################### End Package ########################################


################################### Start Hotel ######################################

def hotels(Request):
    type = Request.user.type
    if type == "Admin":
        data = Hotel.objects.all()  
    else:
        data = Hotel.objects.filter(user__email=Request.user.email)
    if Request.method == "POST":
        country = Request.POST.get('country')
        city = Request.POST.get('city')

        data = Hotel.objects.filter(Q(country=country) | Q(city=city))
        return render(Request, "hotels.html", {"h2": data})
    return render(Request, "hotels.html", {"h2": data})

    

def addhotels(Request):
    if(Request.method == "POST"):
        hotelname = Request.POST.get('hotelname')
        country = Request.POST.get('country')
        city = Request.POST.get('city')
        address = Request.POST.get('address')
        contact = Request.POST.get('contact')
        email = Request.POST.get('email')
        rate = Request.POST.get('rate')
        htype = Request.POST.get('htype')
        childfreeage = Request.POST.get('childfreeage')
        childwithoutfreeage = Request.POST.get('childwithoutfreeage')
        amenities = Request.POST.get('amenities')
        description = Request.POST.get('description')
        image = Request.FILES.get('image')
        data = Hotel(user=Request.user,hotelname=hotelname, country=country, city=city, email=email, 
                    address=address, contact=contact, rate=rate, htype=htype, 
                    childfreeage=childfreeage, childwithoutfreeage=childwithoutfreeage, 
                    amenities=amenities, description=description, image=image)

        data.save()
    return render(Request, "addhotels.html")

def viewhotels(Request,id): 
    data = Hotel.objects.get(id=id)
    return render(Request, "viewhotels.html", {"h1": data})

def edithotels(Request, id):
    data = Hotel.objects.get(id=id)
    if (Request.method == "POST"):
        data.hotelname = Request.POST.get('hotelname')
        data.country = Request.POST.get('country')
        data.city = Request.POST.get('city')
        data.address = Request.POST.get('address')
        data.contact = Request.POST.get('contact')
        data.email = Request.POST.get('email')
        data.rate = Request.POST.get('rate')
        data.htype = Request.POST.get('htype')
        data.childfreeage = Request.POST.get('childfreeage')
        data.childwithoutfreeage = Request.POST.get('childwithoutfreeage')
        data.amenities = Request.POST.get('amenities')
        data.description = Request.POST.get('description')
        data.image = Request.FILES.get('image')
        data.save()
        return redirect("/hotels")
    return render(Request, "edithotels.html", {"data": data})


################################### End Hotel ##############################################



def visa(Request):
    return render(Request,"visainfo.html")

def addvisa(Request):
    return render(Request,"addvisa.html")


#################################### Creating the RestAPI  ###################################

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def lead_api(Request, pk=None): 
    if Request.method == 'GET':
        id = pk 
        if id is not None:
            lead = Lead.objects.get(id=id)
            serializer = LeadModelSerializer(lead)
            return Response(serializer.data)
        
        lead = Lead.objects.all()
        serializer = LeadModelSerializer(lead, many=True)
        return Response(serializer.data)
    
    if Request.method == 'POST':
        serializer = LeadModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Lead is Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PUT':
        id = pk
        lead = Lead.objects.get(pk=id)
        serializer = LeadModelSerializer(lead, data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data Updated'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PATCH':
        id = pk 
        lead = Lead.objects.get(pk=id)
        serializer = LeadModelSerializer(lead, data=Request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'DELETE':
        id = pk 
        lead = Lead.objects.get(pk=id)
        lead.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_301_MOVED_PERMANENTLY)
    

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def customer_api(Request, pk=None):
    if Request.method == 'GET':
        id = pk 
        if id is not None:
            Customer = customer.objects.get(id=id)
            serializer = CustomerModelSerializer(Customer)
            return Response(serializer.data)
        
        Customer = customer.objects.all()
        serializer = CustomerModelSerializer(Customer, many=True)
        return Response(serializer.data)
    
    if Request.method == 'POST':
        serializer = CustomerModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Customer is Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PUT':
        id = pk
        Customer = customer.objects.get(pk=id)
        serializer = CustomerModelSerializer(Customer, data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data Updated'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PATCH':
        id = pk 
        Customer = customer.objects.get(pk=id)
        serializer = CustomerModelSerializer(customer, data=Request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'DELETE':
        id = pk 
        Customer = customer.objects.get(pk=id)
        Customer.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_301_MOVED_PERMANENTLY)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def supplier_api(Request, pk=None):
    if Request.method == 'GET':
        id = pk 
        if id is not None:
            Supplier = supplier.objects.get(id=id)
            serializer = SupplierModelSerializer(Supplier)
            return Response(serializer.data)
        
        Supplier = supplier.objects.all()
        serializer = SupplierModelSerializer(Supplier, many=True)
        return Response(serializer.data)
    
    if Request.method == 'POST':
        serializer = SupplierModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Supplier is Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PUT':
        id = pk
        Supplier = supplier.objects.get(pk=id)
        serializer = SupplierModelSerializer(Supplier, data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data Updated'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PATCH':
        id = pk 
        Supplier = supplier.objects.get(pk=id)
        serializer = SupplierModelSerializer(Supplier, data=Request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'DELETE':
        id = pk 
        Supplier = supplier.objects.get(pk=id)
        Supplier.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_301_MOVED_PERMANENTLY)
    
    
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def sightseeing_api(Request, pk=None):
    if Request.method == 'GET':
        id = pk 
        if id is not None:
            sightseeing = Sightseeing.objects.get(id=id)
            serializer = SightseeingModelSerializer(sightseeing)
            return Response(serializer.data)
        
        sightseeing = Sightseeing.objects.all()
        serializer = SightseeingModelSerializer(sightseeing, many=True)
        return Response(serializer.data)
    
    if Request.method == 'POST':
        serializer = SightseeingModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Sightseeing is Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PUT':
        id = pk
        sightseeing = Sightseeing.objects.get(pk=id)
        serializer = SightseeingModelSerializer(Supplier, data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data Updated'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PATCH':
        id = pk 
        sightseeing = supplier.objects.get(pk=id)
        serializer = SightseeingModelSerializer(Supplier, data=Request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'DELETE':
        id = pk 
        sightseeing = Sightseeing.objects.get(pk=id)
        sightseeing.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_301_MOVED_PERMANENTLY)
    

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def package_api(Request, pk=None):
    if Request.method == 'GET':
        id = pk 
        if id is not None:
            package = Package.objects.get(id=id)
            serializer = PackageModelSerializer(package)
            return Response(serializer.data)
        
        package = Package.objects.all()
        serializer = PackageModelSerializer(package, many=True)
        return Response(serializer.data)
    
    if Request.method == 'POST':
        serializer = PackageModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Package is Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PUT':
        id = pk
        package = Package.objects.get(pk=id)
        serializer = PackageModelSerializer(package, data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data Updated'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PATCH':
        id = pk 
        package = Package.objects.get(pk=id)
        serializer = PackageModelSerializer(package, data=Request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'DELETE':
        id = pk 
        package = Package.objects.get(pk=id)
        package.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_301_MOVED_PERMANENTLY)
    

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def vehicle_api(Request, pk=None):
    if Request.method == 'GET':
        id = pk 
        if id is not None:
            vehicle = Vehicle.objects.get(id=id)
            serializer = VehicleModelSerializer(vehicle)
            return Response(serializer.data)
        
        vehicle = Vehicle.objects.all()
        serializer = VehicleModelSerializer(vehicle, many=True)
        return Response(serializer.data)
    
    if Request.method == 'POST':
        serializer = VehicleModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Transportation detail is Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PUT':
        id = pk
        vehicle = Vehicle.objects.get(pk=id)
        serializer = VehicleModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data Updated'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PATCH':
        id = pk 
        vehicle = Vehicle.objects.get(pk=id)
        serializer = VehicleModelSerializer(vehicle, data=Request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'DELETE':
        id = pk 
        vehicle = Vehicle.objects.get(pk=id)
        vehicle.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_301_MOVED_PERMANENTLY)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def hotel_api(Request, pk=None):
    if Request.method == 'GET':
        id = pk 
        if id is not None:
            hotel = Hotel.objects.get(id=id)
            serializer = HotelModelSerializer(hotel)
            return Response(serializer.data)
        
        hotel = Hotel.objects.all()
        serializer = HotelModelSerializer(hotel, many=True)
        return Response(serializer.data)
    
    
    if Request.method == 'POST':
        serializer = HotelModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Hotels detail is Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    
    if Request.method == 'PUT':
        id = pk
        hotel = Hotel.objects.get(pk=id)
        serializer = HotelModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data Updated'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    if Request.method == 'PATCH':
        id = pk 
        hotel = Hotel.objects.get(pk=id)
        serializer = HotelModelSerializer(hotel, data=Request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    if Request.method == 'DELETE':
        id = pk 
        hotel = Hotel.objects.get(pk=id)
        hotel.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_301_MOVED_PERMANENTLY)

    
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def user_api(Request, pk=None):
    if Request.method == 'GET':
        id = pk 
        if id is not None:
            user = User.objects.get(id=id)
            serializer = UserModelSerializer(user)
            return Response(serializer.data)
        
        user = User.objects.all()
        serializer = UserModelSerializer(user, many=True)
        return Response(serializer.data)
    
    if Request.method == 'POST':
        serializer = UserModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'User is Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PUT':
        id = pk
        user = User.objects.get(pk=id)
        serializer = UserModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data Updated'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PATCH':
        id = pk 
        user = User.objects.get(pk=id)
        serializer = UserModelSerializer(user, data=Request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'DELETE':
        id = pk 
        user = User.objects.get(pk=id)
        user.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_301_MOVED_PERMANENTLY)


################################### End APIs ######################################################


