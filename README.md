# CiscoIOSBackupScript
To centralize backups from cisco IOS devices with python script

IMPORTANT!

- First, install **netmiko** module in your python environment
- Put the script in the desired bacjup storage directory
- Create a "IPs.yml" file in the desired backup storage directory with the list of all IPs of the devices you want to backup
  In the format:
  - "- 192.x.x.x"
  - "- 10.x.x.x"
  - "- 172.x.x.x"
  
  **Without Quotes!**
- Run the script, it will prompt for Cisco IOS devices shared credentials, you can provide it.
- Then you can see all backups files in the current directory
- You also can see failed conections with failed IPs in the "errip.yml" file

Author: Moises Pujols
