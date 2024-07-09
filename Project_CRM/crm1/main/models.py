from django.db import models
from . utils import generate_lead_no
from Useraccount.models import User
from django.utils import timezone
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django import forms
    
CUSTOMER_CHOICES = (
    ('B2B','B2B'),
    ('B2C','B2C'),
    ('Corporate','Corporate'),
    ('VIP','VIP'),
)    

DAYS_CHOICES = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10')

) 

SALUTATION_CHOICES = (
    ('Mr','Mr'),
    ('Mrs','Mrs'),
    ('Miss','Miss'),
    ('Dr','Dr'),
)

LEAD_SOURCE_CHOICES = (
    ('Advertisement','Advertisement'),
    ('Cold Call','Cold Call'),
    ('Employee Referral','Employee Referral'),
    ('External Referral','External Referral'),
    ('Website','Website'),
    ('Public Relation','Public Relation'),
    ('Email Campaign','Email Campaign'),
    ('SMS Campaign','SMS Campaign'),
    ('Trade Show','Trade Show'),
    ('None','None'),
    ('Old Customer','Old Customer'),
    ('New Customer','New Customer'),
    ('Walk In','Walk In'),
    ('SEO','SEO'),
    ('Excel','Excel'),
    ('Just Dial','Just Dial'),
    ('Phone Call','Phone Call'),
    ('Airbnb','Airbnb'),
    ('Live Chat','Live Chat'),
    ('Travvolt','Travvolt'),
    ('Hello Travel','Hello Travel'),
    ('TripShelf','TripShelf'),
    ('Newspaper','Newspaper'),
    ('Sulekha','Sulekha'),
    ('Travel Triangle','Travel Triangle'),
    ('TripCrafters','TripCrafters'),
    ('Other','Other'),
    ('Flyer','Flyer'),
    ('Travelsetu','Travelsetu'),
    ('Facebook','Facebook'),
    ('Google Ads','Google Ads'),
    ('Instagram','Instagram'),
    ('10Times','10Times'),
    ('Rotary','Rotary'),
    ('BNI','BNI'),
    ('YES','YES'),
    ('Mail','Mail'),
    ('Agent','Agent'),
    ('Google','Google'),
    ('Whatsapp','Whatsapp'),
    ('Webmail','Webmail'),
    ('Direct Sales','Direct Sales'),
    ('Incoming Call','Incoming Call'),
    ('Chat','Chat'),
    ('Brouchers','Brouchers'),
)

LEAD_PRIORITY_CHOICES = (
    ('All','All'),
    ('Cold','Cold'),
    ('Warm','Warm'),
    ('Hot','Hot'),
)

LEAD_STATUS_CHOICES = (
    ('All','All'),
    ('Unquilified','Unquilified'),
    ('New','New'),
    ('Working','Working'),
    ('Proposal Sent','Proposal Sent'),
    ('Negotiating','Negotiating'),
    ('Booked','Booked'),
    ('Lost','Lost'),
)

TAGS_CHOICES = (
    ('All','All'),
    ('Family','Family'),
    ('Honeymoon','Honeymoon'),
    ('Individual','Individual'),
    ('Adventure','Adventure'),
    ('Group','Group'),
    ('Women Only','Women Only'),
    ('Domestic','Domestic'),
    ('International','International'),
    ('Beaches','Beaches'),
    ('Weekend','Weekend'),
    ('Heritage','Heritage'),
    ('Wildlife','Wildlife'),
    ('Jungle Safari','Jungle Safari'),
    ('Student','Student'),
    ('Pilgrimage','Pilgrimage'),
    ('Popular','Popular'),
    ('Trending','Trending'),
)

TRIP_CHOICES = (
    ('Other','Other'),
    ('Family','Family'),
    ('Honeymoon','Honeymoon'),
    ('Friends','Friends'),
    ('Official','Official'),
    ('Adventure','Adventure'),
    ('Corporate','Corporate'),
    ('Educational','Educational'),
    ('Group','Group'),
    ('Individual','Individual'),
    ('Religious','Religious'),
    ('Couple','Couple'),
    ('Student Group','Student Group'),
)

FOOD_CHOICES = (
    ('All','All'),
    ('Vegetarian','Vegetarian'),
    ('NonVegetarian','NonVegetarian'),
    ('Jainism','Jainism'),
    ('Sweet','Sweet')
)

