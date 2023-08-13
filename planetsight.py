# courtesy of saikuru0

import requests

c_green = '\033[92m'
c_yellow = '\033[93m'
c_red = '\033[91m'
c_purple = '\033[95m'
c_blue = '\033[94m'
c_white = '\033[97m'
c_bold = '\033[1m'
c_reset = '\033[0m'

api_url = "https://ps2.fisu.pw/api/population/?world="
worlds = [
    (1,'Connery'),
	(10,'Miller'),
	(13,'Cobalt'),
	(17,'Emerald'),
	(19,'Jaeger'),
	(40,'SolTech')
]

limits = {
	'low': 10,
	'med': 150
}

ppl_list = []

for world in worlds:
	url = api_url + str(world[0])
	response = requests.get(url)
	
	if response.status_code == 200:
		data = response.json()
		vs = data['result'][0]['vs']
		nc = data['result'][0]['nc']
		tr = data['result'][0]['tr']
		ns = data['result'][0]['ns']
		
		ppl_sum = vs + nc + tr + ns
		
		ppl_list.append({
			'world': world[1],
			'vs': vs,
			'nc': nc,
			'tr': tr,
			'ns': ns,
			'ppl': ppl_sum
		})

sorted_ppl = sorted(ppl_list, key=lambda x: x['ppl'], reverse=True)

print("=" * 50)
for item in sorted_ppl:
	status = c_green if item['ppl'] > limits['med'] else c_yellow if item['ppl'] > limits['low'] else c_red
	print(f"{c_bold}{item['world']}{c_reset}: {status}{item['ppl']}{c_reset} ({c_purple}{item['vs']} VS{c_reset}, {c_blue}{item['nc']} NC{c_reset}, {c_red}{item['tr']} TR{c_reset}, {c_white}{item['ns']} NSO{c_reset})")
print("=" * 50)