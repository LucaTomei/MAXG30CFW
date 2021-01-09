import requests
from datetime import datetime

url = "https://api.cfw.sh/max"


params = {
    'version': 'DRV126',
    "compat_patches": "on",
    "region": "auto",
    "version_spoofing": "on",
    "boot_workmode": "2",   # Sport
    "speed_normal_battery": "33000",
    "speed_normal_kmh": "26",
    "speed_normal_kmh_eu": "26",
    "speed_normal_kmh_de": "26",
    #"no_kers": "on",   # se non volessi il kers
    "patch_all": "on",
    "direct_power_control": "dyn",  # con freno
    "direct_power_control_curve": "quadratic",
    "current_raising_coefficient": "1800",
    "motor_start_speed": "2",
    "brake_limit": "120",
    "brake_i_min": "6000",
    "brake_i_max": "35000",
    "kers_min_speed": "6",
    "brake_current_raising_coefficient": "500",
    "brake_light_mode": "stock",
    "brake_light_flash_frequency": "235",
    "cruise_control_delay": "3",
    "error_raising_level": "0",
    "no_overspeed_alarm": "on", # da tutti gli errori
    "stay_on_locked": "on",
    "wheel_size": "10.0",
    "showbatt": "on"       # per mostrare la percentuale batteria
}

params_dragster  = {
	'version': 'DRV126',
    "compat_patches": "on",
    "region": "auto",
    "boot_workmode": "3",
    "speed_normal_battery": "38000",
    "speed_normal_kmh": "45",
    "speed_normal_kmh_eu": "45",
    "speed_normal_kmh_de": "45",
    "patch_all": "on",
    "direct_power_control": "on",
    "direct_power_control_curve": "quadratic",
    "current_raising_coefficient": "2200",
    "motor_start_speed": "2",
    "brake_limit": "120",
    "brake_i_min": "6000",
    "brake_i_max": "35000",
    "kers_min_speed": "6",
    "no_kers": "on",
    "brake_current_raising_coefficient": "500",
    "brake_light_mode": "stock",
    "brake_light_flash_frequency": "235",
    "cruise_control_delay": "3",
    "error_raising_level": "1",
    "no_overspeed_alarm": "on",
    "wheel_size": "10.0"
}


if __name__ == '__main__':
	response = requests.get(url = url, params = params)
	
	filename = "files/G30_%s.zip" %(datetime.now().strftime("%Y-%m-%d_at_%H-%m"))
	file = open(filename, "wb")
	file.write(response.content)
	file.close()


