import xmltodict
import json
import sys
from device import Device

def show_intf_mgmt(sw):

	getdata = sw.show('show interface mgmt0')

	print getdata

	show_intf_dict = xmltodict.parse(getdata[1])

	data = show_intf_dict['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']

	ip = data['eth_ip_addr']
	mask = data['eth_ip_mask']
	name = data['interface']
	speed = data['eth_speed']
	duplex = data['eth_duplex']

	mgmt_dict = {'ip_addr': ip + '/'+mask, 'name':name, 'speed':speed, 'duplex':duplex}

	#print json.dumps(mgmt_dict, indent = 4)

	return mgmt_dict

def show_hardware(sw):

	getdata = sw.show('show hardware')

	show_hw_dict = xmltodict.parse(getdata[1])
	data = show_hw_dict['ins_api']['outputs']['output']['body']

	hw_dict = {}
	hw_dict['os_version'] = data['kickstart_ver_str']
	hw_dict['type'] = data['chassis_id']
	hw_dict['memory'] = data['memory'] + data['mem_type']
	hw_dict['hostname'] = data['host_name']
	hw_dict['bootflash'] = data['bootflash_size']
	hw_dict['last_boot_reason'] = data['rr_reason']
	hw_dict['uptime'] = '{} days(s) {} hour(s) {} mins(s) {} sec(s)'.format(data['kern_uptm_days'],\
						data['kern_uptm_hrs'], data['kern_uptm_mins'], data['kern_uptm_secs'])

	ser_nums = {}
	ser_nums_data = show_hw_dict['ins_api']['outputs']['output']['body']['TABLE_slot'] \
		['ROW_slot']['TABLE_slot_info']['ROW_slot_info']

	for each in ser_nums_data:

		if 'serial_num' in each.keys():
			key = each['serial_num']
			ser_nums[key] = each['model_num']

	hw_dict['serial_numbers'] = ser_nums

	#print json.dumps(hw_dict, indent = 4)

	return hw_dict

def main():

	switch = Device(ip='172.31.217.142', username='admin', password='cisco123')
	switch.open()

	facts = {}

	intf = show_intf_mgmt(switch)
	facts['mgmt_intf'] = intf
	facts.update(intf)

	args = sys.argv

	hw = show_hardware(switch)
	facts.update(hw)

	if len(args) == 1:
		print json.dumps(facts,indent = 4)
	else:
		if args[1] in facts.keys():
			print args[1].upper() + ': ' + json.dumps(facts[args[1]], indent = 4)
		else:
			print 'Invalid Key. Try again'


if __name__ == "__main__":
	main()