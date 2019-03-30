from django.db import models

class RedditPost(models.Model):
    post_id = models.CharField(unique=True, max_length=6, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    karma = models.IntegerField(blank=True, null=True)
    subreddit = models.CharField(max_length=500, blank=True, null=True)
    submission_link_url = models.CharField(max_length=1000, blank=True, null=True)
    submission_url = models.CharField(max_length=1000, blank=True, null=True)
    date_time = models.CharField(max_length=100, blank=True, null=True)
    collected_date = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        db_table = 'reddit_posts'

class test(models.Model):
    body = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'test'


# Create your models here.
class Report(models.Model):
    timestamp_sutc = models.FloatField()
    timestamp_local = models.FloatField()
    eta_utc = models.FloatField()
    eta_local = models.FloatField()
    state = models.FloatField()
    event = models.FloatField()
    captain = models.FloatField()
    chief_engineer = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    period = models.FloatField()
    sailing_time = models.FloatField()
    total_running_hours_me = models.FloatField()
    heading = models.FloatField()
    course_made_good = models.FloatField()
    speed_over_ground = models.FloatField()
    speed_through_water = models.FloatField()
    distance_over_ground = models.FloatField()
    distance_through_water = models.FloatField()
    water_depth = models.FloatField()
    water_depth_below_keel = models.FloatField()
    draft_forward = models.FloatField()
    draft_aft = models.FloatField()
    mean_draft = models.FloatField()
    trim = models.FloatField()
    air_temp = models.FloatField()
    air_temp_weather_provider = models.FloatField()
    engine_room_temp = models.FloatField()
    cooling_water_temp_lt = models.FloatField()
    air_press = models.FloatField()
    air_press_weather_provider = models.FloatField()
    sea_water_temp = models.FloatField()
    sea_water_temp_weather_provider = models.FloatField()
    sea_state = models.FloatField()
    douglas_sea_scale = models.FloatField()
    wind_speed_true = models.FloatField()
    wind_speed_true_weather_provider = models.FloatField()
    wind_speed_rel = models.FloatField()
    wind_direction_true = models.FloatField()
    wind_direction_true_weather_provider = models.FloatField()
    wind_direction_rel = models.FloatField()
    wave_height = models.FloatField()
    wave_height_weather_provider = models.FloatField()
    wave_direction = models.FloatField()
    swell_height = models.FloatField()
    swell_height_weather_provider = models.FloatField()
    swell_direction = models.FloatField()
    swell_direction_weather_provider = models.FloatField()
    swell_period_weather_provider = models.FloatField()
    visibility_weather_provider = models.FloatField()
    cargo_weight = models.FloatField()
    cargo_teu_full = models.FloatField()
    cargo_teu_empty = models.FloatField()
    cargo_reefers = models.FloatField()
    cargo_volume = models.FloatField()
    cargo_passengers = models.FloatField()
    ballast_weight = models.FloatField()
    avg_shaft_rpm = models.FloatField()
    avg_slip = models.FloatField()
    total_foc = models.FloatField()
    total_foc_iso = models.FloatField()
    total_foc_me = models.FloatField()
    total_foc_me_iso = models.FloatField()
    total_foc_ae = models.FloatField()
    total_foc_ae_iso = models.FloatField()
    total_foc_ab = models.FloatField()
    total_foc_ab_iso = models.FloatField()
    total_foc_igs = models.FloatField()
    total_foc_igs_iso = models.FloatField()
    total_foc_inc = models.FloatField()
    total_foc_inc_iso = models.FloatField()
    total_foc_hfo = models.FloatField()
    total_foc_hfo_hs = models.FloatField()
    total_foc_hfo_ls = models.FloatField()
    total_foc_hfo_lls = models.FloatField()
    total_foc_lfo = models.FloatField()
    total_foc_mdo = models.FloatField()
    total_foc_mgo = models.FloatField()
    total_foc_propane = models.FloatField()
    total_foc_butane = models.FloatField()
    total_foc_lng = models.FloatField()
    total_foc_methanol = models.FloatField()
    total_foc_ethanol = models.FloatField()
    total_foc_undef = models.FloatField()
    total_sfoc_me = models.FloatField()
    total_sfoc_ae = models.FloatField()
    total_sfoc_me_iso = models.FloatField()
    total_sfoc_ae_iso = models.FloatField()
    total_co2 = models.FloatField()
    total_co2_me = models.FloatField()
    total_co2_ae = models.FloatField()
    total_co2_ab = models.FloatField()
    total_co2_igs = models.FloatField()
    total_co2_inc = models.FloatField()
    total_co2_undef = models.FloatField()
    total_power_me_avg = models.FloatField()
    total_power_ae_avg = models.FloatField()
    total_generated_energy_me = models.FloatField()
    total_generated_energy_ae = models.FloatField()
    total_generated_electrical_energy = models.FloatField()
    total_generated_shaft_energy = models.FloatField()
    total_shaft_power_avg = models.FloatField()
    total_shaft_power_corrected_avg = models.FloatField()
    total_electrical_power_avg = models.FloatField()
    me_load_avg = models.FloatField()
    ae_load_avg = models.FloatField()
    delivered_power_corrected = models.FloatField()
    eeoi_weight = models.FloatField()
    eeoi_teu = models.FloatField()
    power_added_or_reduced_by_wind = models.FloatField()
    speed_loss = models.FloatField()
    speed_loss_uncorrected = models.FloatField()
    total_fuel_oil_rob = models.FloatField()
    total_fresh_water_rob = models.FloatField()
    fuel_oil_hfo_rob = models.FloatField()
    fuel_oil_hfo_hs_rob = models.FloatField()
    fuel_oil_hfo_ls_rob = models.FloatField()
    fuel_oil_hfo_lls_rob = models.FloatField()
    fuel_oil_lfo_rob = models.FloatField()
    fuel_oil_mdo_rob = models.FloatField()
    fuel_oil_mgo_rob = models.FloatField()
    fuel_oil_propane_rob = models.FloatField()
    fuel_oil_butane_rob = models.FloatField()
    fuel_oil_lng_rob = models.FloatField()
    fuel_oil_methanol_rob = models.FloatField()
    fuel_oil_ethanol_rob = models.FloatField()
    circulation_lub_oil_me_rob = models.FloatField()
    circulation_lub_oil_ae_rob = models.FloatField()
    circulation_lub_oil_undef_rob = models.FloatField()
    total_circulation_lub_oil_rob = models.FloatField()
    cylinder_lub_oil_rob = models.FloatField()
    cylinder_hs_lub_oil_rob = models.FloatField()
    cylinder_ls_lub_oil_rob = models.FloatField()
    undefined_lub_oil_rob = models.FloatField()
    fresh_water_drinking_rob = models.FloatField()
    fresh_water_boiler_rob = models.FloatField()
    fresh_water_undefined_rob = models.FloatField()
    total_fuel_oil_bunkered = models.FloatField()
    fuel_oil_hfo_bunkered = models.FloatField()
    fuel_oil_hfo_hs_bunkered = models.FloatField()
    fuel_oil_hfo_ls_bunkered = models.FloatField()
    fuel_oil_hfo_lls_bunkered = models.FloatField()
    fuel_oil_lfo_bunkered = models.FloatField()
    fuel_oil_mdo_bunkered = models.FloatField()
    fuel_oil_mgo_bunkered = models.FloatField()
    fuel_oil_propane_bunkered = models.FloatField()
    fuel_oil_butane_bunkered = models.FloatField()
    fuel_oil_lng_bunkered = models.FloatField()
    fuel_oil_methanol_bunkered = models.FloatField()
    fuel_oil_ethanol_bunkered = models.FloatField()
    circulation_lub_oil_me_bunkered = models.FloatField()
    circulation_lub_oil_ae_bunkered = models.FloatField()
    circulation_lub_oil_undef_bunkered = models.FloatField()
    total_circulation_lub_oil_bunkered = models.FloatField()
    cylinder_lub_oil_bunkered = models.FloatField()
    cylinder_hs_lub_oil_bunkered = models.FloatField()
    cylinder_ls_lub_oil_bunkered = models.FloatField()
    undefined_lub_oil_bunkered = models.FloatField()
    total_fuel_oil_gain_loss = models.FloatField()
    fuel_oil_hfo_gain_loss = models.FloatField()
    fuel_oil_hfo_hs_gain_loss = models.FloatField()
    fuel_oil_hfo_ls_gain_loss = models.FloatField()
    fuel_oil_hfo_lls_gain_loss = models.FloatField()
    fuel_oil_lfo_gain_loss = models.FloatField()
    fuel_oil_mdo_gain_loss = models.FloatField()
    fuel_oil_mgo_gain_loss = models.FloatField()
    fuel_oil_propane_gain_loss = models.FloatField()
    fuel_oil_butane_gain_loss = models.FloatField()
    fuel_oil_lng_gain_loss = models.FloatField()
    fuel_oil_methanol_gain_loss = models.FloatField()
    fuel_oil_ethanol_gain_loss = models.FloatField()
    circulation_lub_oil_me_gain_loss = models.FloatField()
    circulation_lub_oil_ae_gain_loss = models.FloatField()
    circulation_lub_oil_undef_gain_loss = models.FloatField()
    total_circulation_lub_oil_gain_loss = models.FloatField()
    cylinder_lub_oil_gain_loss = models.FloatField()
    cylinder_hs_lub_oil_gain_loss = models.FloatField()
    cylinder_ls_lub_oil_gain_loss = models.FloatField()
    undefined_lub_oil_gain_loss = models.FloatField()
    total_cylinder_lub_oil_consumption = models.FloatField()
    total_cylinder_hs_lub_oil_consumption = models.FloatField()
    total_cylinder_ls_lub_oil_consumption = models.FloatField()
    total_circulation_lub_oil_consumption_me = models.FloatField()
    total_circulation_lub_oil_consumption_ae = models.FloatField()
    total_fresh_water_consumption_undefined = models.FloatField()
    total_fresh_water_consumption_domestic = models.FloatField()
    total_fresh_water_consumption_boiler = models.FloatField()
    total_fresh_water_consumption_washing = models.FloatField()
    total_oily_water_discharge_undefined = models.FloatField()
    total_oily_water_discharge_via_ows = models.FloatField()
    total_oily_water_discharge_via_odme = models.FloatField()
    estimation_score = models.FloatField()
    completeness_score = models.FloatField()
    plausibility_score = models.FloatField()
    
    class Meta:
        db_table = 'reports'