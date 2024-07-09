from django.contrib import admin
from .models import *
    
class LeadAdmin(admin.ModelAdmin):
    list_display = ['leadno','customertype','number','email','salutation','firstname','lastname','address','city','alternatenumber','alternateemail','leadsource','priority','status','adults','child','infants','tags','triptype','assigned',
                    'enquiry_flight_booking','enquiry_hotel_booking','enquiry_visa','enquiry_travel_insurance','enquiry_forex','enquiry_sightseeing','enquiry_transport','enquiry_other','enquiry_package','enquiry_customize_package','enquiry_bus','enquiry_train',
                    'enquiry_passport','enquiry_cruise','enquiry_adventure','enquiry_group']
    
class customerAdmin(admin.ModelAdmin):
    list_display = ['number','email','salutation','firstname','lastname','address','address2','city','pincode','alternateaddress','alternatemobile','alternateemail','source','customertype','accounthead','tags','flyer','food','pan','passport','enquirydate','issuedate']

class supplierAdmin(admin.ModelAdmin):
    list_display=['companyname','aliasname','name','number','email']
   
class sightseeingAdmin(admin.ModelAdmin):
    list_display=['country','city','activity','duration','image'] 
    
class VehicleAdmin(admin.ModelAdmin):
    list_display=['country','city','vehicletype'] 
    
class HotelAdmin(admin.ModelAdmin):
    list_display = ['hotelname','country','city','address','contact','email','rate','htype','childfreeage','childwithoutfreeage','amenities','description','image']

class DestinationAdmin(admin.ModelAdmin):
    list_display=['destination'] 
    
    
class PackageAdmin(admin.ModelAdmin):
    raw_id_fields = ['destinations']
    list_display = ['packagename','country','tags','overview','mealtype','image','inclusive','exclusive']

class WhatsappAdmin(admin.ModelAdmin):
    list_display = ['number']

admin.site.register(Lead,LeadAdmin)
admin.site.register(customer,customerAdmin)
admin.site.register(supplier,supplierAdmin)
admin.site.register(Sightseeing,sightseeingAdmin)
admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(Hotel,HotelAdmin)
admin.site.register(Package,PackageAdmin)
admin.site.register(Destination,DestinationAdmin)
admin.site.register(WhatsAppNumber,WhatsappAdmin)


# Enquiry Type 
class FlightBookAdmin(admin.ModelAdmin):
    list_display = ['flight_from','flight_to','flight_departure','flight_return','flight_class','category_domestic_flight','category_international_flight','flight_flexibity','flight_preference']
admin.site.register(FlightBook,FlightBookAdmin)

# class HotelBookAdmin(admin.ModelAdmin):
#     list_display = ['hotel_country','hotel_city','hotel_roomtype','hotel_starrate','hotel_checkin','hotel_checkout','hotel_nofnight','hotel_bugdet','hotel_hotelname','hotel_nofroom']
# admin.site.register(HotelBook,HotelBookAdmin)

# class VisaAdmin(admin.ModelAdmin):
#     list_display = ['visa_country','visa_visacategory','visa_visittype','visa_duration','visa_traveldate','visa_jobprofile','visa_age','visa_qualification','visa_description']
# admin.site.register(Visa,VisaAdmin)

# class TravelInsuranceAdmin(admin.ModelAdmin):
#     list_display = ['travel_country','travel_howlong','travel_traveldate','travel_insurancevisa']
# admin.site.register(TravelInsurance,TravelInsuranceAdmin)

# class ForexAdmin(admin.ModelAdmin):
#     list_display = ['forex_currency','forex_amount']
# admin.site.register(Forex,ForexAdmin)

# class SightseeingsAdmin(admin.ModelAdmin):
#     list_display = ['sight_country','sight_city','sightseeingoption','sight_preference','sight_traveldate']
# admin.site.register(Sightseeings,SightseeingsAdmin)

# class TransportAdmin(admin.ModelAdmin):
#     list_display = ['transport_country','transport_city','transport_transportdate','transport_dropdate','transport_preference','transport_airport_transfers','transport_sightseeing_transfers','transport_other']
# admin.site.register(Transport,TransportAdmin)

# class OtherAdmin(admin.ModelAdmin):
#     list_display = ['other_country','other_traveldate','other_nofdays','other_subcategory','other_description']
# admin.site.register(Other,OtherAdmin)

# class PackageDetailAdmin(admin.ModelAdmin):
#     list_display = ['package_traveldate','package_bugdet','package_selectcountry','package_packagename','package_extradetails']
# admin.site.register(PackageDetails,PackageDetailAdmin)

# class CustomizePackageAdmin(admin.ModelAdmin):
#     list_display = ['customize_selectcountry','customize_services','customize_hotelrate','customize_hotelrate','customize_nofnight','customize_flexibity','customize_nofroom','customize_preference','customize_bugdet','customize_description']
# admin.site.register(CustomizePackage,CustomizePackageAdmin)

# class BusAdmin(admin.ModelAdmin):
#     list_display = ['bus_country','bus_from','bus_to','bus_departure','bus_return','bus_preference','bus_remark']
# admin.site.register(Bus,BusAdmin)

# class TrainAdmin(admin.ModelAdmin):
#     list_display = ['train_country','train_from','train_to','train_departure','train_return','train_preference','train_remark']
# admin.site.register(Train,TrainAdmin)

# class PassportAdmin(admin.ModelAdmin):
#     list_display = ['pass_issuingcountry','pass_date','pass_passportno','pass_placeapply','pass_nofperson','pass_category','pass_urgent','pass_remark']
# admin.site.register(Passport,PassportAdmin)

# class CruiseAdmin(admin.ModelAdmin):
#     list_display = ['cruise_country','cruise_city','cruise_days','cruisename','cruise_type','cruise_departure','cruise_return','cruise_roomtype','cruise_remark']
# admin.site.register(Cruise,CruiseAdmin)

# class AdventureAdmin(admin.ModelAdmin):
#     list_display = ['adventure_country','adventure_city','adventure_traveldate','category_motor_biking','category_camping','category_safari','category_water_sports','adventure_remark']
# admin.site.register(Adventure,AdventureAdmin)

# class GroupPackageAdmin(admin.ModelAdmin):
#     list_display = ['group_selectcountry','group_packagename','group_preference','group_remark']
# admin.site.register(GroupPackage,GroupPackageAdmin)




# from django.contrib import admin
# from django.urls import reverse
# from django.utils.html import format_html
# from django.contrib.auth.models import User
# from Useraccount.models import User

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'is_staff', 'is_active', 'block_user_link')

#     def block_user_link(self, obj):
#         if obj.is_active:
#             url = reverse('admin:block_user', args=[obj.id])
#             return format_html('<a href="{}">Block user</a>', url)
#         else:
#             return format_html('<span style="color: #ccc">Blocked</span>')

#     block_user_link.short_description = 'Block user'

# admin.site.register(User, UserAdmin)
# admin.site.unregister(User)




