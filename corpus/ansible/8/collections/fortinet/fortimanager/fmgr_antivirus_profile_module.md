---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_antivirus_profile module – Configure AntiVirus profiles."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_antivirus_profile_module.html
fetched_at: 2026-07-28T02:07:51+00:00
---
# fortinet.fortimanager.fmgr_antivirus_profile module – Configure AntiVirus profiles.

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortimanager/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_antivirus_profile`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_antivirus_profile_module.md#synopsis)
- [Parameters](fmgr_antivirus_profile_module.md#parameters)
- [Notes](fmgr_antivirus_profile_module.md#notes)
- [Examples](fmgr_antivirus_profile_module.md#examples)
- [Return Values](fmgr_antivirus_profile_module.md#return-values)

## [Synopsis](fmgr_antivirus_profile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_antivirus_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **antivirus_profile**  dictionary | the top level parameters set |
| **analytics-accept-filetype**  string | Only submit files matching this DLP file-pattern to FortiSandbox. |
| **analytics-bl-filetype**  string | Only submit files matching this DLP file-pattern to FortiSandbox. |
| **analytics-db**  string | Enable/disable using the FortiSandbox signature database to supplement the AV signature databases.  **Choices:**   - `"disable"` - `"enable"` |
| **analytics-ignore-filetype**  string | Do not submit files matching this DLP file-pattern to FortiSandbox. |
| **analytics-max-upload**  integer | Maximum size of files that can be uploaded to FortiSandbox |
| **analytics-wl-filetype**  string | Do not submit files matching this DLP file-pattern to FortiSandbox. |
| **av-block-log**  string | Enable/disable logging for AntiVirus file blocking.  **Choices:**   - `"disable"` - `"enable"` |
| **av-virus-log**  string | Enable/disable AntiVirus logging.  **Choices:**   - `"disable"` - `"enable"` |
| **cifs**  dictionary | no description |
| **archive-block**  list / elements=string | Select the archive types to block.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **archive-log**  list / elements=string | Select the archive types to log.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **av-scan**  string | Enable AntiVirus scan service.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **emulator**  string | Enable/disable the virus emulator.  **Choices:**   - `"disable"` - `"enable"` |
| **external-blocklist**  string | Enable external-blocklist.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **fortiai**  string | Enable/disable scanning of files by FortiAI.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **fortindr**  string | Enable scanning of files by FortiNDR.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | Enable scanning of files by FortiSandbox.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | Enable/disable CIFS AntiVirus scanning, monitoring, and quarantine.  **Choices:**   - `"scan"` - `"quarantine"` - `"avmonitor"` |
| **outbreak-prevention**  string | Enable Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` - `"disable"` - `"block"` - `"monitor"` |
| **quarantine**  string | Enable/disable quarantine for infected files.  **Choices:**   - `"disable"` - `"enable"` |
| **comment**  string | Comment. |
| **content-disarm**  dictionary | no description |
| **cover-page**  string | Enable/disable inserting a cover page into the disarmed document.  **Choices:**   - `"disable"` - `"enable"` |
| **detect-only**  string | Enable/disable only detect disarmable files, do not alter content.  **Choices:**   - `"disable"` - `"enable"` |
| **error-action**  string | Action to be taken if CDR engine encounters an unrecoverable error.  **Choices:**   - `"block"` - `"log-only"` - `"ignore"` |
| **office-action**  string | Enable/disable stripping of PowerPoint action events in Microsoft Office documents.  **Choices:**   - `"disable"` - `"enable"` |
| **office-dde**  string | Enable/disable stripping of Dynamic Data Exchange events in Microsoft Office documents.  **Choices:**   - `"disable"` - `"enable"` |
| **office-embed**  string | Enable/disable stripping of embedded objects in Microsoft Office documents.  **Choices:**   - `"disable"` - `"enable"` |
| **office-hylink**  string | Enable/disable stripping of hyperlinks in Microsoft Office documents.  **Choices:**   - `"disable"` - `"enable"` |
| **office-linked**  string | Enable/disable stripping of linked objects in Microsoft Office documents.  **Choices:**   - `"disable"` - `"enable"` |
| **office-macro**  string | Enable/disable stripping of macros in Microsoft Office documents.  **Choices:**   - `"disable"` - `"enable"` |
| **original-file-destination**  string | Destination to send original file if active content is removed.  **Choices:**   - `"fortisandbox"` - `"quarantine"` - `"discard"` |
| **pdf-act-form**  string | Enable/disable stripping of PDF document actions that submit data to other targets.  **Choices:**   - `"disable"` - `"enable"` |
| **pdf-act-gotor**  string | Enable/disable stripping of PDF document actions that access other PDF documents.  **Choices:**   - `"disable"` - `"enable"` |
| **pdf-act-java**  string | Enable/disable stripping of PDF document actions that execute JavaScript code.  **Choices:**   - `"disable"` - `"enable"` |
| **pdf-act-launch**  string | Enable/disable stripping of PDF document actions that launch other applications.  **Choices:**   - `"disable"` - `"enable"` |
| **pdf-act-movie**  string | Enable/disable stripping of PDF document actions that play a movie.  **Choices:**   - `"disable"` - `"enable"` |
| **pdf-act-sound**  string | Enable/disable stripping of PDF document actions that play a sound.  **Choices:**   - `"disable"` - `"enable"` |
| **pdf-embedfile**  string | Enable/disable stripping of embedded files in PDF documents.  **Choices:**   - `"disable"` - `"enable"` |
| **pdf-hyperlink**  string | Enable/disable stripping of hyperlinks from PDF documents.  **Choices:**   - `"disable"` - `"enable"` |
| **pdf-javacode**  string | Enable/disable stripping of JavaScript code in PDF documents.  **Choices:**   - `"disable"` - `"enable"` |
| **ems-threat-feed**  string | Enable/disable use of EMS threat feed when performing AntiVirus scan.  **Choices:**   - `"disable"` - `"enable"` |
| **extended-log**  string | Enable/disable extended logging for antivirus.  **Choices:**   - `"disable"` - `"enable"` |
| **external-blocklist**  any | (list or str) One or more external malware block lists. |
| **external-blocklist-archive-scan**  string | Enable/disable external-blocklist archive scanning.  **Choices:**   - `"disable"` - `"enable"` |
| **external-blocklist-enable-all**  string | Enable/disable all external blocklists.  **Choices:**   - `"disable"` - `"enable"` |
| **feature-set**  string | Flow/proxy feature set.  **Choices:**   - `"proxy"` - `"flow"` |
| **fortiai-error-action**  string | Action to take if FortiAI encounters an error.  **Choices:**   - `"block"` - `"log-only"` - `"ignore"` |
| **fortiai-timeout-action**  string | Action to take if FortiAI encounters a scan timeout.  **Choices:**   - `"block"` - `"log-only"` - `"ignore"` |
| **fortindr-error-action**  string | Action to take if FortiNDR encounters an error.  **Choices:**   - `"log-only"` - `"block"` - `"ignore"` |
| **fortindr-timeout-action**  string | Action to take if FortiNDR encounters a scan timeout.  **Choices:**   - `"log-only"` - `"block"` - `"ignore"` |
| **fortisandbox-error-action**  string | Action to take if FortiSandbox inline scan encounters an error.  **Choices:**   - `"log-only"` - `"block"` - `"ignore"` |
| **fortisandbox-max-upload**  integer | Maximum size of files that can be uploaded to FortiSandbox. |
| **fortisandbox-mode**  string | FortiSandbox scan modes.  **Choices:**   - `"inline"` - `"analytics-suspicious"` - `"analytics-everything"` |
| **fortisandbox-timeout-action**  string | Action to take if FortiSandbox inline scan encounters a scan timeout.  **Choices:**   - `"log-only"` - `"block"` - `"ignore"` |
| **ftgd-analytics**  string | Settings to control which files are uploaded to FortiSandbox.  **Choices:**   - `"disable"` - `"suspicious"` - `"everything"` |
| **ftp**  dictionary | no description |
| **archive-block**  list / elements=string | Select the archive types to block.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **archive-log**  list / elements=string | Select the archive types to log.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **av-scan**  string | Enable AntiVirus scan service.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **emulator**  string | Enable/disable the virus emulator.  **Choices:**   - `"disable"` - `"enable"` |
| **external-blocklist**  string | Enable external-blocklist.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **fortiai**  string | Enable/disable scanning of files by FortiAI.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **fortindr**  string | Enable scanning of files by FortiNDR.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | Enable scanning of files by FortiSandbox.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | Enable/disable FTP AntiVirus scanning, monitoring, and quarantine.  **Choices:**   - `"scan"` - `"file-filter"` - `"quarantine"` - `"avquery"` - `"avmonitor"` |
| **outbreak-prevention**  string | Enable Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` - `"disable"` - `"block"` - `"monitor"` |
| **quarantine**  string | Enable/disable quarantine for infected files.  **Choices:**   - `"disable"` - `"enable"` |
| **http**  dictionary | no description |
| **archive-block**  list / elements=string | Select the archive types to block.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **archive-log**  list / elements=string | Select the archive types to log.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **av-optimize**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **av-scan**  string | Enable AntiVirus scan service.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **content-disarm**  string | Enable Content Disarm and Reconstruction for this protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **emulator**  string | Enable/disable the virus emulator.  **Choices:**   - `"disable"` - `"enable"` |
| **external-blocklist**  string | Enable external-blocklist.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **fortiai**  string | Enable/disable scanning of files by FortiAI.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **fortindr**  string | Enable scanning of files by FortiNDR.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | Enable scanning of files by FortiSandbox.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | Enable/disable HTTP AntiVirus scanning, monitoring, and quarantine.  **Choices:**   - `"scan"` - `"file-filter"` - `"quarantine"` - `"avquery"` - `"avmonitor"` - `"strict-file"` |
| **outbreak-prevention**  string | Enable Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` - `"disable"` - `"block"` - `"monitor"` |
| **quarantine**  string | Enable/disable quarantine for infected files.  **Choices:**   - `"disable"` - `"enable"` |
| **unknown-content-encoding**  string | Configure the action the FortiGate unit will take on unknown content-encoding.  **Choices:**   - `"block"` - `"inspect"` - `"bypass"` |
| **imap**  dictionary | no description |
| **archive-block**  list / elements=string | Select the archive types to block.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **archive-log**  list / elements=string | Select the archive types to log.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **av-scan**  string | Enable AntiVirus scan service.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **content-disarm**  string | Enable Content Disarm and Reconstruction for this protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **emulator**  string | Enable/disable the virus emulator.  **Choices:**   - `"disable"` - `"enable"` |
| **executables**  string | Treat Windows executable files as viruses for the purpose of blocking or monitoring.  **Choices:**   - `"default"` - `"virus"` |
| **external-blocklist**  string | Enable external-blocklist.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **fortiai**  string | Enable/disable scanning of files by FortiAI.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **fortindr**  string | Enable scanning of files by FortiNDR.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | Enable scanning of files by FortiSandbox.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | Enable/disable IMAP AntiVirus scanning, monitoring, and quarantine.  **Choices:**   - `"scan"` - `"file-filter"` - `"quarantine"` - `"avquery"` - `"avmonitor"` |
| **outbreak-prevention**  string | Enable Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` - `"disable"` - `"block"` - `"monitor"` |
| **quarantine**  string | Enable/disable quarantine for infected files.  **Choices:**   - `"disable"` - `"enable"` |
| **inspection-mode**  string | Inspection mode.  **Choices:**   - `"proxy"` - `"flow-based"` |
| **mapi**  dictionary | no description |
| **archive-block**  list / elements=string | Select the archive types to block.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **archive-log**  list / elements=string | Select the archive types to log.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **av-scan**  string | Enable AntiVirus scan service.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **emulator**  string | Enable/disable the virus emulator.  **Choices:**   - `"disable"` - `"enable"` |
| **executables**  string | Treat Windows executable files as viruses for the purpose of blocking or monitoring.  **Choices:**   - `"default"` - `"virus"` |
| **external-blocklist**  string | Enable external-blocklist.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **fortiai**  string | Enable/disable scanning of files by FortiAI.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **fortindr**  string | Enable scanning of files by FortiNDR.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | Enable scanning of files by FortiSandbox.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | Enable/disable MAPI AntiVirus scanning, monitoring, and quarantine.  **Choices:**   - `"scan"` - `"quarantine"` - `"avquery"` - `"avmonitor"` |
| **outbreak-prevention**  string | Enable Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` - `"disable"` - `"block"` - `"monitor"` |
| **quarantine**  string | Enable/disable quarantine for infected files.  **Choices:**   - `"disable"` - `"enable"` |
| **mobile-malware-db**  string | Enable/disable using the mobile malware signature database.  **Choices:**   - `"disable"` - `"enable"` |
| **nac-quar**  dictionary | no description |
| **expiry**  string | Duration of quarantine. |
| **infected**  string | Enable/Disable quarantining infected hosts to the banned user list.  **Choices:**   - `"none"` - `"quar-src-ip"` - `"quar-interface"` |
| **log**  string | Enable/disable AntiVirus quarantine logging.  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string / required | Profile name. |
| **nntp**  dictionary | no description |
| **archive-block**  list / elements=string | Select the archive types to block.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **archive-log**  list / elements=string | Select the archive types to log.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **av-scan**  string | Enable AntiVirus scan service.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **emulator**  string | Enable/disable the virus emulator.  **Choices:**   - `"disable"` - `"enable"` |
| **external-blocklist**  string | Enable external-blocklist.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **fortiai**  string | Enable/disable scanning of files by FortiAI.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **fortindr**  string | Enable scanning of files by FortiNDR.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | Enable scanning of files by FortiSandbox.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | Enable/disable NNTP AntiVirus scanning, monitoring, and quarantine.  **Choices:**   - `"scan"` - `"file-filter"` - `"quarantine"` - `"avquery"` - `"avmonitor"` |
| **outbreak-prevention**  string | Enable Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` - `"disable"` - `"block"` - `"monitor"` |
| **quarantine**  string | Enable/disable quarantine for infected files.  **Choices:**   - `"disable"` - `"enable"` |
| **outbreak-prevention**  dictionary | no description |
| **external-blocklist**  string | Enable/disable external malware blocklist.  **Choices:**   - `"disable"` - `"enable"` |
| **ftgd-service**  string | Enable/disable FortiGuard Virus outbreak prevention service.  **Choices:**   - `"disable"` - `"enable"` |
| **outbreak-prevention-archive-scan**  string | Enable/disable outbreak-prevention archive scanning.  **Choices:**   - `"disable"` - `"enable"` |
| **pop3**  dictionary | no description |
| **archive-block**  list / elements=string | Select the archive types to block.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **archive-log**  list / elements=string | Select the archive types to log.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **av-scan**  string | Enable AntiVirus scan service.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **content-disarm**  string | Enable Content Disarm and Reconstruction for this protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **emulator**  string | Enable/disable the virus emulator.  **Choices:**   - `"disable"` - `"enable"` |
| **executables**  string | Treat Windows executable files as viruses for the purpose of blocking or monitoring.  **Choices:**   - `"default"` - `"virus"` |
| **external-blocklist**  string | Enable external-blocklist.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **fortiai**  string | Enable/disable scanning of files by FortiAI.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **fortindr**  string | Enable scanning of files by FortiNDR.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | Enable scanning of files by FortiSandbox.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | Enable/disable POP3 AntiVirus scanning, monitoring, and quarantine.  **Choices:**   - `"scan"` - `"file-filter"` - `"quarantine"` - `"avquery"` - `"avmonitor"` |
| **outbreak-prevention**  string | Enable Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` - `"disable"` - `"block"` - `"monitor"` |
| **quarantine**  string | Enable/disable quarantine for infected files.  **Choices:**   - `"disable"` - `"enable"` |
| **replacemsg-group**  string | Replacement message group customized for this profile. |
| **scan-mode**  string | Choose between full scan mode and quick scan mode.  **Choices:**   - `"quick"` - `"full"` - `"legacy"` - `"default"` |
| **smb**  dictionary | no description |
| **archive-block**  list / elements=string | no description  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **archive-log**  list / elements=string | no description  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **emulator**  string | Enable/disable the virus emulator.  **Choices:**   - `"disable"` - `"enable"` |
| **options**  list / elements=string | no description  **Choices:**   - `"scan"` - `"quarantine"` - `"avquery"` - `"avmonitor"` |
| **outbreak-prevention**  string | Enable FortiGuard Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` |
| **smtp**  dictionary | no description |
| **archive-block**  list / elements=string | Select the archive types to block.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **archive-log**  list / elements=string | Select the archive types to log.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **av-scan**  string | Enable AntiVirus scan service.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **content-disarm**  string | Enable Content Disarm and Reconstruction for this protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **emulator**  string | Enable/disable the virus emulator.  **Choices:**   - `"disable"` - `"enable"` |
| **executables**  string | Treat Windows executable files as viruses for the purpose of blocking or monitoring.  **Choices:**   - `"default"` - `"virus"` |
| **external-blocklist**  string | Enable external-blocklist.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **fortiai**  string | Enable/disable scanning of files by FortiAI.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **fortindr**  string | Enable scanning of files by FortiNDR.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | Enable scanning of files by FortiSandbox.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | Enable/disable SMTP AntiVirus scanning, monitoring, and quarantine.  **Choices:**   - `"scan"` - `"file-filter"` - `"quarantine"` - `"avquery"` - `"avmonitor"` |
| **outbreak-prevention**  string | Enable Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` - `"disable"` - `"block"` - `"monitor"` |
| **quarantine**  string | Enable/disable quarantine for infected files.  **Choices:**   - `"disable"` - `"enable"` |
| **ssh**  dictionary | no description |
| **archive-block**  list / elements=string | Select the archive types to block.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **archive-log**  list / elements=string | Select the archive types to log.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **av-scan**  string | Enable AntiVirus scan service.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **emulator**  string | Enable/disable the virus emulator.  **Choices:**   - `"disable"` - `"enable"` |
| **external-blocklist**  string | Enable external-blocklist.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **fortiai**  string | Enable/disable scanning of files by FortiAI.  **Choices:**   - `"disable"` - `"monitor"` - `"block"` |
| **fortindr**  string | Enable scanning of files by FortiNDR.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | Enable scanning of files by FortiSandbox.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | Enable/disable SFTP and SCP AntiVirus scanning, monitoring, and quarantine.  **Choices:**   - `"avmonitor"` - `"quarantine"` - `"scan"` |
| **outbreak-prevention**  string | Enable Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` - `"disable"` - `"block"` - `"monitor"` |
| **quarantine**  string | Enable/disable quarantine for infected files.  **Choices:**   - `"disable"` - `"enable"` |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_antivirus_profile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_antivirus_profile_module.md#id4)

```yaml+jinja
- name: gathering fortimanager facts
  hosts: fortimanager00
  gather_facts: no
  connection: httpapi
  collections:
    - fortinet.fortimanager
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
   - name: retrieve all the antivirus profiles
     fmgr_fact:
       facts:
           selector: 'antivirus_profile'
           params:
               adom: 'ansible'
               profile: 'your_value'
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure AntiVirus profiles.
     fmgr_antivirus_profile:
        adom: ansible
        state: present
        antivirus_profile:
           analytics-db: disable
           analytics-max-upload: 20
           av-block-log: disable
           av-virus-log: disable
           comment: 'test comment'
           extended-log: disable
           ftgd-analytics: disable
           inspection-mode: proxy
           mobile-malware-db: disable
           name: 'antivirus-profile'
           scan-mode: quick
```

## [Return Values](fmgr_antivirus_profile_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meta**  dictionary | The result of the request.  **Returned:** always |
| **request_url**  string | The full url requested.  **Returned:** always  **Sample:** `"/sys/login/user"` |
| **response_code**  integer | The status of api request.  **Returned:** always  **Sample:** `0` |
| **response_data**  list / elements=string | The api response.  **Returned:** always |
| **response_message**  string | The descriptive message of the api response.  **Returned:** always  **Sample:** `"OK."` |
| **system_information**  dictionary | The information of the target system.  **Returned:** always |
| **rc**  integer | The status the request.  **Returned:** always  **Sample:** `0` |
| **version_check_warning**  list / elements=string | Warning if the parameters used in the playbook are not supported by the current FortiManager version.  **Returned:** complex |

### Authors

- Xinwei Du (@dux-fortinet)
- Xing Li (@lix-fortinet)
- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
- [Homepage](https://fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection)
