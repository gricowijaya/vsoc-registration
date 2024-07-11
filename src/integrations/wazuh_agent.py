import subprocess
import urllib3
import xml.etree.cElementTree as ET
from xml.dom import minidom
from ..utils import exception_handler, beautify_json, get_prefix_config, get_response


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@exception_handler
def set_config(agent_ip: str, manager_address, manager_port):
    prefix = get_prefix_config()["prefix"]

    if not agent_ip:
        raise Exception("Agent IP is required")

    print(f"Writing Configuration File for to {prefix}/ossec.conf")

    client = ET.Element("client")
    enrollment = ET.SubElement(client, "enrollment")

    ET.SubElement(enrollment, "enabled").text = "yes"
    ET.SubElement(enrollment, "manager_address").text = manager_address
    ET.SubElement(enrollment, "port").text = manager_port
    ET.SubElement(enrollment, "agent_name").text = "agent"
    ET.SubElement(enrollment, "groups").text = "API"
    ET.SubElement(enrollment, "agent_address").text = agent_ip
    # ET.SubElement(enrollment, "ssl_cipher").text = "HIGH:!ADH:!EXP:!MD5:!RC4:!3DES:!CAMELLIA:@STRENGTH"
    # ET.SubElement(enrollment, "server_ca_path").text = "/path/to/server_ca"
    # ET.SubElement(enrollment, "agent_certificate_path").text = "/path/to/agent.cert"
    # ET.SubElement(enrollment, "agent_key_path").text = "/path/to/agent.key"
    # ET.SubElement(enrollment, "authorization_pass_path").text = "/path/to/agent.pass"
    # ET.SubElement(enrollment, "auto_method").text = "no"
    ET.SubElement(enrollment, "delay_after_enrollment").text = "20"
    ET.SubElement(enrollment, "use_source_ip").text = "no"

    rough_string = ET.tostring(client, "utf-8")
    reparsed = minidom.parseString(rough_string)
    pretty_xml_as_string = reparsed.toprettyxml(indent="  ")

    # TODO change this to write to the correct path, this is the testing path
    with open(f"ossec.conf", "w") as f:
        f.write(pretty_xml_as_string)

    return f"Agent Config is written in ossec.conf"


@exception_handler
def set_agent_key(agent_key: str):
    prefix = get_prefix_config()
    system_os = prefix["os_info"]["system_os"]
    print (f"Communicate Wazuh Agent with Wazuh Server using on {system_os} ...")

    cmd = f"./scripts/set_agent_key.sh"
    args = agent_key 
    process = subprocess.run([cmd, args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if process.returncode != 0:
        raise Exception("Error in registering agent with key, msg: ", process.stderr)

    return process.returncode

@exception_handler
@beautify_json
def set_agent_to_group(token: str, agent_id: str, group_id: str):
    path = f"/agents/{agent_id}/group/{group_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    agent_groups = get_response("PUT", path, headers)
    return agent_groups

