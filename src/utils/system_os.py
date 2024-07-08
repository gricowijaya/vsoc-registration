import platform
from . import exception_handler

@exception_handler
def get_system_os():
    system_os = platform.system()
    system_architecture = platform.architecture()
    system_info = { "system_os": system_os, "system_architecture": system_architecture}
    return system_info

@exception_handler
def get_prefix_config():
    os_info = get_system_os()
    system_os = os_info["system_os"]
    prefixes = { 
        "Linux": "/var/ossec/etc",
        "Darwin": "/Library/Ossec/etc",
        "Windows": "C:\\Program Files (x86)\\ossec-agent",
    }

    prefix = prefixes.get(system_os)

    if not prefix:
        raise Exception(f"Unsupported OS: {system_os}")

    return {"prefix": prefix, "os_info": os_info}

