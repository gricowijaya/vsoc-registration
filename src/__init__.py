from .integrations import (auth, 
						   get_checkhealth, 
						   get_list_agent, 
						   get_summary_agents_os, 
						   get_summary_agents_status,
						   set_register_agent,
						   get_agent_key)
                           set_agent_key,

from .utils import (get_agent_ip_hostname)

__all__ = ['auth', 
		   'get_checkhealth', 
		   'get_list_agent', 
		   'get_summary_agents_os', 
		   'get_summary_agents_status',
		   'set_register_agent',
		   'get_agent_ip_hostname',
		   'get_agent_key']
		   'set_agent_key',
