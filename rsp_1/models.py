from django.db import models

# Create your models here.

class Double_run_institution_woodin(models.Model):

    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    drying_temperature = models.CharField(max_length = 1, default=ANSWER_NO, choices = ANSWER)
    speed = models.CharField(max_length = 1, default=ANSWER_NO, choices = ANSWER)
    cloth_width = models.CharField(max_length = 1, default=ANSWER_NO, choices = ANSWER)
    beam_position = models.CharField(max_length = 1, default=ANSWER_NO, choices = ANSWER)
    lattice_roller = models.CharField(max_length = 1, default=ANSWER_NO, choices = ANSWER)
    vision_system = models.CharField(max_length = 1, default=ANSWER_NO, choices = ANSWER)
    colour_pumps = models.CharField(max_length = 1, default=ANSWER_NO, choices = ANSWER)
    check_fitting = models.CharField(max_length = 1, default=ANSWER_NO, choices = ANSWER)
    penetration = models.CharField(max_length = 1, default=ANSWER_NO, choices = ANSWER)
    colour_marking_off = models.CharField(max_length = 1, default=ANSWER_NO, choices = ANSWER)
    other_defects = models.CharField(max_length = 1, default=ANSWER_NO, choices = ANSWER)
    time_stamp_curr = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp_curr)
    
