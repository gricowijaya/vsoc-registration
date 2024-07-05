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
		address = (manager_ip, int(manager_port))
		s.connect(address)
		ip = s.getsockname()[0]
		s.close()
		data = {"hostname": name, "ip": ip}
	except socket.gaierror:
		data = {"hostname": name, "ip": ""}

	return data

