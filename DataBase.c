#include <stdio.h>
#include <curl/curl.h>
#include <stdlib.h>
#include <time.h>

#define SAMPLE_LEN 2928
int main(void) {

  time_t t;
  int temperatura;
  int pressio;
  int pluja;
  int humitat_aire;
  int velocitat_vent;
  char direccions[2];
  int direccio_vent;
  int minut = 0;
  int hora = 0;
  int dia = 1;
  int mes = 5;
  char fecha[16];

	
	srand((unsigned) time(&t));
	
	void check_data(){	
		if (minut == 60){
				minut = 0;
				hora = hora + 1;
				if (hora == 24){
				  hora = 0;
				  dia = dia + 1;
				  if (dia == 32){
				    dia = 1;
				    mes = mes + 1;
				  }
				}
			}
		sprintf(fecha, "2021-%i-%iT%i:%i", mes, dia, hora, minut);
	}
	
	void adjust_temperatura(){
		if (hora > 11 && hora < 20){
    	temperatura = rand() % 15 + 14;
  	}
  	else {
    	temperatura = rand() % 12 + 6;
  	}
	}
	
	void adjust_pluja(){
	pluja = rand() % 101;
		if (pluja < 50) pluja = 0;
		else if (pluja < 55) pluja = 1;
		else if (pluja < 60) pluja = 2;
		else if (pluja < 65) pluja = 3;
		else if (pluja < 70) pluja = 4;
		else if (pluja < 75) pluja = 5;
		else if (pluja < 80) pluja = 6;
		else if (pluja < 85) pluja = 7;
		else if (pluja < 90) pluja = 8;
		else if (pluja < 95) pluja = 9;
		else if (pluja < 100) pluja = 10;
	}
	
	void adjust_pressio(){
		if (pluja != 0) pressio = rand() % 2801 + 98500;
		else pressio = rand() % 2801 + 101301;
	}
	
	void adjust_humitatAire(){
		if (pressio < 101300) humitat_aire = rand() % 38 + 60;
  	else humitat_aire = rand() % 30 + 40;
	}
	
	void adjust_direccioVent(){
		direccio_vent = rand() % 8;
		switch (direccio_vent){
			case 0:
				direccions[0] = 'N';
			break;
			
			case 1:
				direccions[0] = 'S';
			break;
			
			case 2:
				direccions[0] = 'E';
			break;
			
			case 3:
				direccions[0] = 'O';
			break;
			
			case 4:
				direccions[0] = 'N';
				direccions[1] = 'E';
			break;
			
			case 5:
				direccions[0] = 'N';
				direccions[1] = 'O';
			break;
			
			case 6:
				direccions[0] = 'S';
				direccions[1] = 'E';
			break;
			
			case 7:
				direccions[0] = 'S';
				direccions[1] = 'O';
			break;
		}
		printf("Direccions: %s", direccions);
	}

  void send_json(){
		CURL *curl;
		CURLcode res;
		curl = curl_easy_init();
		if(curl) {
			curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, "POST");
			curl_easy_setopt(curl, CURLOPT_URL, "http://http://localhost:8000/api/updatedades/");
			curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
			curl_easy_setopt(curl, CURLOPT_DEFAULT_PROTOCOL, "https");
			struct curl_slist *headers = NULL;
			headers = curl_slist_append(headers, "Content-Type: application/json");
			curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
			char *data;
			sprintf(data, "{\r\n  \"ID_Arduino\": \"01000001\",\r\n  \"day\": \"%s\",\r\n  \"temperature\": \"%i\",\r\n  \"press\": \"%i\",\r\n  \"rain\": \"%i\",\r\n  \"air_humidity\": \"%i\",\r\n \"wind_speed\": \"%i\",\r\n  \"wind_direction\": \"%s\"\r\n}\r\n", fecha, temperatura, pressio, pluja, humitat_aire, velocitat_vent, direccions);
			printf(data);
			curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);
			res = curl_easy_perform(curl);
		}
		curl_easy_cleanup(curl);
  }
	
	for(int i = 0; i < SAMPLE_LEN; i++){
		printf("Entra al for");
		check_data();
		minut+=30;
		
		adjust_temperatura();
		adjust_pluja();
		adjust_pressio();
		adjust_humitatAire();
		adjust_direccioVent();
		
		velocitat_vent = rand() % 24 + 2;
		
		send_json();
		}		
	}