VEHICLE_CHOICES= (
    ('Sedan', 'Sedan'),
    ('Hatchback', 'Hatchback'),
    ('MPV', 'MPV'),
    ('SUV', 'SUV'),
)

TRANSPORT_PREFERENCES_CHOICES=(
    ('Private','Private'),
    ('SIC','SIC'),
    ('Other','Other'),
)

MEAL_CHOICES = (
        ('AP(Full Board)', 'AP(Full Board)'),
        ('MAP(Half Board)', 'MAP(Half Board)'),
        ('CP(Only Breakfast)', 'CP(Only Breakfast)'),
        ('EP(No Meal)', 'EP(No Meal)'),
        ('Any(Any type of meal)', 'Any(Any type of meal)'),
        ('AI(All Inclusive)', 'AI(All Inclusive)'),
           
    )

STAR_RATE_CHOICES=[
    ('-','-'),
    ('All','All'),
    ('One Star','One Star'),
    ('Two Star','Two Star'),
    ('Three Star','Three Star'),
    ('Four Star','Four Star'),
    ('Five Star','Five Star')
]

ROOM_TYPE_CHOICES=[
    ('-','-'),
    ('All','All'),
    ('Standard','Standard'),
    ('Deluxe','Deluxe'),
    ('Any','Any')
]


class Lead(models.Model):
    leadno = models.CharField(max_length=50, unique=True, null=True, blank=True)
    # user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_lead')
    customertype = models.CharField(max_length=100,choices=CUSTOMER_CHOICES,default='B2B') 
    number = PhoneNumberField(max_length=20)
    email = models.EmailField(max_length=100)
    salutation = models.CharField(max_length=100,choices=SALUTATION_CHOICES,default='Mr') 
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=500,blank=True,null=True)
    city = models.CharField(max_length=100)
    alternatenumber = models.CharField(max_length=15,blank=True,null=True)
    alternateemail = models.EmailField(max_length=100,blank=True,null=True)
    leadsource = models.CharField(max_length=100,null=True,choices=LEAD_SOURCE_CHOICES,default='Advertisement') 
    priority = models.CharField(max_length=100,choices=LEAD_PRIORITY_CHOICES,default='All') 
    status = models.CharField(max_length=100,null=True,choices=LEAD_STATUS_CHOICES,default='All') 
    adults = models.IntegerField(blank=True)
    child = models.CharField(max_length=15,blank=True,null=True)
    infants = models.CharField(max_length=15,blank=True,null=True)
    tags = models.CharField(max_length=100,null=True,choices=TAGS_CHOICES,default='All')   
    triptype = models.CharField(max_length=100,null=True,choices=TRIP_CHOICES,default='Other') 
    assigned = models.ForeignKey(User,on_delete=models.CASCADE) 
    destination = models.CharField(max_length=100,blank=True,null=True,default='-')
    created = models.DateTimeField(editable=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # enquirytype = models.CharField(max_length=100)
    enquiry_flight_booking = models.BooleanField(default=False)
    enquiry_hotel_booking = models.BooleanField(default=False)
    enquiry_visa = models.BooleanField(default=False)
    enquiry_travel_insurance = models.BooleanField(default=False)
    enquiry_forex = models.BooleanField(default=False)
    enquiry_sightseeing = models.BooleanField(default=False)
    enquiry_transport = models.BooleanField(default=False)
    enquiry_other = models.BooleanField(default=False)
    enquiry_package = models.BooleanField(default=False)
    enquiry_customize_package = models.BooleanField(default=False)
    enquiry_bus = models.BooleanField(default=False)
    enquiry_train = models.BooleanField(default=False)
    enquiry_passport = models.BooleanField(default=False)
    enquiry_cruise = models.BooleanField(default=False)
    enquiry_adventure = models.BooleanField(default=False)
    enquiry_group = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if self.leadno =="":
            lead_no = (generate_lead_no())
            
            self.leadno=lead_no
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.firstname)
    
