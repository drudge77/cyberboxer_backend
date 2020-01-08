from import_export import resources
from .models import Organisation

class PersonResource(resources.ModelResource):
    class Meta:
        model = Organisation