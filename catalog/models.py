from django.db.models import Model, CharField, TextField
from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
import json


class Mineral(Model):
    name = CharField(max_length=255)
    caption = TextField()
    img = CharField(max_length=255)
    fields = TextField(blank=True, null=True)

    @property
    def fields_dict(self):
        return json.loads(self.fields)