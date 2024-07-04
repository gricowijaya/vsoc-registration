import socket
from .exception import exception_handler
from .output import beautify_json

@exception_handler
@beautify_json
def get_agent_ip_hostname(manager_ip: int, manager_port: int):
	try:
		name = socket.gethostname()
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect((str(manager_ip), manager_port))
		ip = s.getsockname()[0]
		s.close()
		data = {"hostname": name, "ip": ip}
	except socket.gaierror:
		data = {"hostname": name, "ip": ""}

	return data

