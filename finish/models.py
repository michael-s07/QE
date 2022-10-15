from django.db import models

# Create your models here.
class Stenter_5(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    straightness_of_design = models.CharField(max_length = 1,choices = ANSWER,default=ANSWER_NO)
    straightness_of_fibre = models.CharField(max_length = 1,choices = ANSWER,default=ANSWER_NO)
    moisture_outfeed_cloth_with = models.CharField(max_length = 1,choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)

class Stenter_7(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    straightness_of_design = models.CharField(max_length = 1,choices = ANSWER,default=ANSWER_NO)
    straightness_of_fibre = models.CharField(max_length = 1,choices = ANSWER,default=ANSWER_NO)
    moisture_outfeed_cloth_with = models.CharField(max_length = 1,choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)

class Calender(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    eveness_of_shiny_effect = models.CharField(max_length = 1,choices = ANSWER,default=ANSWER_NO)
    temperature = models.CharField(max_length = 1,choices = ANSWER,default=ANSWER_NO)
    speed_fancy_woodin_dumas = models.CharField(max_length = 1,choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)

class Baking_Oven(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    loop = models.CharField(max_length = 1,choices = ANSWER,default=ANSWER_NO)
    spread = models.CharField(max_length = 1,choices = ANSWER,default=ANSWER_NO)
    residence_time = models.CharField(max_length = 1,choices = ANSWER,default=ANSWER_NO)
    temperature = models.CharField(max_length = 1,choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)
    