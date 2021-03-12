# Generated by Django 3.1.4 on 2021-03-12 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property_website', '0003_auto_20210312_0852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='country',
        ),
        migrations.RemoveField(
            model_name='property',
            name='images_array',
        ),
        migrations.AddField(
            model_name='property',
            name='property_sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='propertytype',
            name='property_type_name',
            field=models.CharField(choices=[('Flat', 'Flat'), ('Penthouse', 'Penthouse'), ('Detached House', 'Detached House'), ('Semi-Detached House', 'Semi-Detached House'), ('Terraced House', 'Terraced House')], default='Flat', max_length=30),
        ),
        migrations.AddField(
            model_name='station',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property_website.city'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='agent',
            name='address_line_3',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='agent',
            name='industry_affiliations',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='agent',
            name='latitude',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='agent',
            name='line',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='agent',
            name='longitude',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='agent',
            name='skype',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='agent',
            name='website',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='agent',
            name='wechat',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='agent',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='property',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='property',
            name='address_line_3',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='property',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property_website.area'),
        ),
        migrations.AlterField(
            model_name='property',
            name='avatar',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='property',
            name='average_increase_last_five_years',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='average_increase_last_three_years',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='average_increase_last_year',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='building_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property_website.city'),
        ),
        migrations.AlterField(
            model_name='property',
            name='developer',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='estimated_rent',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='estimated_yield_pct',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='floorplan',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='property',
            name='images',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='property',
            name='key_feature_1',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='key_feature_2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='key_feature_3',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='key_feature_4',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='key_feature_5',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='notes',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='property',
            name='parking_type',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='pdf_brochure',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_id',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='property',
            name='video',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='property',
            name='year_last_renovated',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]