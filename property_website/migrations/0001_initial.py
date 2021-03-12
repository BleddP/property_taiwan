# Generated by Django 3.1.4 on 2021-03-12 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=15)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=25)),
                ('line', models.CharField(max_length=25)),
                ('whatsapp', models.CharField(max_length=25)),
                ('wechat', models.CharField(max_length=25)),
                ('skype', models.CharField(max_length=25)),
                ('agency', models.CharField(max_length=30)),
                ('experience', models.IntegerField()),
                ('address_line_1', models.CharField(max_length=30)),
                ('address_line_2', models.CharField(max_length=30)),
                ('address_line_3', models.CharField(max_length=30)),
                ('postcode', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('latitude', models.CharField(max_length=30)),
                ('longitude', models.CharField(max_length=30)),
                ('website', models.CharField(max_length=30)),
                ('industry_affiliations', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_id', models.CharField(max_length=30)),
                ('property_available', models.BooleanField(default=False)),
                ('property_name', models.CharField(max_length=30)),
                ('building_name', models.CharField(max_length=30)),
                ('address_line_1', models.CharField(max_length=30)),
                ('address_line_2', models.CharField(max_length=30)),
                ('address_line_3', models.CharField(max_length=30)),
                ('postcode', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('latitude', models.CharField(max_length=30)),
                ('longitude', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('which_floor', models.IntegerField()),
                ('total_square_m', models.IntegerField()),
                ('total_square_ft', models.IntegerField()),
                ('total_square_ping', models.IntegerField()),
                ('number_of_bedrooms', models.IntegerField()),
                ('number_of_bathrooms', models.IntegerField()),
                ('images', models.CharField(max_length=50)),
                ('property_description_short', models.CharField(max_length=500)),
                ('property_description_long', models.CharField(max_length=1500)),
                ('parking_spaces', models.IntegerField()),
                ('parking_type', models.CharField(max_length=10)),
                ('property_viewed', models.IntegerField()),
                ('year_built', models.IntegerField()),
                ('year_last_renovated', models.IntegerField()),
                ('previous_owners', models.IntegerField()),
                ('developer', models.CharField(max_length=50)),
                ('listing_date', models.DateField()),
                ('notes', models.CharField(max_length=500)),
                ('key_feature_1', models.CharField(max_length=50)),
                ('key_feature_2', models.CharField(max_length=50)),
                ('key_feature_3', models.CharField(max_length=50)),
                ('key_feature_4', models.CharField(max_length=50)),
                ('key_feature_5', models.CharField(max_length=50)),
                ('pdf_brochure', models.CharField(max_length=50)),
                ('garden', models.BooleanField(default=False)),
                ('security', models.BooleanField(default=False)),
                ('concierge', models.BooleanField(default=False)),
                ('shared_pool', models.BooleanField(default=False)),
                ('shared_gym', models.BooleanField(default=False)),
                ('shared_KTV', models.BooleanField(default=False)),
                ('shared_lounge', models.BooleanField(default=False)),
                ('air_conditioning', models.BooleanField(default=False)),
                ('baths', models.IntegerField(default=False)),
                ('showers', models.IntegerField(default=False)),
                ('toilets', models.IntegerField(default=False)),
                ('dining_rooms', models.IntegerField(default=False)),
                ('living_room', models.IntegerField(default=False)),
                ('bedrooms', models.IntegerField(default=False)),
                ('kitchen', models.IntegerField(default=False)),
                ('oven', models.BooleanField(default=False)),
                ('fridge', models.BooleanField(default=False)),
                ('dishwasher', models.BooleanField(default=False)),
                ('double_lock', models.BooleanField(default=False)),
                ('balcony', models.BooleanField(default=False)),
                ('floorplan', models.CharField(max_length=100)),
                ('avatar', models.CharField(max_length=100)),
                ('images_array', models.CharField(max_length=100)),
                ('video', models.CharField(max_length=100)),
                ('property_price', models.IntegerField()),
                ('average_increase_last_year', models.IntegerField()),
                ('average_increase_last_three_years', models.IntegerField()),
                ('average_increase_last_five_years', models.IntegerField()),
                ('estimated_rent', models.IntegerField()),
                ('estimated_yield_pct', models.IntegerField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selling_agent', to='property_website.agent')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=15)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=25)),
                ('saved_agents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent_history', to='property_website.agent')),
                ('saved_properties', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_properties', to='property_website.property')),
                ('viewed_properties', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_history', to='property_website.property')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField()),
                ('station_name', models.CharField(max_length=30)),
                ('train_lines', models.CharField(max_length=30)),
                ('nearby_bus_stations', models.CharField(max_length=30)),
                ('nearby_agents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='area_agents', to='property_website.agent')),
                ('nearby_properties', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='area_properties', to='property_website.property')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_id', models.IntegerField()),
                ('school_name', models.CharField(max_length=30)),
                ('school_type', models.CharField(max_length=30)),
                ('train_lines', models.CharField(max_length=30)),
                ('nearby_bus_stations', models.CharField(max_length=30)),
                ('average_property_price', models.IntegerField()),
                ('nearby_agents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_area_agents', to='property_website.agent')),
                ('nearby_properties', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_area_properties', to='property_website.property')),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='nearby_schools',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_area', to='property_website.school'),
        ),
        migrations.AddField(
            model_name='property',
            name='nearby_stations',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='station_area', to='property_website.station'),
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_type', to='property_website.propertytype'),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_id', models.IntegerField()),
                ('city_name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('average_property_price', models.IntegerField()),
                ('nearby_agents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_agencies', to='property_website.agent')),
                ('nearby_properties', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_properties', to='property_website.property')),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_id', models.IntegerField()),
                ('area_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('average_property_price', models.IntegerField()),
                ('nearby_agents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhood_agencies', to='property_website.agent')),
                ('nearby_properties', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhood_properties', to='property_website.property')),
                ('nearby_schools', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhood_schools', to='property_website.school')),
                ('nearby_stations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhood_stations', to='property_website.station')),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='properties',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agencies', to='property_website.property'),
        ),
    ]