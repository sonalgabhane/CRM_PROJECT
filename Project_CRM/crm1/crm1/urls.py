
from django.contrib import admin
from django.urls import path,include
from main import views
from Useraccount.views import RegisterView,LoginView ,UserDeleteView
urlpatterns = [
    path("admin/", admin.site.urls),
    # path("",views.home),
    path('accounts/', include('allauth.urls')),
    path("",views.maincontent,name="maincontent"),
    path("about/",views.about ,name="about"), 
    path("features/",views.features ,name="features"),
    path("calendy/",views.calendy,name="calendy"),
    path("clients/",views.clients,name="clients"),
    path("contactus/",views.contactus,name="contactus"),
    path("pricing/",views.pricing,name="pricing"),
    path("privacypolicy/",views.privacypolicy,name="privacypolicy"),
    path("termsandconditions/",views.termsandconditions,name="termsandconditions"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("leads/",views.leads,name="leads"),
    path("addleads/",views.addleads,name="addleads"),
    path("editleads/<int:id>",views.editleads,name="editleads"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('viewlead/<int:id>', views.viewlead, name='viewlead'),
    path('user/', views.people, name='user'),
    path('adduser/', views.AdduserView.as_view(), name='adduser'),
    path("edituser/<int:id>",views.edituser,name="edituser"),
    path('viewuser/<int:id>', views.viewUser, name='viewuser'),
    path("customer/",views.contact,name="customer"),
    path("addcustomer/",views.addcustomer,name="addcustomer"),
    path("editcustomer/<int:id>",views.editcustomer,name="editcustomer"),
    path('viewcustomer/<int:id>', views.viewcustomer, name='viewcustomer'),
    path("supplier/",views.Supplier,name="supplier"),
    path("addsupplier/",views.addsupplier,name="addsupplier"),
    path('viewsupplier/<int:id>', views.viewsupplier, name='viewsupplier'),
    path("signup/",RegisterView.as_view(),name="signup"),
    path("login/",LoginView.as_view(),name="login"),
    path("logout/",views.logoutPage,name="logout"),
    path("sightseeing/",views.sightseeing,name="sightseeing"),
    path("addsightseeing/",views.addsightseeing,name="addsightseeing"),
    path("editsightseeing/<int:id>",views.editsightseeing,name="editsightseeing"),
    path('viewsightseeing/<int:id>', views.viewsightseeing, name='viewsightseeing'),
    path("transport/",views.transport,name="transport"),
    path("addtransport/",views.addtransport,name="addtransport"),
    path("edittransport/<int:id>",views.edittransport,name="edittransport"),
    path('viewtransport/<int:id>', views.viewtransport, name='viewtransport'),
    path("visainfo/",views.visa,name="visa"),
    path("addvisa/",views.addvisa,name="addvisa"),
    path('viewprofile/<int:id>', views.viewProfile, name='viewprofile'),
    path("hotels/",views.hotels, name="hotels"),
    path("addhotels/",views.addhotels, name="addhotels"),
    path("viewhotels/<int:id>",views.viewhotels,name="viewhotels"),
    path("edithotels/<int:id>",views.edithotels,name="edithotels"),
    path("packages/",views.packages, name="packages"),
    path("addpackages/",views.addpackages, name="addpackages"),
    path('viewpackages/<int:id>',views.viewpackages, name='viewpackages'),
    # path('editpackages/<int:id>',views.editpackages, name='editpackages'),
    path('generateinvoice/<int:id>', views.GenerateInvoice.as_view(), name = 'generateinvoice'),
    path("editpackages/<int:pk>", views.PackageUpdateView.as_view(), name="editpackages"),
    path("add/", views.BirdAddView.as_view(), name="add_bird"),


    # api urls 
    path("leadapi/",views.lead_api),
    path("leadapi/<int:pk>", views.lead_api),
    path("customerapi/", views.customer_api),
    path("customerapi/<int:pk>", views.customer_api),
    path("supplierapi/", views.supplier_api),
    path("supplierapi/<int:pk>", views.supplier_api),
    path("sightseeingapi/", views.sightseeing_api),
    path("sightseeingapi/<int:pk>", views.sightseeing_api),
    path("packageapi/", views.package_api),
    path("packageapi/<int:pk>", views.package_api),
    path("vehicleapi/", views.vehicle_api),
    path("vehicleapi/<int:pk>", views.vehicle_api),
    path("hotelapi/", views.hotel_api),
    path("hotelapi/<int:pk>", views.hotel_api),
    path("userapi/", views.user_api),
    path("userapi/<int:pk>", views.user_api),



    # Enquiry Type Forms Urls
    path('addflightbook/', views.addflightbook, name='addflightbook'),

   

]
