$downloadUrl=’https://packages.wazuh.com/4.x/windows/wazuh-agent-4.7.2-1.msi’;
Invoke-WebRequest -Uri $downloadUrl -OutFile ${env.tmp}\wazuh-agent; 

Get-Service WazuhSvc

Select-String -Path ‘C:\Program Files (x86)\ossec-agent\wazuh-agent.state’ -Pattern “^status”
