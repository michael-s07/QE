from pyexpat import model
from django.db import models

# Create your models here.
class Adepa_Base_Nustyle_Safoa (models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    drying_temperature = models.CharField(max_length = 1, choices = ANSWER,default=ANSWER_NO)
    speed = models.CharField(max_length = 1, choices = ANSWER,default=ANSWER_NO)
    base_colour_misfit = models.CharField(max_length = 1, choices = ANSWER,default=ANSWER_NO)
    selvedge_effect = models.CharField(max_length = 1, choices = ANSWER,default=ANSWER_NO)
    white_patches = models.CharField(max_length = 1, choices = ANSWER,default=ANSWER_NO)
    color_marking_off = models.CharField(max_length = 1, choices = ANSWER,default=ANSWER_NO)
    other_defect = models.CharField(max_length = 1, choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

class Steamer(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    temperature =  models.CharField(max_length = 1, choices = ANSWER,default=ANSWER_NO)
    speed = models.CharField(max_length = 1, choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

class OWS(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    temperatures_washing = models.CharField(max_length = 1, choices = ANSWER,default=ANSWER_NO)
    units_squeezing_pressures = models.CharField(max_length = 1, choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)