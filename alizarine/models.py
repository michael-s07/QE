from django.db import models

# Create your models here.
class Soaper_1(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    water_flow_comp_1 = models.CharField(max_length = 1, choices = ANSWER, default=ANSWER_NO)
    water_temperatures_comp_1 = models.CharField(max_length = 1, choices = ANSWER, default=ANSWER_NO)
    water_exit_comp_1 = models.CharField(max_length = 1, choices = ANSWER, default=ANSWER_NO)
    water_flow_comp_2 = models.CharField(max_length = 1, choices = ANSWER, default=ANSWER_NO)
    water_temperatures_comp_2 = models.CharField(max_length = 1, choices = ANSWER, default=ANSWER_NO)
    water_flow_comp_3 = models.CharField(max_length = 1, choices = ANSWER, default=ANSWER_NO)
    water_temperatures_comp_3 = models.CharField(max_length = 1, choices = ANSWER, default=ANSWER_NO)
    staining = models.CharField(max_length = 1, choices = ANSWER, default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)

class Soaper_2(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    water_flow_comp_1 = models.CharField(max_length = 1, choices = ANSWER, default=ANSWER_NO)
    water_temperatures_comp_1 = models.CharField(max_length = 1, choices = ANSWER, default=ANSWER_NO)
    water_exit_comp_1 = models.CharField(max_length = 1, choices = ANSWER, default=ANSWER_NO)
    water_flow_comp_2 = models.CharField(max_length = 1, choices = ANSWER, default=ANSWER_NO)
    water_temperatures_comp_2 = models.CharField(max_length = 1, choices = ANSWER, default=ANSWER_NO)
    water_flow_comp_3 = models.CharField(max_length = 1, choices = ANSWER, default=ANSWER_NO)
    water_temperatures_comp_3 = models.CharField(max_length = 1, choices = ANSWER, default=ANSWER_NO)
    staining = models.CharField(max_length = 1, choices = ANSWER, default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)

class Soaper_4(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    staining = models.CharField(max_length = 1, choices = ANSWER, default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)

class Plain_Dyeing(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    beam_absorption = models.CharField(max_length = 1, choices = ANSWER, default=ANSWER_NO)
    other_defects = models.CharField(max_length = 1, choices = ANSWER, default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)
