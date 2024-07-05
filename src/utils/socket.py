import socket
from .exception import exception_handler
from .output import beautify_json

@exception_handler
@beautify_json
def get_agent_ip_hostname(manager_ip: str, manager_port: str):
	try:
		name = socket.gethostname()
		print(name)
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		print(f'12, {__name__} The manager ip is {manager_ip} with type of {type(manager_ip)}')
		print(f'13, {__name__}The manager port is {manager_port} with type of {type(manager_port)}')
		print(f'15, {__name__} The manager ip is {manager_ip} with type of {type(manager_ip)}')
		manager_port = int(manager_port)
		print(f'16, {__name__}The manager port is {manager_port} with type of {type(manager_port)}')
		s.connect(manager_ip, manager_port)
		ip = s.getsockname()[0]
		s.close()
		data = {"hostname": name, "ip": ip}
	except socket.gaierror:
		data = {"hostname": name, "ip": ""}

	return data

