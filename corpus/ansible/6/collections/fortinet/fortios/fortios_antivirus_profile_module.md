---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_antivirus_profile module – Configure AntiVirus profiles in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_antivirus_profile_module.html
fetched_at: 2026-07-27T17:39:51+00:00
---
# fortinet.fortios.fortios_antivirus_profile module – Configure AntiVirus profiles in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_antivirus_profile_module.md#ansible-collections-fortinet-fortios-fortios-antivirus-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_antivirus_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_antivirus_profile_module.md#synopsis)
- [Requirements](fortios_antivirus_profile_module.md#requirements)
- [Parameters](fortios_antivirus_profile_module.md#parameters)
- [Notes](fortios_antivirus_profile_module.md#notes)
- [Examples](fortios_antivirus_profile_module.md#examples)
- [Return Values](fortios_antivirus_profile_module.md#return-values)

## [Synopsis](fortios_antivirus_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify antivirus feature and profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_antivirus_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_antivirus_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **antivirus_profile**  dictionary | Configure AntiVirus profiles. |
| **analytics_accept_filetype**  integer | Only submit files matching this DLP file-pattern to FortiSandbox (post-transfer scan only). Source dlp.filepattern.id. |
| **analytics_bl_filetype**  integer | Only submit files matching this DLP file-pattern to FortiSandbox. Source dlp.filepattern.id. |
| **analytics_db**  string | Enable/disable using the FortiSandbox signature database to supplement the AV signature databases.  Choices:   - `"disable"` - `"enable"` |
| **analytics_ignore_filetype**  integer | Do not submit files matching this DLP file-pattern to FortiSandbox (post-transfer scan only). Source dlp.filepattern.id. |
| **analytics_max_upload**  integer | Maximum size of files that can be uploaded to FortiSandbox. |
| **analytics_wl_filetype**  integer | Do not submit files matching this DLP file-pattern to FortiSandbox. Source dlp.filepattern.id. |
| **av_block_log**  string | Enable/disable logging for AntiVirus file blocking.  Choices:   - `"enable"` - `"disable"` |
| **av_virus_log**  string | Enable/disable AntiVirus logging.  Choices:   - `"enable"` - `"disable"` |
| **cifs**  dictionary | Configure CIFS AntiVirus options. |
| **archive_block**  list / elements=string | Select the archive types to block.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"timeout"` - `"unhandled"` - `"fileslimit"` |
| **archive_log**  list / elements=string | Select the archive types to log.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"timeout"` - `"unhandled"` - `"fileslimit"` |
| **av_scan**  string | Enable AntiVirus scan service.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **emulator**  string | Enable/disable the virus emulator.  Choices:   - `"enable"` - `"disable"` |
| **external_blocklist**  string | Enable external-blocklist. Analyzes files including the content of archives.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortiai**  string | Enable/disable scanning of files by FortiAI.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortindr**  string | Enable scanning of files by FortiNDR.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | Enable scanning of files by FortiSandbox.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | Enable/disable CIFS AntiVirus scanning, monitoring, and quarantine.  Choices:   - `"scan"` - `"avmonitor"` - `"quarantine"` |
| **outbreak_prevention**  string | Enable virus outbreak prevention service.  Choices:   - `"disable"` - `"block"` - `"monitor"` - `"disabled"` - `"files"` - `"full-archive"` |
| **quarantine**  string | Enable/disable quarantine for infected files.  Choices:   - `"disable"` - `"enable"` |
| **comment**  string | Comment. |
| **content_disarm**  dictionary | AV Content Disarm and Reconstruction settings. |
| **cover_page**  string | Enable/disable inserting a cover page into the disarmed document.  Choices:   - `"disable"` - `"enable"` |
| **detect_only**  string | Enable/disable only detect disarmable files, do not alter content.  Choices:   - `"disable"` - `"enable"` |
| **error_action**  string | Action to be taken if CDR engine encounters an unrecoverable error.  Choices:   - `"block"` - `"log-only"` - `"ignore"` |
| **office_action**  string | Enable/disable stripping of PowerPoint action events in Microsoft Office documents.  Choices:   - `"disable"` - `"enable"` |
| **office_dde**  string | Enable/disable stripping of Dynamic Data Exchange events in Microsoft Office documents.  Choices:   - `"disable"` - `"enable"` |
| **office_embed**  string | Enable/disable stripping of embedded objects in Microsoft Office documents.  Choices:   - `"disable"` - `"enable"` |
| **office_hylink**  string | Enable/disable stripping of hyperlinks in Microsoft Office documents.  Choices:   - `"disable"` - `"enable"` |
| **office_linked**  string | Enable/disable stripping of linked objects in Microsoft Office documents.  Choices:   - `"disable"` - `"enable"` |
| **office_macro**  string | Enable/disable stripping of macros in Microsoft Office documents.  Choices:   - `"disable"` - `"enable"` |
| **original_file_destination**  string | Destination to send original file if active content is removed.  Choices:   - `"fortisandbox"` - `"quarantine"` - `"discard"` |
| **pdf_act_form**  string | Enable/disable stripping of PDF document actions that submit data to other targets.  Choices:   - `"disable"` - `"enable"` |
| **pdf_act_gotor**  string | Enable/disable stripping of PDF document actions that access other PDF documents.  Choices:   - `"disable"` - `"enable"` |
| **pdf_act_java**  string | Enable/disable stripping of PDF document actions that execute JavaScript code.  Choices:   - `"disable"` - `"enable"` |
| **pdf_act_launch**  string | Enable/disable stripping of PDF document actions that launch other applications.  Choices:   - `"disable"` - `"enable"` |
| **pdf_act_movie**  string | Enable/disable stripping of PDF document actions that play a movie.  Choices:   - `"disable"` - `"enable"` |
| **pdf_act_sound**  string | Enable/disable stripping of PDF document actions that play a sound.  Choices:   - `"disable"` - `"enable"` |
| **pdf_embedfile**  string | Enable/disable stripping of embedded files in PDF documents.  Choices:   - `"disable"` - `"enable"` |
| **pdf_hyperlink**  string | Enable/disable stripping of hyperlinks from PDF documents.  Choices:   - `"disable"` - `"enable"` |
| **pdf_javacode**  string | Enable/disable stripping of JavaScript code in PDF documents.  Choices:   - `"disable"` - `"enable"` |
| **ems_threat_feed**  string | Enable/disable use of EMS threat feed when performing AntiVirus scan. Analyzes files including the content of archives.  Choices:   - `"disable"` - `"enable"` |
| **extended_log**  string | Enable/disable extended logging for antivirus.  Choices:   - `"enable"` - `"disable"` |
| **external_blocklist**  list / elements=dictionary | One or more external malware block lists. |
| **name**  string | External blocklist. Source system.external-resource.name. |
| **external_blocklist_archive_scan**  string | Enable/disable external-blocklist archive scanning.  Choices:   - `"disable"` - `"enable"` |
| **external_blocklist_enable_all**  string | Enable/disable all external blocklists.  Choices:   - `"disable"` - `"enable"` |
| **feature_set**  string | Flow/proxy feature set.  Choices:   - `"flow"` - `"proxy"` |
| **fortiai_error_action**  string | Action to take if FortiAI encounters an error.  Choices:   - `"log-only"` - `"block"` - `"ignore"` |
| **fortiai_timeout_action**  string | Action to take if FortiAI encounters a scan timeout.  Choices:   - `"log-only"` - `"block"` - `"ignore"` |
| **fortindr_error_action**  string | Action to take if FortiNDR encounters an error.  Choices:   - `"log-only"` - `"block"` - `"ignore"` |
| **fortindr_timeout_action**  string | Action to take if FortiNDR encounters a scan timeout.  Choices:   - `"log-only"` - `"block"` - `"ignore"` |
| **fortisandbox_error_action**  string | Action to take if FortiSandbox inline scan encounters an error.  Choices:   - `"log-only"` - `"block"` - `"ignore"` |
| **fortisandbox_max_upload**  integer | Maximum size of files that can be uploaded to FortiSandbox. |
| **fortisandbox_mode**  string | FortiSandbox scan modes.  Choices:   - `"inline"` - `"analytics-suspicious"` - `"analytics-everything"` |
| **fortisandbox_timeout_action**  string | Action to take if FortiSandbox inline scan encounters a scan timeout.  Choices:   - `"log-only"` - `"block"` - `"ignore"` |
| **ftgd_analytics**  string | Settings to control which files are uploaded to FortiSandbox.  Choices:   - `"disable"` - `"suspicious"` - `"everything"` |
| **ftp**  dictionary | Configure FTP AntiVirus options. |
| **archive_block**  list / elements=string | Select the archive types to block.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"timeout"` - `"unhandled"` - `"fileslimit"` |
| **archive_log**  list / elements=string | Select the archive types to log.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"timeout"` - `"unhandled"` - `"fileslimit"` |
| **av_scan**  string | Enable AntiVirus scan service.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **emulator**  string | Enable/disable the virus emulator.  Choices:   - `"enable"` - `"disable"` |
| **external_blocklist**  string | Enable external-blocklist. Analyzes files including the content of archives.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortiai**  string | Enable/disable scanning of files by FortiAI.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortindr**  string | Enable scanning of files by FortiNDR.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | Enable scanning of files by FortiSandbox.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | Enable/disable FTP AntiVirus scanning, monitoring, and quarantine.  Choices:   - `"scan"` - `"avmonitor"` - `"quarantine"` |
| **outbreak_prevention**  string | Enable virus outbreak prevention service.  Choices:   - `"disable"` - `"block"` - `"monitor"` - `"disabled"` - `"files"` - `"full-archive"` |
| **quarantine**  string | Enable/disable quarantine for infected files.  Choices:   - `"disable"` - `"enable"` |
| **http**  dictionary | Configure HTTP AntiVirus options. |
| **archive_block**  list / elements=string | Select the archive types to block.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"timeout"` - `"unhandled"` - `"fileslimit"` |
| **archive_log**  list / elements=string | Select the archive types to log.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"timeout"` - `"unhandled"` - `"fileslimit"` |
| **av_scan**  string | Enable AntiVirus scan service.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **content_disarm**  string | Enable/disable Content Disarm and Reconstruction when performing AntiVirus scan.  Choices:   - `"disable"` - `"enable"` |
| **emulator**  string | Enable/disable the virus emulator.  Choices:   - `"enable"` - `"disable"` |
| **external_blocklist**  string | Enable external-blocklist. Analyzes files including the content of archives.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortiai**  string | Enable/disable scanning of files by FortiAI.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortindr**  string | Enable scanning of files by FortiNDR.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | Enable scanning of files by FortiSandbox.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | Enable/disable HTTP AntiVirus scanning, monitoring, and quarantine.  Choices:   - `"scan"` - `"avmonitor"` - `"quarantine"` |
| **outbreak_prevention**  string | Enable virus outbreak prevention service.  Choices:   - `"disable"` - `"block"` - `"monitor"` - `"disabled"` - `"files"` - `"full-archive"` |
| **quarantine**  string | Enable/disable quarantine for infected files.  Choices:   - `"disable"` - `"enable"` |
| **unknown_content_encoding**  string | Configure the action the FortiGate unit will take on unknown content-encoding.  Choices:   - `"block"` - `"inspect"` - `"bypass"` |
| **imap**  dictionary | Configure IMAP AntiVirus options. |
| **archive_block**  list / elements=string | Select the archive types to block.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"timeout"` - `"unhandled"` - `"fileslimit"` |
| **archive_log**  list / elements=string | Select the archive types to log.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"timeout"` - `"unhandled"` - `"fileslimit"` |
| **av_scan**  string | Enable AntiVirus scan service.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **content_disarm**  string | Enable/disable Content Disarm and Reconstruction when performing AntiVirus scan.  Choices:   - `"disable"` - `"enable"` |
| **emulator**  string | Enable/disable the virus emulator.  Choices:   - `"enable"` - `"disable"` |
| **executables**  string | Treat Windows executable files as viruses for the purpose of blocking or monitoring.  Choices:   - `"default"` - `"virus"` |
| **external_blocklist**  string | Enable external-blocklist. Analyzes files including the content of archives.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortiai**  string | Enable/disable scanning of files by FortiAI.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortindr**  string | Enable scanning of files by FortiNDR.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | Enable scanning of files by FortiSandbox.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | Enable/disable IMAP AntiVirus scanning, monitoring, and quarantine.  Choices:   - `"scan"` - `"avmonitor"` - `"quarantine"` |
| **outbreak_prevention**  string | Enable virus outbreak prevention service.  Choices:   - `"disable"` - `"block"` - `"monitor"` - `"disabled"` - `"files"` - `"full-archive"` |
| **quarantine**  string | Enable/disable quarantine for infected files.  Choices:   - `"disable"` - `"enable"` |
| **inspection_mode**  string | Inspection mode.  Choices:   - `"proxy"` - `"flow-based"` |
| **mapi**  dictionary | Configure MAPI AntiVirus options. |
| **archive_block**  list / elements=string | Select the archive types to block.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"timeout"` - `"unhandled"` - `"fileslimit"` |
| **archive_log**  list / elements=string | Select the archive types to log.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"timeout"` - `"unhandled"` - `"fileslimit"` |
| **av_scan**  string | Enable AntiVirus scan service.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **emulator**  string | Enable/disable the virus emulator.  Choices:   - `"enable"` - `"disable"` |
| **executables**  string | Treat Windows executable files as viruses for the purpose of blocking or monitoring.  Choices:   - `"default"` - `"virus"` |
| **external_blocklist**  string | Enable external-blocklist. Analyzes files including the content of archives.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortiai**  string | Enable/disable scanning of files by FortiAI.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortindr**  string | Enable scanning of files by FortiNDR.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | Enable scanning of files by FortiSandbox.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | Enable/disable MAPI AntiVirus scanning, monitoring, and quarantine.  Choices:   - `"scan"` - `"avmonitor"` - `"quarantine"` |
| **outbreak_prevention**  string | Enable virus outbreak prevention service.  Choices:   - `"disable"` - `"block"` - `"monitor"` - `"disabled"` - `"files"` - `"full-archive"` |
| **quarantine**  string | Enable/disable quarantine for infected files.  Choices:   - `"disable"` - `"enable"` |
| **mobile_malware_db**  string | Enable/disable using the mobile malware signature database.  Choices:   - `"disable"` - `"enable"` |
| **nac_quar**  dictionary | Configure AntiVirus quarantine settings. |
| **expiry**  string | Duration of quarantine. |
| **infected**  string | Enable/Disable quarantining infected hosts to the banned user list.  Choices:   - `"none"` - `"quar-src-ip"` |
| **log**  string | Enable/disable AntiVirus quarantine logging.  Choices:   - `"enable"` - `"disable"` |
| **name**  string / required | Profile name. |
| **nntp**  dictionary | Configure NNTP AntiVirus options. |
| **archive_block**  list / elements=string | Select the archive types to block.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"timeout"` - `"unhandled"` - `"fileslimit"` |
| **archive_log**  list / elements=string | Select the archive types to log.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"timeout"` - `"unhandled"` - `"fileslimit"` |
| **av_scan**  string | Enable AntiVirus scan service.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **emulator**  string | Enable/disable the virus emulator.  Choices:   - `"enable"` - `"disable"` |
| **external_blocklist**  string | Enable external-blocklist. Analyzes files including the content of archives.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortiai**  string | Enable/disable scanning of files by FortiAI.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortindr**  string | Enable scanning of files by FortiNDR.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | Enable scanning of files by FortiSandbox.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | Enable/disable NNTP AntiVirus scanning, monitoring, and quarantine.  Choices:   - `"scan"` - `"avmonitor"` - `"quarantine"` |
| **outbreak_prevention**  string | Enable virus outbreak prevention service.  Choices:   - `"disable"` - `"block"` - `"monitor"` - `"disabled"` - `"files"` - `"full-archive"` |
| **quarantine**  string | Enable/disable quarantine for infected files.  Choices:   - `"disable"` - `"enable"` |
| **outbreak_prevention**  dictionary | Configure Virus Outbreak Prevention settings. |
| **external_blocklist**  string | Enable/disable external malware blocklist.  Choices:   - `"disable"` - `"enable"` |
| **ftgd_service**  string | Enable/disable FortiGuard Virus outbreak prevention service.  Choices:   - `"disable"` - `"enable"` |
| **outbreak_prevention_archive_scan**  string | Enable/disable outbreak-prevention archive scanning.  Choices:   - `"disable"` - `"enable"` |
| **pop3**  dictionary | Configure POP3 AntiVirus options. |
| **archive_block**  list / elements=string | Select the archive types to block.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"timeout"` - `"unhandled"` - `"fileslimit"` |
| **archive_log**  list / elements=string | Select the archive types to log.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"timeout"` - `"unhandled"` - `"fileslimit"` |
| **av_scan**  string | Enable AntiVirus scan service.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **content_disarm**  string | Enable/disable Content Disarm and Reconstruction when performing AntiVirus scan.  Choices:   - `"disable"` - `"enable"` |
| **emulator**  string | Enable/disable the virus emulator.  Choices:   - `"enable"` - `"disable"` |
| **executables**  string | Treat Windows executable files as viruses for the purpose of blocking or monitoring.  Choices:   - `"default"` - `"virus"` |
| **external_blocklist**  string | Enable external-blocklist. Analyzes files including the content of archives.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortiai**  string | Enable/disable scanning of files by FortiAI.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortindr**  string | Enable scanning of files by FortiNDR.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | Enable scanning of files by FortiSandbox.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | Enable/disable POP3 AntiVirus scanning, monitoring, and quarantine.  Choices:   - `"scan"` - `"avmonitor"` - `"quarantine"` |
| **outbreak_prevention**  string | Enable virus outbreak prevention service.  Choices:   - `"disable"` - `"block"` - `"monitor"` - `"disabled"` - `"files"` - `"full-archive"` |
| **quarantine**  string | Enable/disable quarantine for infected files.  Choices:   - `"disable"` - `"enable"` |
| **replacemsg_group**  string | Replacement message group customized for this profile. Source system.replacemsg-group.name. |
| **scan_mode**  string | Configure scan mode .  Choices:   - `"default"` - `"legacy"` - `"quick"` - `"full"` |
| **smb**  dictionary | Configure SMB AntiVirus options. |
| **archive_block**  string | Select the archive types to block.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"fileslimit"` - `"timeout"` - `"unhandled"` |
| **archive_log**  string | Select the archive types to log.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"fileslimit"` - `"timeout"` - `"unhandled"` |
| **emulator**  string | Enable/disable the virus emulator.  Choices:   - `"enable"` - `"disable"` |
| **options**  string | Enable/disable SMB AntiVirus scanning, monitoring, and quarantine.  Choices:   - `"scan"` - `"avmonitor"` - `"quarantine"` |
| **outbreak_prevention**  string | Enable FortiGuard Virus Outbreak Prevention service.  Choices:   - `"disabled"` - `"files"` - `"full-archive"` |
| **smtp**  dictionary | Configure SMTP AntiVirus options. |
| **archive_block**  list / elements=string | Select the archive types to block.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"timeout"` - `"unhandled"` - `"fileslimit"` |
| **archive_log**  list / elements=string | Select the archive types to log.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"timeout"` - `"unhandled"` - `"fileslimit"` |
| **av_scan**  string | Enable AntiVirus scan service.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **content_disarm**  string | Enable/disable Content Disarm and Reconstruction when performing AntiVirus scan.  Choices:   - `"disable"` - `"enable"` |
| **emulator**  string | Enable/disable the virus emulator.  Choices:   - `"enable"` - `"disable"` |
| **executables**  string | Treat Windows executable files as viruses for the purpose of blocking or monitoring.  Choices:   - `"default"` - `"virus"` |
| **external_blocklist**  string | Enable external-blocklist. Analyzes files including the content of archives.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortiai**  string | Enable/disable scanning of files by FortiAI.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortindr**  string | Enable scanning of files by FortiNDR.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | Enable scanning of files by FortiSandbox.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | Enable/disable SMTP AntiVirus scanning, monitoring, and quarantine.  Choices:   - `"scan"` - `"avmonitor"` - `"quarantine"` |
| **outbreak_prevention**  string | Enable virus outbreak prevention service.  Choices:   - `"disable"` - `"block"` - `"monitor"` - `"disabled"` - `"files"` - `"full-archive"` |
| **quarantine**  string | Enable/disable quarantine for infected files.  Choices:   - `"disable"` - `"enable"` |
| **ssh**  dictionary | Configure SFTP and SCP AntiVirus options. |
| **archive_block**  list / elements=string | Select the archive types to block.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"timeout"` - `"unhandled"` - `"fileslimit"` |
| **archive_log**  list / elements=string | Select the archive types to log.  Choices:   - `"encrypted"` - `"corrupted"` - `"partiallycorrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"timeout"` - `"unhandled"` - `"fileslimit"` |
| **av_scan**  string | Enable AntiVirus scan service.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **emulator**  string | Enable/disable the virus emulator.  Choices:   - `"enable"` - `"disable"` |
| **external_blocklist**  string | Enable external-blocklist. Analyzes files including the content of archives.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortiai**  string | Enable/disable scanning of files by FortiAI.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortindr**  string | Enable scanning of files by FortiNDR.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | Enable scanning of files by FortiSandbox.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | Enable/disable SFTP and SCP AntiVirus scanning, monitoring, and quarantine.  Choices:   - `"scan"` - `"avmonitor"` - `"quarantine"` |
| **outbreak_prevention**  string | Enable virus outbreak prevention service.  Choices:   - `"disable"` - `"block"` - `"monitor"` - `"disabled"` - `"files"` - `"full-archive"` |
| **quarantine**  string | Enable/disable quarantine for infected files.  Choices:   - `"disable"` - `"enable"` |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_antivirus_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_antivirus_profile_module.md#id5)

```yaml+jinja
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure AntiVirus profiles.
    fortios_antivirus_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      antivirus_profile:
        analytics_accept_filetype: "0"
        analytics_bl_filetype: "2147483647"
        analytics_db: "disable"
        analytics_ignore_filetype: "0"
        analytics_max_upload: "10"
        analytics_wl_filetype: "2147483647"
        av_block_log: "enable"
        av_virus_log: "enable"
        cifs:
            archive_block: "encrypted"
            archive_log: "encrypted"
            av_scan: "disable"
            emulator: "enable"
            external_blocklist: "disable"
            fortiai: "disable"
            fortindr: "disable"
            fortisandbox: "disable"
            options: "scan"
            outbreak_prevention: "disable"
            quarantine: "disable"
        comment: "Comment."
        content_disarm:
            cover_page: "disable"
            detect_only: "disable"
            error_action: "block"
            office_action: "disable"
            office_dde: "disable"
            office_embed: "disable"
            office_hylink: "disable"
            office_linked: "disable"
            office_macro: "disable"
            original_file_destination: "fortisandbox"
            pdf_act_form: "disable"
            pdf_act_gotor: "disable"
            pdf_act_java: "disable"
            pdf_act_launch: "disable"
            pdf_act_movie: "disable"
            pdf_act_sound: "disable"
            pdf_embedfile: "disable"
            pdf_hyperlink: "disable"
            pdf_javacode: "disable"
        ems_threat_feed: "disable"
        extended_log: "enable"
        external_blocklist:
         -
            name: "default_name_47 (source system.external-resource.name)"
        external_blocklist_archive_scan: "disable"
        external_blocklist_enable_all: "disable"
        feature_set: "flow"
        fortiai_error_action: "log-only"
        fortiai_timeout_action: "log-only"
        fortindr_error_action: "log-only"
        fortindr_timeout_action: "log-only"
        fortisandbox_error_action: "log-only"
        fortisandbox_max_upload: "10"
        fortisandbox_mode: "inline"
        fortisandbox_timeout_action: "log-only"
        ftgd_analytics: "disable"
        ftp:
            archive_block: "encrypted"
            archive_log: "encrypted"
            av_scan: "disable"
            emulator: "enable"
            external_blocklist: "disable"
            fortiai: "disable"
            fortindr: "disable"
            fortisandbox: "disable"
            options: "scan"
            outbreak_prevention: "disable"
            quarantine: "disable"
        http:
            archive_block: "encrypted"
            archive_log: "encrypted"
            av_scan: "disable"
            content_disarm: "disable"
            emulator: "enable"
            external_blocklist: "disable"
            fortiai: "disable"
            fortindr: "disable"
            fortisandbox: "disable"
            options: "scan"
            outbreak_prevention: "disable"
            quarantine: "disable"
            unknown_content_encoding: "block"
        imap:
            archive_block: "encrypted"
            archive_log: "encrypted"
            av_scan: "disable"
            content_disarm: "disable"
            emulator: "enable"
            executables: "default"
            external_blocklist: "disable"
            fortiai: "disable"
            fortindr: "disable"
            fortisandbox: "disable"
            options: "scan"
            outbreak_prevention: "disable"
            quarantine: "disable"
        inspection_mode: "proxy"
        mapi:
            archive_block: "encrypted"
            archive_log: "encrypted"
            av_scan: "disable"
            emulator: "enable"
            executables: "default"
            external_blocklist: "disable"
            fortiai: "disable"
            fortindr: "disable"
            fortisandbox: "disable"
            options: "scan"
            outbreak_prevention: "disable"
            quarantine: "disable"
        mobile_malware_db: "disable"
        nac_quar:
            expiry: "<your_own_value>"
            infected: "none"
            log: "enable"
        name: "default_name_119"
        nntp:
            archive_block: "encrypted"
            archive_log: "encrypted"
            av_scan: "disable"
            emulator: "enable"
            external_blocklist: "disable"
            fortiai: "disable"
            fortindr: "disable"
            fortisandbox: "disable"
            options: "scan"
            outbreak_prevention: "disable"
            quarantine: "disable"
        outbreak_prevention:
            external_blocklist: "disable"
            ftgd_service: "disable"
        outbreak_prevention_archive_scan: "disable"
        pop3:
            archive_block: "encrypted"
            archive_log: "encrypted"
            av_scan: "disable"
            content_disarm: "disable"
            emulator: "enable"
            executables: "default"
            external_blocklist: "disable"
            fortiai: "disable"
            fortindr: "disable"
            fortisandbox: "disable"
            options: "scan"
            outbreak_prevention: "disable"
            quarantine: "disable"
        replacemsg_group: "<your_own_value> (source system.replacemsg-group.name)"
        scan_mode: "default"
        smb:
            archive_block: "encrypted"
            archive_log: "encrypted"
            emulator: "enable"
            options: "scan"
            outbreak_prevention: "disabled"
        smtp:
            archive_block: "encrypted"
            archive_log: "encrypted"
            av_scan: "disable"
            content_disarm: "disable"
            emulator: "enable"
            executables: "default"
            external_blocklist: "disable"
            fortiai: "disable"
            fortindr: "disable"
            fortisandbox: "disable"
            options: "scan"
            outbreak_prevention: "disable"
            quarantine: "disable"
        ssh:
            archive_block: "encrypted"
            archive_log: "encrypted"
            av_scan: "disable"
            emulator: "enable"
            external_blocklist: "disable"
            fortiai: "disable"
            fortindr: "disable"
            fortisandbox: "disable"
            options: "scan"
            outbreak_prevention: "disable"
            quarantine: "disable"
```

## [Return Values](fortios_antivirus_profile_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
