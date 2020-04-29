from django.db import models
import json, decimal

class NautTemp(models.Model):
    class Meta:
        db_table = "naut_temp"

    naut_id     = models.IntegerField(primary_key = True)
    name        = models.CharField(max_length = 32)
    amount      = models.DecimalField(max_digits = 18, decimal_places = 3)

class NautilusEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, NautTemp):
            model = {}
            for prop in vars(obj):
                if not prop.startswith("_"):
                    model[prop] = getattr(obj, prop)
            return model
        elif (isinstance(obj, decimal.Decimal)):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)

