from django.db import models

# Create your models here.
class Agent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=25)
    line = models.CharField(max_length=25, blank=True)
    whatsapp = models.CharField(max_length=25, blank=True)
    wechat = models.CharField(max_length=25, blank=True)
    skype = models.CharField(max_length=25, blank=True)
    agency = models.CharField(max_length=30)
    experience = models.IntegerField()
    address_line_1 = models.CharField(max_length=30)
    address_line_2 = models.CharField(max_length=30, blank=True)
    address_line_3 = models.CharField(max_length=30, blank=True)
    postcode = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    latitude = models.CharField(max_length=30, blank=True)
    longitude = models.CharField(max_length=30, blank=True)
    website = models.CharField(max_length=30, blank=True)
    properties = models.ForeignKey("Property", on_delete=models.CASCADE, related_name='agencies', blank=True, null=True)
    industry_affiliations = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.agency}'

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=25, blank=True)
    saved_properties = models.ForeignKey("Property", on_delete=models.CASCADE, related_name="saved_properties", blank=True, null=True)
    viewed_properties = models.ForeignKey("Property", on_delete=models.CASCADE, related_name="property_history", blank=True, null=True)
    saved_agents = models.ForeignKey("Agent", on_delete=models.CASCADE, related_name="agent_history", blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Property(models.Model):
    property_id = models.CharField(max_length=30, blank=True)
    property_available = models.BooleanField(default=False)
    property_sold = models.BooleanField(default=False)
    property_name = models.CharField(max_length=30, blank=True)
    building_name = models.CharField(max_length=30, blank=True)
    address_line_1 = models.CharField(max_length=30)
    address_line_2 = models.CharField(max_length=30, blank=True)
    address_line_3 = models.CharField(max_length=30, blank=True)
    postcode = models.CharField(max_length=30)
    area = models.ForeignKey("Area", on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey("City", on_delete=models.CASCADE, blank=True, null=True)
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    property_type = models.ForeignKey("PropertyType", on_delete=models.CASCADE, related_name="property_type", blank=True, null=True)
    which_floor = models.IntegerField()
    total_square_m = models.IntegerField()
    total_square_ft = models.IntegerField()
    total_square_ping = models.IntegerField()
    number_of_bedrooms = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    images = models.CharField(max_length=50, blank=True)
    property_description_short = models.CharField(max_length=500)
    property_description_long = models.CharField(max_length=1500)
    nearby_stations = models.ForeignKey("Station", on_delete=models.CASCADE, related_name="station_area",blank=True, null=True)
    nearby_schools = models.ForeignKey("School", on_delete=models.CASCADE, related_name="school_area", blank=True, null=True)
    parking_spaces = models.IntegerField()
    parking_type = models.CharField(max_length=10, blank=True)
    property_viewed = models.IntegerField()
    year_built = models.IntegerField()
    year_last_renovated = models.IntegerField(blank=True)
    previous_owners = models.IntegerField()
    developer = models.CharField(max_length=50, blank=True)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE, related_name="selling_agent")
    listing_date = models.DateField()
    notes = models.CharField(max_length=500, blank=True)
    key_feature_1 = models.CharField(max_length=50, blank=True)
    key_feature_2 = models.CharField(max_length=50, blank=True)
    key_feature_3 = models.CharField(max_length=50, blank=True)
    key_feature_4 = models.CharField(max_length=50, blank=True)
    key_feature_5 = models.CharField(max_length=50, blank=True)
    pdf_brochure = models.CharField(max_length=50, blank=True)
    balcony = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    concierge = models.BooleanField(default=False)
    shared_pool = models.BooleanField(default=False)
    shared_gym = models.BooleanField(default=False)
    shared_KTV = models.BooleanField(default=False)
    shared_lounge = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    baths = models.IntegerField(default=False)
    showers = models.IntegerField(default=False)
    toilets = models.IntegerField(default=False)
    dining_rooms = models.IntegerField(default=False)
    living_room = models.IntegerField(default=False)
    bedrooms = models.IntegerField(default=False)
    kitchen = models.IntegerField(default=False)
    oven = models.BooleanField(default=False)
    fridge = models.BooleanField(default=False)
    dishwasher = models.BooleanField(default=False)
    double_lock = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    floorplan = models.CharField(max_length=100, blank=True)
    avatar = models.CharField(max_length=100, blank=True)
    images = models.CharField(max_length=100, blank=True)
    video = models.CharField(max_length=100, blank=True)
    property_price = models.IntegerField()
    average_increase_last_year = models.IntegerField(blank=True, null=True)
    average_increase_last_three_years = models.IntegerField(blank=True, null=True)
    average_increase_last_five_years = models.IntegerField(blank=True, null=True)
    estimated_rent = models.IntegerField(blank=True, null=True)
    estimated_yield_pct = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.address_line_1}, {self.area}'

