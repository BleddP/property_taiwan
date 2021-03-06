# Generated by Django 3.1.4 on 2021-03-13 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=25)),
                ('line', models.CharField(blank=True, max_length=25)),
                ('whatsapp', models.CharField(blank=True, max_length=25)),
                ('wechat', models.CharField(blank=True, max_length=25)),
                ('skype', models.CharField(blank=True, max_length=25)),
                ('experience', models.IntegerField()),
                ('address_line_1', models.CharField(max_length=30)),
                ('address_line_2', models.CharField(blank=True, max_length=30)),
                ('address_line_3', models.CharField(blank=True, max_length=30)),
                ('postcode', models.CharField(max_length=30)),
                ('latitude', models.CharField(blank=True, max_length=30)),
                ('longitude', models.CharField(blank=True, max_length=30)),
                ('website', models.CharField(blank=True, max_length=30)),
                ('industry_affiliations', models.CharField(blank=True, max_length=30)),
                ('blacklisted', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_id', models.IntegerField()),
                ('area_name', models.CharField(max_length=30)),
                ('latitude', models.CharField(blank=True, max_length=30)),
                ('longitude', models.CharField(blank=True, max_length=30)),
                ('average_property_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_id', models.IntegerField()),
                ('city_name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('average_property_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.BooleanField(default=False)),
                ('property_id', models.CharField(blank=True, max_length=30)),
                ('property_available', models.BooleanField(default=False)),
                ('property_sold', models.BooleanField(default=False)),
                ('property_name', models.CharField(blank=True, max_length=30)),
                ('building_name', models.CharField(blank=True, max_length=30)),
                ('address_line_1', models.CharField(max_length=30)),
                ('address_line_2', models.CharField(blank=True, max_length=30)),
                ('address_line_3', models.CharField(blank=True, max_length=30)),
                ('postcode', models.CharField(max_length=30)),
                ('latitude', models.CharField(max_length=30)),
                ('longitude', models.CharField(max_length=30)),
                ('which_floor', models.IntegerField()),
                ('total_square_m', models.IntegerField()),
                ('total_square_ft', models.IntegerField()),
                ('total_square_ping', models.IntegerField()),
                ('number_of_bedrooms', models.IntegerField()),
                ('number_of_bathrooms', models.IntegerField()),
                ('property_description_short', models.CharField(max_length=500)),
                ('property_description_long', models.CharField(max_length=1500)),
                ('parking_spaces', models.IntegerField()),
                ('parking_type', models.CharField(blank=True, max_length=10)),
                ('property_viewed', models.IntegerField()),
                ('year_built', models.IntegerField()),
                ('year_last_renovated', models.IntegerField(blank=True)),
                ('previous_owners', models.IntegerField()),
                ('developer', models.CharField(blank=True, max_length=50)),
                ('listing_date', models.DateField()),
                ('notes', models.CharField(blank=True, max_length=500)),
                ('key_feature_1', models.CharField(blank=True, max_length=50)),
                ('key_feature_2', models.CharField(blank=True, max_length=50)),
                ('key_feature_3', models.CharField(blank=True, max_length=50)),
                ('key_feature_4', models.CharField(blank=True, max_length=50)),
                ('key_feature_5', models.CharField(blank=True, max_length=50)),
                ('pdf_brochure', models.CharField(blank=True, max_length=50)),
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
                ('washing_machine', models.BooleanField(default=False)),
                ('free_windows', models.BooleanField(default=False)),
                ('internet', models.BooleanField(default=False)),
                ('floorplan', models.CharField(blank=True, max_length=100)),
                ('avatar', models.CharField(blank=True, max_length=100)),
                ('images', models.CharField(blank=True, max_length=100)),
                ('video', models.CharField(blank=True, max_length=100)),
                ('property_price', models.IntegerField()),
                ('average_increase_last_year', models.IntegerField(blank=True, null=True)),
                ('average_increase_last_three_years', models.IntegerField(blank=True, null=True)),
                ('average_increase_last_five_years', models.IntegerField(blank=True, null=True)),
                ('estimated_rent', models.IntegerField(blank=True, null=True)),
                ('estimated_yield_pct', models.IntegerField(blank=True, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selling_agent', to='property_website.agent')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property_website.area')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property_website.city')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type_name', models.CharField(choices=[('Flat', 'Flat'), ('Penthouse', 'Penthouse'), ('Detached House', 'Detached House'), ('Semi-Detached House', 'Semi-Detached House'), ('Terraced House', 'Terraced House')], default='Flat', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(blank=True, max_length=25)),
                ('blacklisted', models.BooleanField(default=False)),
                ('saved_agents', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent_history', to='property_website.agent')),
                ('saved_properties', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saved_properties', to='property_website.property')),
                ('viewed_properties', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='property_history', to='property_website.property')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField()),
                ('station_name', models.CharField(max_length=30)),
                ('latitude', models.CharField(blank=True, max_length=30)),
                ('longitude', models.CharField(blank=True, max_length=30)),
                ('train_lines', models.CharField(max_length=30)),
                ('nearby_bus_stations', models.CharField(max_length=30)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property_website.area')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property_website.city')),
                ('nearby_agents', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_agents', to='property_website.agent')),
                ('nearby_properties', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_properties', to='property_website.property')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_id', models.IntegerField()),
                ('school_name', models.CharField(max_length=30)),
                ('school_type', models.CharField(max_length=30)),
                ('latitude', models.CharField(blank=True, max_length=30)),
                ('longitude', models.CharField(blank=True, max_length=30)),
                ('train_lines', models.CharField(max_length=30)),
                ('nearby_bus_stations', models.CharField(max_length=30)),
                ('average_property_price', models.IntegerField()),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property_website.area')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property_website.city')),
                ('nearby_agents', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school_area_agents', to='property_website.agent')),
                ('nearby_properties', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school_area_properties', to='property_website.property')),
            ],
        ),
        migrations.CreateModel(
            name='RealEstateAgency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(max_length=30)),
                ('address_line_2', models.CharField(blank=True, max_length=30)),
                ('address_line_3', models.CharField(blank=True, max_length=30)),
                ('postcode', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('latitude', models.CharField(blank=True, max_length=30)),
                ('longitude', models.CharField(blank=True, max_length=30)),
                ('website', models.CharField(blank=True, max_length=30)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=30)),
                ('membership_level', models.CharField(choices=[('Standard', 'Standard'), ('Professional', 'Professional'), ('Expert', 'Expert')], default='standard', max_length=30)),
                ('joined_date', models.DateField()),
                ('subscription_expiry', models.DateField()),
                ('blacklisted', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('industry_affiliations', models.CharField(blank=True, max_length=30)),
                ('account_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property_website.accountmanager')),
                ('agents', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property_website.agent')),
                ('properties', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property_website.property')),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='nearby_schools',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school_area', to='property_website.school'),
        ),
        migrations.AddField(
            model_name='property',
            name='nearby_stations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='station_area', to='property_website.station'),
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='property_type', to='property_website.propertytype'),
        ),
        migrations.AddField(
            model_name='city',
            name='agencies',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city_agencies', to='property_website.realestateagency'),
        ),
        migrations.AddField(
            model_name='city',
            name='properties',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city_properties', to='property_website.property'),
        ),
        migrations.AddField(
            model_name='area',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_website.city'),
        ),
        migrations.AddField(
            model_name='area',
            name='nearby_agents',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhood_agencies', to='property_website.agent'),
        ),
        migrations.AddField(
            model_name='area',
            name='nearby_properties',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhood_properties', to='property_website.property'),
        ),
        migrations.AddField(
            model_name='area',
            name='nearby_schools',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhood_schools', to='property_website.school'),
        ),
        migrations.AddField(
            model_name='area',
            name='nearby_stations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhood_stations', to='property_website.station'),
        ),
        migrations.AddField(
            model_name='agent',
            name='agency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_website.realestateagency'),
        ),
        migrations.AddField(
            model_name='agent',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property_website.area'),
        ),
        migrations.AddField(
            model_name='agent',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_website.city'),
        ),
        migrations.AddField(
            model_name='agent',
            name='properties',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agencies', to='property_website.property'),
        ),
    ]
