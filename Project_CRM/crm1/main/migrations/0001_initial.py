# Generated by Django 4.1.7 on 2023-03-29 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FlightBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_from', models.CharField(blank=True, max_length=100, null=True)),
                ('flight_to', models.CharField(blank=True, max_length=100, null=True)),
                ('flight_departure', models.DateField(blank=True, null=True)),
                ('flight_return', models.DateField(blank=True, null=True)),
                ('flight_class', models.CharField(blank=True, choices=[('-', '-'), ('All', 'All'), ('Economy', 'Economy'), ('Premium Economy', 'Premium Economy'), ('Business', 'Business'), ('First Class', 'First Class')], default='-', max_length=100, null=True)),
                ('category_domestic_flight', models.BooleanField(default=False)),
                ('category_international_flight', models.BooleanField(default=False)),
                ('flight_flexibity', models.CharField(blank=True, choices=[('-', '-'), ('+/- 0 Day', '+/- 0 Day'), ('+/- 3 Day', '+/- 3 Day'), ('+/- 6 Day', '+/- 6 Day'), ('+/- 1 Week', '+/- 1 Week'), ('+/- 3 Week', '+/- 3 Week')], default='-', max_length=100, null=True)),
                ('flight_preference', models.CharField(blank=True, choices=[('-', '-'), ('All', 'All'), ('One Stop', 'One Stop'), ('Cheapest', 'Cheapest'), ('Direct', 'Direct')], default='-', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WhatsAppNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('vehicletype', models.CharField(choices=[('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'), ('MPV', 'MPV'), ('SUV', 'SUV')], default='Select Vehicle Type', max_length=100, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('internalremark', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_vehicle', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=255, null=True)),
                ('aliasname', models.CharField(blank=True, max_length=255, null=True)),
                ('gst', models.IntegerField(blank=True, null=True)),
                ('billingaddress', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('deals_in_visa', models.BooleanField(default=False)),
                ('deals_in_flights', models.BooleanField(default=False)),
                ('deals_in_hotel', models.BooleanField(default=False)),
                ('deals_in_travel_insurance', models.BooleanField(default=False)),
                ('deals_in_forex', models.BooleanField(default=False)),
                ('deals_in_sightseeing', models.BooleanField(default=False)),
                ('deals_in_transport', models.BooleanField(default=False)),
                ('deals_in_cruise', models.BooleanField(default=False)),
                ('deals_in_other', models.BooleanField(default=False)),
                ('deals_in_package', models.BooleanField(default=False)),
                ('deals_in_customize_package', models.BooleanField(default=False)),
                ('deals_in_bus', models.BooleanField(default=False)),
                ('deals_in_train', models.BooleanField(default=False)),
                ('deals_in_passport', models.BooleanField(default=False)),
                ('deals_in_adventure', models.BooleanField(default=False)),
                ('deals_in_group_package', models.BooleanField(default=False)),
                ('country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('tags', models.CharField(choices=[('All', 'All'), ('Family', 'Family'), ('Honeymoon', 'Honeymoon'), ('Individual', 'Individual'), ('Adventure', 'Adventure'), ('Group', 'Group'), ('Women Only', 'Women Only'), ('Domestic', 'Domestic'), ('International', 'International'), ('Beaches', 'Beaches'), ('Weekend', 'Weekend'), ('Heritage', 'Heritage'), ('Wildlife', 'Wildlife'), ('Jungle Safari', 'Jungle Safari'), ('Student', 'Student'), ('Pilgrimage', 'Pilgrimage'), ('Popular', 'Popular'), ('Trending', 'Trending')], default='All', max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, null=True, region=None)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('alternatenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, null=True, region=None)),
                ('alternateemail', models.EmailField(blank=True, max_length=254, null=True)),
                ('preffered_supplier', models.BooleanField(default=False)),
                ('inactive_supplier', models.BooleanField(default=False)),
                ('default_email', models.BooleanField(default=False)),
                ('cc_email', models.BooleanField(default=False)),
                ('bankdetails', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_supplier', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sightseeing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('activity', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(null=True)),
                ('inclusion', models.TextField(null=True)),
                ('exclusion', models.TextField(null=True)),
                ('duration', models.CharField(max_length=255, null=True)),
                ('closeday', models.CharField(max_length=255, null=True)),
                ('timings', models.CharField(max_length=255, null=True)),
                ('transport', models.CharField(choices=[('Private', 'Private'), ('SIC', 'SIC'), ('Other', 'Other')], default='Private', max_length=255, null=True)),
                ('time', models.CharField(max_length=255, null=True)),
                ('remark', models.TextField(null=True)),
                ('internalremark', models.TextField(null=True)),
                ('externalremark', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_sightseen', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packagename', models.CharField(blank=True, max_length=100, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('days', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='1', max_length=100)),
                ('detailed_itenerary', models.TextField(blank=True, null=True)),
                ('tags', models.CharField(choices=[('All', 'All'), ('Family', 'Family'), ('Honeymoon', 'Honeymoon'), ('Individual', 'Individual'), ('Adventure', 'Adventure'), ('Group', 'Group'), ('Women Only', 'Women Only'), ('Domestic', 'Domestic'), ('International', 'International'), ('Beaches', 'Beaches'), ('Weekend', 'Weekend'), ('Heritage', 'Heritage'), ('Wildlife', 'Wildlife'), ('Jungle Safari', 'Jungle Safari'), ('Student', 'Student'), ('Pilgrimage', 'Pilgrimage'), ('Popular', 'Popular'), ('Trending', 'Trending')], default='All', max_length=100)),
                ('overview', models.CharField(blank=True, max_length=1000)),
                ('mealtype', models.CharField(choices=[('AP(Full Board)', 'AP(Full Board)'), ('MAP(Half Board)', 'MAP(Half Board)'), ('CP(Only Breakfast)', 'CP(Only Breakfast)'), ('EP(No Meal)', 'EP(No Meal)'), ('Any(Any type of meal)', 'Any(Any type of meal)'), ('AI(All Inclusive)', 'AI(All Inclusive)')], default='AI(All Inclusive)', max_length=100)),
                ('hotel_details', models.TextField(blank=True, max_length=500, null=True)),
                ('free_wi_fi', models.BooleanField(default=False)),
                ('airport_transfers_private', models.BooleanField(default=False)),
                ('airport_transfers_sic', models.BooleanField(default=False)),
                ('travel_insurance', models.BooleanField(default=False)),
                ('visa', models.BooleanField(default=False)),
                ('Inter_hotel_transfer_private', models.BooleanField(default=False)),
                ('sightseeing_transfer_private', models.BooleanField(default=False)),
                ('sightseeing_transfer_sic', models.BooleanField(default=False)),
                ('Inter_hotel_transfer_sic', models.BooleanField(default=False)),
                ('candlelight_dinner', models.BooleanField(default=False)),
                ('bed_decorations', models.BooleanField(default=False)),
                ('honeymoon_cake', models.BooleanField(default=False)),
                ('private_ferry', models.BooleanField(default=False)),
                ('private_cruise', models.BooleanField(default=False)),
                ('scuba_diving', models.BooleanField(default=False)),
                ('parasailing', models.BooleanField(default=False)),
                ('sea_walk', models.BooleanField(default=False)),
                ('photoshoot_for_couple', models.BooleanField(default=False)),
                ('candle_light_dinner_with_wine', models.BooleanField(default=False)),
                ('candle_light_dinner_without_wine', models.BooleanField(default=False)),
                ('jet_ski', models.BooleanField(default=False)),
                ('snorkeling', models.BooleanField(default=False)),
                ('airport_transfers_speed_boat_seaplane', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('inclusive', models.TextField(blank=True, max_length=1000, null=True)),
                ('exclusive', models.TextField(blank=True, max_length=1000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('terms_and_conditions', models.TextField(blank=True, max_length=1000, null=True)),
                ('cancellation_policy', models.TextField(blank=True, max_length=1000, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_package', to=settings.AUTH_USER_MODEL)),
                ('destinations', models.ManyToManyField(blank=True, null=True, to='main.destination')),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leadno', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('customertype', models.CharField(choices=[('B2B', 'B2B'), ('B2C', 'B2C'), ('Corporate', 'Corporate'), ('VIP', 'VIP')], default='B2B', max_length=100)),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None)),
                ('email', models.EmailField(max_length=100)),
                ('salutation', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Dr', 'Dr')], default='Mr', max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('city', models.CharField(max_length=100)),
                ('alternatenumber', models.CharField(blank=True, max_length=15, null=True)),
                ('alternateemail', models.EmailField(blank=True, max_length=100, null=True)),
                ('leadsource', models.CharField(choices=[('Advertisement', 'Advertisement'), ('Cold Call', 'Cold Call'), ('Employee Referral', 'Employee Referral'), ('External Referral', 'External Referral'), ('Website', 'Website'), ('Public Relation', 'Public Relation'), ('Email Campaign', 'Email Campaign'), ('SMS Campaign', 'SMS Campaign'), ('Trade Show', 'Trade Show'), ('None', 'None'), ('Old Customer', 'Old Customer'), ('New Customer', 'New Customer'), ('Walk In', 'Walk In'), ('SEO', 'SEO'), ('Excel', 'Excel'), ('Just Dial', 'Just Dial'), ('Phone Call', 'Phone Call'), ('Airbnb', 'Airbnb'), ('Live Chat', 'Live Chat'), ('Travvolt', 'Travvolt'), ('Hello Travel', 'Hello Travel'), ('TripShelf', 'TripShelf'), ('Newspaper', 'Newspaper'), ('Sulekha', 'Sulekha'), ('Travel Triangle', 'Travel Triangle'), ('TripCrafters', 'TripCrafters'), ('Other', 'Other'), ('Flyer', 'Flyer'), ('Travelsetu', 'Travelsetu'), ('Facebook', 'Facebook'), ('Google Ads', 'Google Ads'), ('Instagram', 'Instagram'), ('10Times', '10Times'), ('Rotary', 'Rotary'), ('BNI', 'BNI'), ('YES', 'YES'), ('Mail', 'Mail'), ('Agent', 'Agent'), ('Google', 'Google'), ('Whatsapp', 'Whatsapp'), ('Webmail', 'Webmail'), ('Direct Sales', 'Direct Sales'), ('Incoming Call', 'Incoming Call'), ('Chat', 'Chat'), ('Brouchers', 'Brouchers')], default='Advertisement', max_length=100, null=True)),
                ('priority', models.CharField(choices=[('All', 'All'), ('Cold', 'Cold'), ('Warm', 'Warm'), ('Hot', 'Hot')], default='All', max_length=100)),
                ('status', models.CharField(choices=[('All', 'All'), ('Unquilified', 'Unquilified'), ('New', 'New'), ('Working', 'Working'), ('Proposal Sent', 'Proposal Sent'), ('Negotiating', 'Negotiating'), ('Booked', 'Booked'), ('Lost', 'Lost')], default='All', max_length=100, null=True)),
                ('adults', models.IntegerField(blank=True)),
                ('child', models.CharField(blank=True, max_length=15, null=True)),
                ('infants', models.CharField(blank=True, max_length=15, null=True)),
                ('tags', models.CharField(choices=[('All', 'All'), ('Family', 'Family'), ('Honeymoon', 'Honeymoon'), ('Individual', 'Individual'), ('Adventure', 'Adventure'), ('Group', 'Group'), ('Women Only', 'Women Only'), ('Domestic', 'Domestic'), ('International', 'International'), ('Beaches', 'Beaches'), ('Weekend', 'Weekend'), ('Heritage', 'Heritage'), ('Wildlife', 'Wildlife'), ('Jungle Safari', 'Jungle Safari'), ('Student', 'Student'), ('Pilgrimage', 'Pilgrimage'), ('Popular', 'Popular'), ('Trending', 'Trending')], default='All', max_length=100, null=True)),
                ('triptype', models.CharField(choices=[('Other', 'Other'), ('Family', 'Family'), ('Honeymoon', 'Honeymoon'), ('Friends', 'Friends'), ('Official', 'Official'), ('Adventure', 'Adventure'), ('Corporate', 'Corporate'), ('Educational', 'Educational'), ('Group', 'Group'), ('Individual', 'Individual'), ('Religious', 'Religious'), ('Couple', 'Couple'), ('Student Group', 'Student Group')], default='Other', max_length=100, null=True)),
                ('destination', models.CharField(blank=True, default='-', max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('enquiry_flight_booking', models.BooleanField(default=False)),
                ('enquiry_hotel_booking', models.BooleanField(default=False)),
                ('enquiry_visa', models.BooleanField(default=False)),
                ('enquiry_travel_insurance', models.BooleanField(default=False)),
                ('enquiry_forex', models.BooleanField(default=False)),
                ('enquiry_sightseeing', models.BooleanField(default=False)),
                ('enquiry_transport', models.BooleanField(default=False)),
                ('enquiry_other', models.BooleanField(default=False)),
                ('enquiry_package', models.BooleanField(default=False)),
                ('enquiry_customize_package', models.BooleanField(default=False)),
                ('enquiry_bus', models.BooleanField(default=False)),
                ('enquiry_train', models.BooleanField(default=False)),
                ('enquiry_passport', models.BooleanField(default=False)),
                ('enquiry_cruise', models.BooleanField(default=False)),
                ('enquiry_adventure', models.BooleanField(default=False)),
                ('enquiry_group', models.BooleanField(default=False)),
                ('assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelname', models.CharField(blank=True, max_length=100, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(max_length=20, null=True, region=None)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('rate', models.CharField(choices=[('-', '-'), ('All', 'All'), ('One Star', 'One Star'), ('Two Star', 'Two Star'), ('Three Star', 'Three Star'), ('Four Star', 'Four Star'), ('Five Star', 'Five Star')], default='All', max_length=100)),
                ('htype', models.CharField(choices=[('-', '-'), ('All', 'All'), ('Standard', 'Standard'), ('Deluxe', 'Deluxe'), ('Any', 'Any')], default='-', max_length=100)),
                ('childfreeage', models.CharField(blank=True, max_length=100, null=True)),
                ('childwithoutfreeage', models.CharField(blank=True, max_length=100, null=True)),
                ('amenities', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_hotel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=20, null=True, region=None)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('salutation', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Dr', 'Dr')], default='Mr', max_length=100, null=True)),
                ('firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('lastname', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('address2', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('alternateaddress', models.CharField(blank=True, max_length=200, null=True)),
                ('alternatemobile', phonenumber_field.modelfields.PhoneNumberField(max_length=20, null=True, region=None)),
                ('alternateemail', models.EmailField(blank=True, max_length=100, null=True)),
                ('source', models.CharField(choices=[('Advertisement', 'Advertisement'), ('Cold Call', 'Cold Call'), ('Employee Referral', 'Employee Referral'), ('External Referral', 'External Referral'), ('Website', 'Website'), ('Public Relation', 'Public Relation'), ('Email Campaign', 'Email Campaign'), ('SMS Campaign', 'SMS Campaign'), ('Trade Show', 'Trade Show'), ('None', 'None'), ('Old Customer', 'Old Customer'), ('New Customer', 'New Customer'), ('Walk In', 'Walk In'), ('SEO', 'SEO'), ('Excel', 'Excel'), ('Just Dial', 'Just Dial'), ('Phone Call', 'Phone Call'), ('Airbnb', 'Airbnb'), ('Live Chat', 'Live Chat'), ('Travvolt', 'Travvolt'), ('Hello Travel', 'Hello Travel'), ('TripShelf', 'TripShelf'), ('Newspaper', 'Newspaper'), ('Sulekha', 'Sulekha'), ('Travel Triangle', 'Travel Triangle'), ('TripCrafters', 'TripCrafters'), ('Other', 'Other'), ('Flyer', 'Flyer'), ('Travelsetu', 'Travelsetu'), ('Facebook', 'Facebook'), ('Google Ads', 'Google Ads'), ('Instagram', 'Instagram'), ('10Times', '10Times'), ('Rotary', 'Rotary'), ('BNI', 'BNI'), ('YES', 'YES'), ('Mail', 'Mail'), ('Agent', 'Agent'), ('Google', 'Google'), ('Whatsapp', 'Whatsapp'), ('Webmail', 'Webmail'), ('Direct Sales', 'Direct Sales'), ('Incoming Call', 'Incoming Call'), ('Chat', 'Chat'), ('Brouchers', 'Brouchers')], default='Advertisement', max_length=100, null=True)),
                ('customertype', models.CharField(choices=[('B2B', 'B2B'), ('B2C', 'B2C'), ('Corporate', 'Corporate'), ('VIP', 'VIP')], default='B2B', max_length=100)),
                ('accounthead', models.CharField(blank=True, max_length=100, null=True)),
                ('tags', models.CharField(choices=[('All', 'All'), ('Family', 'Family'), ('Honeymoon', 'Honeymoon'), ('Individual', 'Individual'), ('Adventure', 'Adventure'), ('Group', 'Group'), ('Women Only', 'Women Only'), ('Domestic', 'Domestic'), ('International', 'International'), ('Beaches', 'Beaches'), ('Weekend', 'Weekend'), ('Heritage', 'Heritage'), ('Wildlife', 'Wildlife'), ('Jungle Safari', 'Jungle Safari'), ('Student', 'Student'), ('Pilgrimage', 'Pilgrimage'), ('Popular', 'Popular'), ('Trending', 'Trending')], default='All', max_length=100, null=True)),
                ('flyer', models.CharField(blank=True, max_length=100, null=True)),
                ('food', models.CharField(choices=[('All', 'All'), ('Vegetarian', 'Vegetarian'), ('NonVegetarian', 'NonVegetarian'), ('Jainism', 'Jainism'), ('Sweet', 'Sweet')], default='All', max_length=100)),
                ('pan', models.CharField(blank=True, max_length=30, null=True)),
                ('passport', models.CharField(blank=True, max_length=30, null=True)),
                ('enquirydate', models.DateField(blank=True, null=True)),
                ('issuedate', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
