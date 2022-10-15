from django.db import models

# Create your models here.
class Woodin_institution(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    drying_temperature = models.CharField(max_length = 1, choices = ANSWER,default=ANSWER_NO)
    speed = models.CharField(max_length = 1, choices = ANSWER,default=ANSWER_NO)
    cloth_width_total = models.CharField(max_length = 1, choices = ANSWER,default=ANSWER_NO)
    check_on_fitting = models.CharField(max_length = 1, choices = ANSWER,default=ANSWER_NO)
    penetration = models.CharField(max_length = 1, choices = ANSWER,default=ANSWER_NO)
    colour_marking_off = models.CharField(max_length = 1, choices = ANSWER,default=ANSWER_NO)
    printing_folds = models.CharField(max_length = 1, choices = ANSWER,default=ANSWER_NO)
    other_defects = models.CharField(max_length = 1, choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)
    