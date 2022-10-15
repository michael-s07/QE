from django.db import models

# Create your models here.
class Singeing(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    flame_distribution = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    colour_of_flame = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    speed = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)


class Desizing_mangle(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    temperature = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    impregnation = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)

class Washing_Machine_1(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    temperature = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    fresh_water_flow = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    starch_test = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)

class Saturator_1_NaOH(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    squeezing_mangle_pressure = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    level = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    density_and_circulation = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    end_point_NaOH = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)

class J_Box_1_Scouring(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    loading_speed = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    volume_of_cloth_in_j_box = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    flow_from_overflow_pipe = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    temperature_and_stream_flow = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)

class Washing_Machine_2(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    temperature = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    fresh_water_flow = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)

class Saturator_2_H2O2(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    level = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    end_point_H2O2 = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    squeezing_mangle_pressure = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)

class J_Box_2_Bleaching(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    volume_of_cloth_in_j_box = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    flow_from_overflow_pipe = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)

class Washing_Machine_3(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    temperature = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    fresh_water_flow = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)

class Merceriser(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    rectofact_performance = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    fibre_deviation = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    folded_selvedge_at_in_the_feed_impregnation_mangle = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    strong_caustic_concentration = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    check_on_in_feed_or_chain_clips = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    flow_on_spraying_units = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    pressure_suction_units_1_to_6 =  models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    water_flow_from_washing_units_to_lagoon = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    lagoon_temperature =  models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    water_flow_to_washing_units = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    week_caustic_concentration = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    final_width_of_mercerised_cloth = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    caustic_check_Phenolphthalein_drop = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)

class Stenter_6(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    Rectofact_performance = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    fibre_deviation = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    impregnation_temperature = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    check_on_in_feed_clips = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    drying_temperature_6_chambers = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    end_moisture = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    width_of_beam = models.CharField(max_length=1,choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)
    