class Station(models.Model):
    station_id = models.IntegerField()
    station_name = models.CharField(max_length=30)
    train_lines = models.CharField(max_length=30)
    nearby_bus_stations = models.CharField(max_length=30)
    city = models.ForeignKey("City", on_delete=models.CASCADE, blank=True, null=True)
    nearby_properties = models.ForeignKey("Property", on_delete=models.CASCADE, related_name="area_properties", blank=True, null=True)
    nearby_agents = models.ForeignKey("Agent", on_delete=models.CASCADE, related_name="area_agents", blank=True, null=True)

    def __str__(self):
        return f'{self.station_name}'

class School(models.Model):
    school_id = models.IntegerField()
    school_name = models.CharField(max_length=30)
    school_type = models.CharField(max_length=30)
    train_lines = models.CharField(max_length=30)
    nearby_bus_stations = models.CharField(max_length=30)
    nearby_properties = models.ForeignKey("Property", on_delete=models.CASCADE, related_name="school_area_properties", blank=True, null=True)
    nearby_agents = models.ForeignKey("Agent", on_delete=models.CASCADE, related_name="school_area_agents", blank=True, null=True)
    average_property_price = models.IntegerField()

    def __str__(self):
        return f'{self.school_name}, {self.school_type}'


class City(models.Model):
    city_id = models.IntegerField()
    city_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    nearby_properties = models.ForeignKey("Property", on_delete=models.CASCADE, related_name="city_properties", blank=True, null=True)
    nearby_agents = models.ForeignKey("Agent", on_delete=models.CASCADE, related_name="city_agencies", blank=True, null=True)
    average_property_price = models.IntegerField()

    def __str__(self):
        return f'{self.city_name}, {self.country}'


class Area(models.Model):
    area_id = models.IntegerField()
    area_name = models.CharField(max_length=30)
    city = models.ForeignKey("City", on_delete=models.CASCADE)
    nearby_properties = models.ForeignKey("Property", on_delete=models.CASCADE, related_name="neighbourhood_properties", blank=True, null=True)
    nearby_agents = models.ForeignKey("Agent", on_delete=models.CASCADE, related_name="neighbourhood_agencies", blank=True, null=True)
    nearby_schools = models.ForeignKey("School", on_delete=models.CASCADE, related_name="neighbourhood_schools", blank=True, null=True)
    nearby_stations = models.ForeignKey("Station", on_delete=models.CASCADE, related_name="neighbourhood_stations", blank=True, null=True)
    average_property_price = models.IntegerField()

    def __str__(self):
        return f'{self.area_name}, {self.city}'

class PropertyType(models.Model):
    PROPERTY_TYPES = (
        ('Flat', 'Flat'),
        ('Penthouse', 'Penthouse'),
        ('Detached House', 'Detached House'),
        ('Semi-Detached House', 'Semi-Detached House'),
        ('Terraced House', 'Terraced House'),
    )
    property_type_id: models.IntegerField()
    property_type_name = models.CharField(max_length=30, choices=PROPERTY_TYPES, default='Flat')
    properties: models.ForeignKey("Property", on_delete=models.CASCADE, related_name="property_type_name", blank=True, null=True)

    def __str__(self):
        return f'{self.property_type_name}'