from django.db import models
from apps.login_app.models import User

class Survey(models.Model):
    user = models.ForeignKey(User, related_name="surveys", on_delete=models.CASCADE)
    anxiety_rating = models.IntegerField()
    lifestyle_rating = models.IntegerField()
    confidence_rating = models.IntegerField()
    happy_rating = models.IntegerField()
    survey_time = models.IntegerField(default=0)
    survey_clicks = models.IntegerField(default=0)
    survey_keypress = models.IntegerField(default=0)
    survey_backspaces = models.IntegerField(default=0)
    quote_replication = models.CharField(max_length=200, default="Knowing how to think empowers you far beyond those who know only what to think.")
