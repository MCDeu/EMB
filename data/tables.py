import django_tables2 as tables
from .models import Data

class DataTable(tables.Table):
		class Meta:
				model = Data
				template_name = "django_tables2/bootstrap.html"
				fields = ("id_station", "day", "temperature", "press", "rain", "air_humidity", "wind_speed" , "wind_direction")
