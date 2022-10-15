from django.db import models

# Create your models here.
class Finishing_Pieces(models.Model):
    ANSWER_YES = "Y"
    ANSWER_NO  =  "N"

    ANSWER = [
        (ANSWER_YES, "Yes"),
        (ANSWER_NO, "No")
    ]
    specification_check_on_defects = models.CharField(max_length = 1,choices = ANSWER,default=ANSWER_NO)
    Quality_of_labeling = models.CharField(max_length = 1,choices = ANSWER,default=ANSWER_NO)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_stamp)
    