class customer(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_customer')
    number = PhoneNumberField(max_length=20,null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    salutation = models.CharField(max_length=100,choices=SALUTATION_CHOICES,default='Mr',null=True)
    firstname = models.CharField(max_length=100,blank=True,null=True)
    lastname = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    address2 = models.CharField(max_length=200,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    pincode = models.IntegerField(blank=True,null=True)
    alternateaddress = models.CharField(max_length=200,blank=True,null=True)
    alternatemobile = PhoneNumberField(max_length=20,null=True)
    alternateemail = models.EmailField(max_length=100,blank=True,null=True)
    source = models.CharField(max_length=100,null=True,choices=LEAD_SOURCE_CHOICES,default='Advertisement') 
    customertype = models.CharField(max_length=100,choices=CUSTOMER_CHOICES,default='B2B') 
    accounthead = models.CharField(max_length=100,blank=True,null=True)
    tags = models.CharField(max_length=100,null=True,choices=TAGS_CHOICES,default='All')   
    flyer = models.CharField(max_length=100,blank=True,null=True)
    food = models.CharField(max_length=100,choices=FOOD_CHOICES,default="All")
    pan = models.CharField(max_length=30,blank=True,null=True)
    passport = models.CharField(max_length=30,blank=True,null=True)
    enquirydate = models.DateField(auto_now_add=False,blank=True,null=True)
    issuedate = models.DateField(auto_now_add=False,blank=True,null=True)


class supplier(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_supplier')
    companyname = models.CharField(max_length=255,null=True) 
    aliasname = models.CharField(max_length=255, blank=True,null=True)
    gst = models.IntegerField(null=True, blank=True)
    billingaddress = models.CharField(max_length=255, blank=True,null=True)
    city = models.CharField(max_length=255, blank=True,null=True) 
    deals_in_visa = models.BooleanField(default=False) 
    deals_in_flights = models.BooleanField(default=False)
    deals_in_hotel = models.BooleanField(default=False)
    deals_in_travel_insurance = models.BooleanField(default=False)
    deals_in_forex = models.BooleanField(default=False)
    deals_in_sightseeing = models.BooleanField(default=False)
    deals_in_transport = models.BooleanField(default=False)
    deals_in_cruise = models.BooleanField(default=False)
    deals_in_other = models.BooleanField(default=False)
    deals_in_package = models.BooleanField(default=False)
    deals_in_customize_package = models.BooleanField(default=False)
    deals_in_bus = models.BooleanField(default=False)
    deals_in_train = models.BooleanField(default=False)
    deals_in_passport = models.BooleanField(default=False)
    deals_in_adventure = models.BooleanField(default=False)
    deals_in_group_package = models.BooleanField(default=False)
    country = CountryField(blank_label='(select country)',null=True)
    tags = models.CharField(max_length=100,null=True,choices=TAGS_CHOICES,default='All') 
    name = models.CharField(max_length=255,null=True,blank=True)
    designation = models.CharField(max_length=255,null=True,blank=True)
    number = PhoneNumberField(max_length=20,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    alternatenumber = PhoneNumberField(max_length=20,null=True,blank=True)
    alternateemail = models.EmailField(null=True,blank=True)
    preffered_supplier = models.BooleanField(default=False)
    inactive_supplier = models.BooleanField(default=False)
    default_email = models.BooleanField(default=False)
    cc_email = models.BooleanField(default=False)
    bankdetails = models.TextField(null=True,blank=True)
    note = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.companyname
    
class Sightseeing(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_sightseen')
    country = CountryField(blank_label='(select country)',null=True)
    city = models.CharField(max_length=255,null=True)
    activity = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)
    inclusion = models.TextField(null=True)
    exclusion = models.TextField(null=True)
    duration = models.CharField(max_length=255,null=True) 
    closeday = models.CharField(max_length=255,null=True)
    timings = models.CharField(max_length=255,null=True)
    transport = models.CharField(max_length=255,null=True,choices=TRANSPORT_PREFERENCES_CHOICES,default='Private')
    time = models.CharField(max_length=255,null=True)
    remark = models.TextField(null=True)
    internalremark = models.TextField(null=True)
    externalremark = models.TextField(null=True)
    image = models.ImageField(upload_to = 'images',null=True, blank=True)

    def __str__(self):
        return self.activity

class Vehicle(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_vehicle')
    country = CountryField(blank_label='(select country)',null=True)
    city = models.CharField(max_length=100,null=True)
    vehicletype = models.CharField(max_length=100,null=True, choices=VEHICLE_CHOICES,default='Select Vehicle Type')
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    internalremark = models.TextField(null=True)
    image = models.ImageField(upload_to = 'images',null=True, blank=True)

    def __str__(self):  
        return self.title




class Hotel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_hotel')
    hotelname = models.CharField(max_length=100,blank=True,null=True)
    country = CountryField(blank_label='(select country)',null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    contact = PhoneNumberField(max_length=20,null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    rate = models.CharField(max_length=100, choices=STAR_RATE_CHOICES,default='All')
    htype = models.CharField(max_length=100, choices=ROOM_TYPE_CHOICES,default='-')
    childfreeage = models.CharField(max_length=100,blank=True,null=True)
    childwithoutfreeage = models.CharField(max_length=100,blank=True,null=True)
    amenities = models.CharField(max_length=100,blank=True,null=True)
    description = models.CharField(max_length=500,blank=True,null=True)
    image = models.ImageField(upload_to = 'images',null=True)

    def __str__(self):
        # return str(self.hotelname)
        return f'{self.hotelname}--{self.country}'

class Destination(models.Model):
    destination = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)


class Package(models.Model): 
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_package')
    packagename = models.CharField(max_length=100,blank=True,null=True)
    country = CountryField(blank=True,null=True)
    # city = models.CharField(max_length=100,blank=True,null=True)
    # stay = models.CharField(max_length=100,blank=True,null=True)
    destinations = models.ManyToManyField(Destination,null=True,blank=True)
    days = models.CharField(max_length=100, choices=DAYS_CHOICES,default="1")
    detailed_itenerary = models.TextField(null=True,blank=True)
    tags = models.CharField(max_length=100, choices=TAGS_CHOICES,default="All")
    overview = models.CharField(max_length=1000,blank=True)
    mealtype = models.CharField(max_length=100, choices=MEAL_CHOICES, default="AI(All Inclusive)")
    hotel_details = models.TextField(max_length=500,blank=True,null=True)
    free_wi_fi = models.BooleanField(default=False)
    airport_transfers_private = models.BooleanField(default=False)
    airport_transfers_sic = models.BooleanField(default=False)
    travel_insurance = models.BooleanField(default=False)
    visa = models.BooleanField(default=False)
    Inter_hotel_transfer_private = models.BooleanField(default=False)
    sightseeing_transfer_private = models.BooleanField(default=False)
    sightseeing_transfer_sic = models.BooleanField(default=False)
    Inter_hotel_transfer_sic = models.BooleanField(default=False)
    candlelight_dinner = models.BooleanField(default=False)
    bed_decorations = models.BooleanField(default=False)
    honeymoon_cake = models.BooleanField(default=False)
    private_ferry = models.BooleanField(default=False)
    private_cruise = models.BooleanField(default=False) 
    scuba_diving = models.BooleanField(default=False)
    parasailing = models.BooleanField(default=False)
    sea_walk = models.BooleanField(default=False)
    photoshoot_for_couple = models.BooleanField(default=False)
    candle_light_dinner_with_wine = models.BooleanField(default=False)
    candle_light_dinner_without_wine = models.BooleanField(default=False)
    jet_ski = models.BooleanField(default=False)
    snorkeling = models.BooleanField(default=False)
    airport_transfers_speed_boat_seaplane = models.BooleanField(default=False)
    image = models.ImageField(upload_to = 'images',null=True,blank=True)
    inclusive = models.TextField(max_length=1000,blank=True,null=True)
    exclusive = models.TextField(max_length=1000,blank=True,null=True)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True )
    terms_and_conditions = models.TextField(max_length=1000,null=True,blank=True)
    cancellation_policy = models.TextField(max_length=1000,null=True,blank=True)    
    
    def __str__(self) -> str:
        return f'{self.packagename}---{self.country}'
    
class WhatsAppNumber(models.Model):
    number = models.CharField(max_length=20)   
    


################## ENQUIRY TYPE MODELS START #########################

CLASS_CHOICES = [
    ('-','-'),
    ('All','All'),
    ('Economy','Economy'),
    ('Premium Economy','Premium Economy'),
    ('Business','Business'),
    ('First Class','First Class')
]

CATEGORY_CHOICES = [
    ('-','-'),
    ('All','All'),
    ('Domestic Flight','Domestic Flight'),
    ('International Flight','International Flight')
]

FLEXIBITY_CHOICES = [
    ('-','-'),
    ('+/- 0 Day','+/- 0 Day'),
    ('+/- 3 Day','+/- 3 Day'),
    ('+/- 6 Day','+/- 6 Day'),
    ('+/- 1 Week','+/- 1 Week'),
    ('+/- 3 Week','+/- 3 Week')
]

PREFERENCE_CHOICES = [
    ('-','-'),
    ('All','All'),
    ('One Stop','One Stop'),
    ('Cheapest','Cheapest'),
    ('Direct','Direct')
]
    
    
VISA_CATEGORY_CHOICES = [
    ('-','-'),
    ('All','All'),
    ('Business','Business'),
    ('Tourist','Tourist'),
    ('Student','Student'),
    ('Work','Work'),
    ('Transit','Transit')
]

VISIT_TYPE_CHOICES = [
    ('-','-'),
    ('All','All'),
    ('Single','Single'),
    ('Double','Double'),
    ('Multiple','Multiple')
] 

PREFERENCES_CHOICES = [
    ('-','-'),
    ('All','All'),
    ('Private','Private'),
    ('SIC','SIC'),
    ('Self Drive','Self Drive')
]

TRANSPORT_PREFERENCES_CHOICES = [
    ('-','-'),
    ('Self Drive','Self Drive'),
    ('Chauffer','Chauffer'),
    ('SIC','SIC')
]

INSURANCE_VISA_CHOICES = [
    ('-','-'),
    ('Yes','Yes'),
    ('No','No')
]

PASSPORT_CATEGORY_CHOICES = [
    ('-','-'),
    ('New Passport','New Passport'),
    ('Renew Passport','Renew Passport')
]

class FlightBook(models.Model):
    # leadno = models.ForeignKey(Lead, on_delete=models.CASCADE,null=True,blank=True)
    flight_from = models.CharField(max_length=100, null=True, blank=True)
    flight_to = models.CharField(max_length=100, null=True, blank=True)
    flight_departure = models.DateField(null=True, blank=True)
    flight_return = models.DateField(null=True, blank=True)
    flight_class = models.CharField(max_length=100, null=True, blank=True,choices=CLASS_CHOICES, default='-')
    category_domestic_flight = models.BooleanField(default=False)
    category_international_flight = models.BooleanField(default=False)
    flight_flexibity = models.CharField(max_length=100, null=True, blank=True,choices=FLEXIBITY_CHOICES,default='-')
    flight_preference = models.CharField(max_length=100, null=True, blank=True,choices=PREFERENCE_CHOICES,default='-')

    def __str__(self) -> str:
        return f'{self.flight_from}'

# class FlightBook(models.Model):
#     leadno = models.ForeignKey(Lead, on_delete=models.CASCADE,null=True,blank=True)
#     flight_from = models.CharField(max_length=100, null=True, blank=True)
#     flight_to = models.CharField(max_length=100, null=True, blank=True)
#     flight_departure = models.DateField(null=True, blank=True)
#     flight_return = models.DateField(null=True, blank=True)
#     flight_class = models.CharField(max_length=100, null=True, blank=True,choices=CLASS_CHOICES, default='-')
#     category_domestic_flight = models.BooleanField(default=False)
#     category_international_flight = models.BooleanField(default=False)
#     flight_flexibity = models.CharField(max_length=100, null=True, blank=True,choices=FLEXIBITY_CHOICES,default='-')
#     flight_preference = models.CharField(max_length=100, null=True, blank=True,choices=PREFERENCE_CHOICES,default='-')

#     def save(self, *args, **kwargs):
#         if not self.leadno:
#             # Set the leadno field to the same value as the leadno field of the associated Lead instance
#             self.leadno = Lead.objects.create().leadno
        
#         super().save(*args, **kwargs)

#     def __str__(self) -> str:
#         return f'{self.flight_from}'



# class HotelBook(models.Model):
#     hotel_country = CountryField(null=True, blank=True)
#     hotel_city = models.CharField(max_length=100, null=True, blank=True)
#     hotel_roomtype = models.CharField(max_length=100,null=True,blank=True,choices=ROOM_TYPE_CHOICES,default='-')
#     hotel_starrate = models.CharField(max_length=100,null=True,blank=True,choices=STAR_RATE_CHOICES,default='-')
#     hotel_checkin = models.DateField(null=True,blank=True)
#     hotel_checkout = models.DateField(null=True,blank=True)
#     hotel_nofnight = models.IntegerField(null=True,blank=True)
#     hotel_bugdet = models.CharField(max_length=100,null=True,blank=True)
#     hotel_hotelname = models.CharField(max_length=100,null=True,blank=True)
#     hotel_nofroom = models.IntegerField(null=True,blank=True)

#     def __str__(self) -> str:
#         return f'{self.hotel_country}'

# class Visa(models.Model):
#     visa_country = CountryField(null=True, blank=True)
#     visa_visacategory = models.CharField(max_length=100, null=True, blank=True,choices=VISA_CATEGORY_CHOICES,default='-')
#     visa_visittype = models.CharField(max_length=100, null=True, blank=True,choices=VISIT_TYPE_CHOICES,default='-')
#     visa_duration = models.CharField(max_length=100, null=True, blank=True)
#     visa_traveldate = models.DateField(null=True,blank=True)
#     visa_jobprofile = models.CharField(max_length=100, null=True, blank=True)
#     visa_age = models.CharField(max_length=100, null=True, blank=True)
#     visa_qualification = models.CharField(max_length=100, null=True, blank=True)
#     visa_description = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self) -> str:
#         return f'{self.visa_country}'
    
# class TravelInsurance(models.Model):
#     travel_country = CountryField(null=True, blank=True)
#     travel_howlong = models.CharField(max_length=100, null=True, blank=True)
#     travel_traveldate = models.DateField(null=True,blank=True)
#     travel_insurancevisa = models.CharField(max_length=100, null=True,blank=True,choices=INSURANCE_VISA_CHOICES,default='-')

#     def __str__(self) -> str:
#         return f'{self.travel_country}'
    
# class Forex(models.Model):
#     forex_currency = CountryField(null=True, blank=True)
#     forex_amount = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self) -> str:
#         return f'{self.forex_currency}'

# class Sightseeings(models.Model):
#     sight_country = CountryField(null=True, blank=True)
#     sight_city = models.CharField(max_length=100, null=True, blank=True)
#     sightseeingoption = models.CharField(max_length=100, null=True, blank=True)
#     sight_preference = models.CharField(max_length=100, null=True, blank=True,choices=PREFERENCES_CHOICES,default='-')
#     sight_traveldate = models.DateField(null=True,blank=True)

#     def __str__(self) -> str:
#         return f'{self.sight_country}'

# class Transport(models.Model):
#     transport_country = CountryField(null=True, blank=True)
#     transport_city = models.CharField(max_length=100, null=True, blank=True)
#     transport_transportdate = models.DateField(null=True,blank=True)
#     transport_dropdate = models.DateField(null=True,blank=True)
#     transport_preference = models.CharField(max_length=100, null=True, blank=True,choices=TRANSPORT_PREFERENCES_CHOICES,default='-')
#     transport_airport_transfers = models.BooleanField(default=False)
#     transport_sightseeing_transfers = models.BooleanField(default=False)
#     transport_other = models.BooleanField(default=False)

#     def __str__(self) -> str:
#         return f'{self.transport_country}'
    
# class Other(models.Model):
#     other_country = CountryField(null=True, blank=True)
#     other_traveldate = models.DateField(null=True,blank=True)
#     other_nofdays = models.IntegerField(null=True, blank=True)
#     other_subcategory = models.CharField(max_length=100, null=True, blank=True)
#     other_description = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self) -> str:
#         return f'{self.other_country}'
    
# class PackageDetails(models.Model):
#     package_traveldate = models.DateField(null=True,blank=True)
#     package_bugdet = models.CharField(max_length=100,null=True,blank=True)
#     package_selectcountry = CountryField(null=True, blank=True)
#     package_packagename = models.CharField(max_length=100,null=True,blank=True)
#     package_extradetails = models.CharField(max_length=100,null=True,blank=True)

#     def __str__(self) -> str:
#         return f'{self.package_traveldate}'
    
# class CustomizePackage(models.Model):
#     customize_selectcountry = CountryField(null=True, blank=True)
#     customize_services = models.CharField(max_length=100,null=True,blank=True)
#     customize_hotelrate = models.CharField(max_length=100,null=True,blank=True,choices=STAR_RATE_CHOICES,default='-')
#     customize_traveldate = models.DateField(null=True,blank=True)
#     customize_nofnight = models.IntegerField(null=True,blank=True)
#     customize_flexibity = models.CharField(max_length=100, null=True, blank=True,choices=FLEXIBITY_CHOICES,default='-')
#     customize_nofroom = models.IntegerField(null=True,blank=True)
#     customize_preference = models.CharField(max_length=100, null=True, blank=True,choices=PREFERENCES_CHOICES,default='-')
#     customize_bugdet = models.CharField(max_length=100,null=True,blank=True)
#     customize_description = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self) -> str:
#         return f'{self.customize_selectcountry}'
    
# class Bus(models.Model):
#     bus_country = CountryField(null=True, blank=True)
#     bus_from = models.CharField(max_length=100, null=True, blank=True)
#     bus_to = models.CharField(max_length=100, null=True, blank=True)
#     bus_departure = models.DateField(null=True, blank=True)
#     bus_return = models.DateField(null=True, blank=True)
#     bus_preference = models.CharField(max_length=100, null=True, blank=True,choices=PREFERENCES_CHOICES,default='-')
#     bus_remark = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self) -> str:
#         return f'{self.bus_country}'
    
# class Train(models.Model):
#     train_country = CountryField(null=True, blank=True)
#     train_from = models.CharField(max_length=100, null=True, blank=True)
#     train_to = models.CharField(max_length=100, null=True, blank=True)
#     train_departure = models.DateField(null=True, blank=True)
#     train_return = models.DateField(null=True, blank=True)
#     train_preference = models.CharField(max_length=100, null=True, blank=True,choices=PREFERENCES_CHOICES,default='-')
#     train_remark = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self) -> str:
#         return f'{self.train_country}'
    
# class Passport(models.Model):
#     pass_issuingcountry = CountryField(null=True, blank=True)
#     pass_date = models.DateField(null=True, blank=True)
#     pass_passportno = models.CharField(max_length=100, null=True, blank=True)
#     pass_placeapply = models.CharField(max_length=100, null=True, blank=True)
#     pass_nofperson = models.IntegerField(null=True, blank=True)
#     pass_category = models.CharField(max_length=100,null=True,blank=True,choices=PASSPORT_CATEGORY_CHOICES,default='-')
#     pass_urgent = models.BooleanField(default=False)
#     pass_remark = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self) -> str:
#         return f'{self.pass_issuingcountry}'
    
# class Cruise(models.Model):
#     cruise_country = CountryField(null=True, blank=True)
#     cruise_city = models.CharField(max_length=100, null=True, blank=True)
#     cruise_days = models.IntegerField(null=True, blank=True)
#     cruisename = models.CharField(max_length=100, null=True, blank=True)
#     cruise_type = models.CharField(max_length=100, null=True, blank=True)
#     cruise_departure = models.DateField(null=True, blank=True)
#     cruise_return = models.DateField(null=True, blank=True)
#     cruise_roomtype = models.CharField(max_length=100, null=True, blank=True,choices=PREFERENCES_CHOICES,default='-')
#     cruise_remark = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self) -> str:
#         return f'{self.cruise_country}'
    
# class Adventure(models.Model):
#     adventure_country = CountryField(null=True, blank=True)
#     adventure_city = models.CharField(max_length=100, null=True, blank=True)
#     adventure_traveldate = models.DateField(null=True,blank=True)
#     category_motor_biking = models.BooleanField(default=False)
#     category_camping = models.BooleanField(default=False)
#     category_safari = models.BooleanField(default=False)
#     category_water_sports = models.BooleanField(default=False)
#     adventure_remark = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self) -> str:
#         return f'{self.adventure_country}'
    
# class GroupPackage(models.Model):
#     group_selectcountry = CountryField(null=True, blank=True)
#     group_packagename = models.CharField(max_length=100,null=True,blank=True)
#     group_preference = models.CharField(max_length=100, null=True, blank=True,choices=TRANSPORT_PREFERENCES_CHOICES,default='-')
#     group_remark = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self) -> str:
#         return f'{self.group_selectcountry}'
    






