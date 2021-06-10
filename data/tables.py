import django_tables2 as tables
from .models import Data

class DataTable(tables.Table):
		class Meta:
				model = Data
				template_name = "django_tables2/bootstrap.html"
				fields = ("day", "temperature", )
