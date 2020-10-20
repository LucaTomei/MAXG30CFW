import requests
from bs4 import BeautifulSoup

class Cfw_Builder(object):
	def __init__(self):
		self.requestURL = "https://api.cfw.sh/max"

		self.version = self.default_value_by_param("version")

		self.latest_changelog_date = "21-06-2020"

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
			"No overspeed alarm":"no_overspeed_alarm"
		}

		self.cfw_params_description = {
			"Version": "DRV126 - (Premi Invio)",
			"Max speed": "Velocità massima\n\t- da 20 a 45\n\t[Default: 33]",
			"EU Max speed": "Velocità massima Europa\n\t- da 20 a 45\n\t[Default: 27]",
			"DE Max speed": "Velocità massima Germania\n\t- da 20 a 45\n\t[Default: 22]",
			"Sport battery current": "Controllo della corrente della batteria\n\t- da 10000 a 65000 \n\t[Default: 25000]",
			"Compat patches":"Sono fatti per migliorare il firmware di base. Attualmente consentono di modificare il numero di serie e di utilizzare il selettore di regione riportato di seguito.\n\t- 'on' o 'off'\n\t[Default: 'on']",
			"Firmware region": "Regione Firmware\n\t- 'auto'\n\t- 'us'\n\t- 'de'\n\t- 'eu'\n\t[Default: auto]",
			"KERS Min Speed":"kers_min_speed\n\t- da 0 a 10\n\t[Default: 6]",
			"NO KERS":"Disabilita il freno motore\n\t- 'on' o 'off'\n\t[Default: off]",
			"Error raising level":"Disabilita errori\n\t- 0: Abilita tutti gli errori\n\t- 1: Disabilita warnings\n\t- 2: Disabilita warning batteria modificata\n\t- 3: Nessun Errore\n\t[Default:1]",
			"Boot in":"Avvia in modalità ...\n\t- 3: Ricorda l'ultima modalità\n\t- 2: Sport\n\t- 1: Eco\n\t- 0: Drive\n\t[Default: 3]",
			"Cruise control delay": "Quanti secondi sono necessari per attivare il controllo automatico della velocità\n\t- Da 1 a 10\n\t[Default: 5]",

			"Motor start speed":"Velocità minima in km / h prima dell'avvio del motore.\n\t- Da 0 a 10\n\t[Default: 5]",
			"Direct Power Control": "Controllo diretto della potenza\n\t- Sempre off: 'off'\n\t- Switchable(Register): 'reg'\n\t- Switchable(Brake): 'dyn'\n\t- Sempre On: 'on'\n\t[Default: off]",
			"Direct power control curve":"Influisce sull'accelerazione della corrente.\n\t- 'flat': Molto scattante in erogazione, da tutto subito\n\t- 'quadtaric': Molto più dolce alla partenza e accellerazione esponenziale\n\t[Default: flat]",
			"Coefficient":" Costante di Curva\n\t- Consigliato 120\n\t[Default: 120]",
			"Version spoofing":"Aumenta il numero di versione per impedire gli aggiornamenti DRV dall'app Ninebot.\n\t-'on' o 'off'\n\t[Default: off]",	
			"No overspeed alarm": "Disabilita gli odiosi segnali acustici oltre i 35 km/h.\n\t-'on' o 'off'\n\t[Default:off]"
		}
		
		self.file_name = "%s_" + self.version + ".zip"

		self.check_changelogs()


	def check_changelogs(self):
		siteURL = "https://max.cfw.sh"
		headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B137 Safari/601.1'}
		response = requests.get(url = siteURL, headers = headers)
		content = response.content
		parsed_html = BeautifulSoup(content, "html.parser")
		if self.onPythonista():
			main_li = parsed_html.select('ul > li')[1]
		else:
			main_li = parsed_html.select('ul > li')[2]
		ul = main_li.select('li')[0].get_text(strip=True)
		latest_changelog_date = ul.split(':')[0]
		latest_changelog_changes = ul.split(':')[1]
		if latest_changelog_date != self.latest_changelog_date:
			print("Il %s è stato aggiornato con le seguenti modifiche: %s\n" % (siteURL, latest_changelog_changes)) 
		
		


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
			"no_overspeed_alarm":""
		}
		return cfw_params[param]

	def clean_dict(self, dictionary):
		return {k:v for k,v in dictionary.items() if v != ""}

	def validate_param(self,param_name, param_value):
		if param_name == 'version':	return 'DRV126'
		elif 'speed_normal_kmh' in param_name:
			if param_value.isdigit():
				param_value = int(param_value)
				return param_value if param_value >= 20 and param_value <= 45 else self.default_value_by_param(param_name)
			else:
				return self.default_value_by_param(param_name)

		elif param_name == 'speed_normal_battery':
			if param_value.isdigit():
				param_value = int(param_value)
				return param_value if param_value >= 10000 and param_value <= 65000 else self.default_value_by_param(param_name)
			else:
				return self.default_value_by_param(param_name)

		elif param_name == 'compat_patches':
			return param_value if param_value == 'on' else self.default_value_by_param(param_name)
		elif param_name == 'region':
			return param_value if param_value == 'auto' or param_value == 'us' or param_value == 'de' or param_value == 'eu' else self.default_value_by_param(param_name)

		elif param_name == 'kers_min_speed':
			if param_value.isdigit():
				param_value = int(param_value)
				return param_value if param_value >= 0 and param_value <= 10 else self.default_value_by_param(param_name)
			else:
				return self.default_value_by_param(param_name)

		elif param_name == 'no_kers':
			return param_value if param_value == 'on' else self.default_value_by_param(param_name)

		elif param_name == 'error_raising_level':
			if param_value.isdigit():
				param_value = int(param_value)
				return param_value if param_value >= 0 and param_value <= 3 else self.default_value_by_param(param_name)
			else:
				return self.default_value_by_param(param_name)

		elif param_name == 'boot_workmode':
			if param_value.isdigit():
				param_value = int(param_value)
				return param_value if param_value >= 0 and param_value <= 3 else self.default_value_by_param(param_name)
			else:
				return self.default_value_by_param(param_name)

		elif param_name == 'cruise_control_delay':
			if param_value.isdigit():
				param_value = int(param_value)
				return param_value if param_value >= 0 and param_value <= 10 else self.default_value_by_param(param_name)
			else:
				return self.default_value_by_param(param_name)

		elif param_name == 'motor_start_speed':
			if param_value.isdigit():
				param_value = int(param_value)
				return param_value if param_value >= 0 and param_value <= 10 else self.default_value_by_param(param_name)
			else:
				return self.default_value_by_param(param_name)

		elif param_name == 'direct_power_control':
			return param_value if param_value == 'off' or param_value == 'reg' or param_value == 'dyn' or param_value == 'on' else self.default_value_by_param(param_name)
		
		elif param_name == 'direct_power_control_curve':
			return param_value if param_value == 'flat' or param_value == 'quadtaric' else self.default_value_by_param(param_name)

		# I Don't know this value
		elif param_name == 'direct_power_control_curve_coefficient':
			return self.default_value_by_param(param_name)

		elif param_name == 'version_spoofing':
			return param_value if param_value == 'on' else self.default_value_by_param(param_name)
		
		elif param_name == 'no_overspeed_alarm':
			return param_value if param_value == 'on' else self.default_value_by_param(param_name)

		elif param_name == 'current_raising_coefficient':
			if param_value.isdigit():
				param_value = int(param_value)
				return param_value if param_value >= 100 and param_value <= 2000 else self.default_value_by_param(param_name)
			else:
				return self.default_value_by_param(param_name)
		return param_value

	def cook_firmware(self):
		chosen_params = {}
		for item_name in self.cfw_params_names:
			to_print = "● %s: %s\n" % (item_name, self.description_by_name(item_name))
			print(to_print)
			param_name = self.value_by_name(item_name)

			# Populate args
			this_param = input()
			if this_param != "" and this_param != "\n":
				chosen_params[param_name] = self.validate_param(param_name, this_param)
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

	def shareForIphone(self):
		if self.onPythonista():
			import console
			console.open_in(self.file_name)
		else:
			pass

	def onPythonista(self):
		try: 
			import objc_util
			return True
		except:	return False


if __name__ == '__main__':
	Cfw_BuilderOBJ = Cfw_Builder()
	Cfw_BuilderOBJ.main()
	Cfw_BuilderOBJ.shareForIphone()



