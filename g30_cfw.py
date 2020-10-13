import requests

class Cfw_Builder(object):
	def __init__(self):
		self.requestURL = "https://api.cfw.sh/max"

		self.version = self.default_value_by_param("version")

		self.cfw_params_names = {
			"Version": "version",
			"Max speed": "speed_normal_kmh",
			"EU Max speed": "speed_normal_kmh_eu",
			"DE Max speed": "speed_normal_kmh_de",
			"Sport battery current": "speed_normal_battery",
			"Compat patches":"compat_patches",
			"Firmware region": "region",
			"KERS Min Speed":"kers_min_speed",
			"NO KERS":"no_kers",
			"Error raising level":"error_raising_level",
			"Boot in": "boot_workmode",

			"Cruise control delay": "cruise_control_delay",
			"Motor start speed":"motor_start_speed",
			
			"Direct Power Control": "direct_power_control",
			"Direct power control curve":"direct_power_control_curve",
			"Coefficient":"direct_power_control_curve_coefficient",
			"Version spoofing":"version_spoofing",
			"No overspeed alarm":"no_overspeed_alarm",
			"Current raising coefficient, mA/step":"current_raising_coefficient"
		}

		self.cfw_params_description = {
			"Version": "DRV126 - Premi Invio",
			"Max speed": "Velocità massima -  da 20 a 45\n[Default: 33]",
			"EU Max speed": "Velocità massima Europa -  da 20 a 45\n[Default: 27]",
			"DE Max speed": "Velocità massima Germania -  da 20 a 45\n[Default: 22]",
			"Sport battery current": "Controllo della corrente della batteria - da 10000 a 65000 \n[Default: 25000]",
			"Compat patches":"Sono fatti per migliorare il firmware di base. Attualmente consentono di modificare il numero di serie e di utilizzare il selettore di regione riportato di seguito. - on o off\n[Default: off]",
			"Firmware region": "Regione Firmware - 'auto', 'us', 'de', 'eu'\n[Default: auto]",
			"KERS Min Speed":"kers_min_speed - da 0 a 10\n[default: 6]",
			"NO KERS":"Disabilita il freno motore - on o off\n[Default: off]",
			"Error raising level":"Disabilita errori - 0: Abilita tutti gli errori, 1: Disabilita warnings, 2: Disabilita warning batteria modificata, 3: Nessun Errore\n[Default:1]",
			"Boot in":"Avvia in modalità ... - 3: Ricorda l'ultima modalità, 2: Sport, 1: Eco, 0: Drive\n[Default: 3]",
			"Cruise control delay": "Quanti secondi sono necessari per attivare il controllo automatico della velocità - Da 1 a 10\n[Default: 5]",

			"Motor start speed":"Velocità minima in km / h prima dell'avvio del motore. - Da 0 a 10\n[Default: 5]",
			"Direct Power Control": "Controllo diretto della potenza - Sempre off: off, Switchable(Register): reg, Switchable(Brake): dyn, Sempre On: on\n[Default: off]",
			"Direct power control curve":"Costante della curva. Influisce sull'accelerazione della corrente. Sperimentale! Invece che basato sulla velocità, l'acceleratore funzionerà su un algoritmo basato sulla potenza (come in un veicolo con motore termico). ATTENZIONE: il limite di velocità viene ignorato durante l'utilizzo di DPC. - flat o quadtaric\n[Default: flat]",
			"Coefficient":" Costante di Curva - Consigliato 120\n[Default: 120]",
			"Version spoofing":"Aumenta il numero di versione per impedire gli aggiornamenti DRV dall'app Ninebot. - on o off\n[Default: off]",	
			"No overspeed alarm": "Disabilita gli odiosi segnali acustici oltre i 35 km/h. - on o off\n[Default:off]",
			"Current raising coefficient, mA/step":"Quanto velocemente verrà applicata la corrente. Influisce sulla velocità di aumento - da 100 a 2000\n[Default: 500]"
		}
		
		self.file_name = "%s_" + self.version + ".zip"

	def value_by_name(self, name):
		for item in self.cfw_params_names:
			if item == name:	return self.cfw_params_names[item]

	def description_by_name(self, name):
		for item in self.cfw_params_description:
			if item == name:	return self.cfw_params_description[item]

	def default_value_by_param(self, param):
		cfw_params = {
			"version":"DRV126",
			"output":"zip2",
			"check": "",
			"compat_patches":"on",		
			"region":"auto",
			"version_spoofing":"",	
			"boot_workmode":3,
			"voltage":36,
			"speed_normal_battery":25000,
			"speed_normal_kmh":33,	# da 1 a 45
			"speed_normal_kmh_eu":27,
			"speed_normal_kmh_de":22,
			"direct_power_control":"off",
			"direct_power_control_curve":"flat",
			"direct_power_control_curve_coefficient":"",
			"kers_min_speed":6,
			"motor_start_speed":5,
			"cruise_control_delay":5,
			"error_raising_level":1,
			"no_kers":"",
			"no_overspeed_alarm":"",
			"current_raising_coefficient": 500
		}
		return cfw_params[param]

	def clean_dict(self, dictionary):
		return {k:v for k,v in dictionary.items() if v != ""}


	def cook_firmware(self):
		chosen_params = {}
		for item_name in self.cfw_params_names:
			to_print = "%s: (%s)?\n" % (item_name, self.description_by_name(item_name))
			print(to_print)
			param_name = self.value_by_name(item_name)

			# Populate args
			this_param = input()
			if this_param != "" and this_param != "\n":
				chosen_params[param_name] = this_param
			else:
				chosen_params[param_name] = self.default_value_by_param(param_name)
		
		chosen_params = self.clean_dict(chosen_params)

		response = requests.get(url = self.requestURL, params = chosen_params)
		self.write_zip(response.content)


	def main(self):
		print("Come desideri chiamare questo file?")
		self.file_name = (self.file_name % input()).upper()
		self.cook_firmware()

	def write_zip(self, content):
		file = open(self.file_name, "wb")
		file.write(content)
		file.close()

if __name__ == '__main__':
	Cfw_BuilderOBJ = Cfw_Builder()
	Cfw_BuilderOBJ.main()