---
collection: ansible
version: "8"
title: "community.fortios.fmgr_secprof_av module – Manage security profile"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/fortios/fmgr_secprof_av_module.html
fetched_at: 2026-07-28T01:44:18+00:00
---
# community.fortios.fmgr_secprof_av module – Manage security profile

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/ui/repo/published/community/fortios/) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_secprof_av`.

- [Synopsis](fmgr_secprof_av_module.md#synopsis)
- [Parameters](fmgr_secprof_av_module.md#parameters)
- [Notes](fmgr_secprof_av_module.md#notes)
- [Examples](fmgr_secprof_av_module.md#examples)
- [Return Values](fmgr_secprof_av_module.md#return-values)

## [Synopsis](fmgr_secprof_av_module.md#id1)

- Manage security profile groups for FortiManager objects

## [Parameters](fmgr_secprof_av_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string | The ADOM the configuration should belong to.  **Default:** `"root"` |
| **analytics_bl_filetype**  string | Only submit files matching this DLP file-pattern to FortiSandbox. |
| **analytics_db**  string | Enable/disable using the FortiSandbox signature database to supplement the AV signature databases.  **Choices:**   - `"disable"` - `"enable"` |
| **analytics_max_upload**  string | Maximum size of files that can be uploaded to FortiSandbox (1 - 395 MBytes, default = 10). |
| **analytics_wl_filetype**  string | Do not submit files matching this DLP file-pattern to FortiSandbox. |
| **av_block_log**  string | Enable/disable logging for AntiVirus file blocking.  **Choices:**   - `"disable"` - `"enable"` |
| **av_virus_log**  string | Enable/disable AntiVirus logging.  **Choices:**   - `"disable"` - `"enable"` |
| **comment**  string | Comment. |
| **content_disarm**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **content_disarm_cover_page**  string | Enable/disable inserting a cover page into the disarmed document.  **Choices:**   - `"disable"` - `"enable"` |
| **content_disarm_detect_only**  string | Enable/disable only detect disarmable files, do not alter content.  **Choices:**   - `"disable"` - `"enable"` |
| **content_disarm_office_embed**  string | Enable/disable stripping of embedded objects in Microsoft Office documents.  **Choices:**   - `"disable"` - `"enable"` |
| **content_disarm_office_hylink**  string | Enable/disable stripping of hyperlinks in Microsoft Office documents.  **Choices:**   - `"disable"` - `"enable"` |
| **content_disarm_office_linked**  string | Enable/disable stripping of linked objects in Microsoft Office documents.  **Choices:**   - `"disable"` - `"enable"` |
| **content_disarm_office_macro**  string | Enable/disable stripping of macros in Microsoft Office documents.  **Choices:**   - `"disable"` - `"enable"` |
| **content_disarm_original_file_destination**  string | Destination to send original file if active content is removed.  **Choices:**   - `"fortisandbox"` - `"quarantine"` - `"discard"` |
| **content_disarm_pdf_act_form**  string | Enable/disable stripping of actions that submit data to other targets in PDF documents.  **Choices:**   - `"disable"` - `"enable"` |
| **content_disarm_pdf_act_gotor**  string | Enable/disable stripping of links to other PDFs in PDF documents.  **Choices:**   - `"disable"` - `"enable"` |
| **content_disarm_pdf_act_java**  string | Enable/disable stripping of actions that execute JavaScript code in PDF documents.  **Choices:**   - `"disable"` - `"enable"` |
| **content_disarm_pdf_act_launch**  string | Enable/disable stripping of links to external applications in PDF documents.  **Choices:**   - `"disable"` - `"enable"` |
| **content_disarm_pdf_act_movie**  string | Enable/disable stripping of embedded movies in PDF documents.  **Choices:**   - `"disable"` - `"enable"` |
| **content_disarm_pdf_act_sound**  string | Enable/disable stripping of embedded sound files in PDF documents.  **Choices:**   - `"disable"` - `"enable"` |
| **content_disarm_pdf_embedfile**  string | Enable/disable stripping of embedded files in PDF documents.  **Choices:**   - `"disable"` - `"enable"` |
| **content_disarm_pdf_hyperlink**  string | Enable/disable stripping of hyperlinks from PDF documents.  **Choices:**   - `"disable"` - `"enable"` |
| **content_disarm_pdf_javacode**  string | Enable/disable stripping of JavaScript code in PDF documents.  **Choices:**   - `"disable"` - `"enable"` |
| **extended_log**  string | Enable/disable extended logging for antivirus.  **Choices:**   - `"disable"` - `"enable"` |
| **ftgd_analytics**  string | Settings to control which files are uploaded to FortiSandbox.  **Choices:**   - `"disable"` - `"suspicious"` - `"everything"` |
| **ftp**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **ftp_archive_block**  string | Select the archive types to block.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **ftp_archive_log**  string | Select the archive types to log.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **ftp_emulator**  string | Enable/disable the virus emulator.  **Choices:**   - `"disable"` - `"enable"` |
| **ftp_options**  string | Enable/disable FTP AntiVirus scanning, monitoring, and quarantine.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"scan"` - `"quarantine"` - `"avmonitor"` |
| **ftp_outbreak_prevention**  string | Enable FortiGuard Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` |
| **http**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **http_archive_block**  string | Select the archive types to block.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **http_archive_log**  string | Select the archive types to log.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **http_content_disarm**  string | Enable Content Disarm and Reconstruction for this protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **http_emulator**  string | Enable/disable the virus emulator.  **Choices:**   - `"disable"` - `"enable"` |
| **http_options**  string | Enable/disable HTTP AntiVirus scanning, monitoring, and quarantine.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"scan"` - `"quarantine"` - `"avmonitor"` |
| **http_outbreak_prevention**  string | Enable FortiGuard Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` |
| **imap**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **imap_archive_block**  string | Select the archive types to block.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **imap_archive_log**  string | Select the archive types to log.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **imap_content_disarm**  string | Enable Content Disarm and Reconstruction for this protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **imap_emulator**  string | Enable/disable the virus emulator.  **Choices:**   - `"disable"` - `"enable"` |
| **imap_executables**  string | Treat Windows executable files as viruses for the purpose of blocking or monitoring.  **Choices:**   - `"default"` - `"virus"` |
| **imap_options**  string | Enable/disable IMAP AntiVirus scanning, monitoring, and quarantine.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"scan"` - `"quarantine"` - `"avmonitor"` |
| **imap_outbreak_prevention**  string | Enable FortiGuard Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` |
| **inspection_mode**  string | Inspection mode.  **Choices:**   - `"proxy"` - `"flow-based"` |
| **mapi**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **mapi_archive_block**  string | Select the archive types to block.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **mapi_archive_log**  string | Select the archive types to log.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **mapi_emulator**  string | Enable/disable the virus emulator.  **Choices:**   - `"disable"` - `"enable"` |
| **mapi_executables**  string | Treat Windows executable files as viruses for the purpose of blocking or monitoring.  **Choices:**   - `"default"` - `"virus"` |
| **mapi_options**  string | Enable/disable MAPI AntiVirus scanning, monitoring, and quarantine.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"scan"` - `"quarantine"` - `"avmonitor"` |
| **mapi_outbreak_prevention**  string | Enable FortiGuard Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` |
| **mobile_malware_db**  string | Enable/disable using the mobile malware signature database.  **Choices:**   - `"disable"` - `"enable"` |
| **mode**  string | Sets one of three modes for managing the object.  Allows use of soft-adds instead of overwriting existing values  **Choices:**   - `"add"` ← (default) - `"set"` - `"delete"` - `"update"` |
| **nac_quar**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **nac_quar_expiry**  string | Duration of quarantine. |
| **nac_quar_infected**  string | Enable/Disable quarantining infected hosts to the banned user list.  **Choices:**   - `"none"` - `"quar-src-ip"` |
| **nac_quar_log**  string | Enable/disable AntiVirus quarantine logging.  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string | Profile name. |
| **nntp**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **nntp_archive_block**  string | Select the archive types to block.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **nntp_archive_log**  string | Select the archive types to log.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **nntp_emulator**  string | Enable/disable the virus emulator.  **Choices:**   - `"disable"` - `"enable"` |
| **nntp_options**  string | Enable/disable NNTP AntiVirus scanning, monitoring, and quarantine.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"scan"` - `"quarantine"` - `"avmonitor"` |
| **nntp_outbreak_prevention**  string | Enable FortiGuard Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` |
| **pop3**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **pop3_archive_block**  string | Select the archive types to block.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **pop3_archive_log**  string | Select the archive types to log.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **pop3_content_disarm**  string | Enable Content Disarm and Reconstruction for this protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **pop3_emulator**  string | Enable/disable the virus emulator.  **Choices:**   - `"disable"` - `"enable"` |
| **pop3_executables**  string | Treat Windows executable files as viruses for the purpose of blocking or monitoring.  **Choices:**   - `"default"` - `"virus"` |
| **pop3_options**  string | Enable/disable POP3 AntiVirus scanning, monitoring, and quarantine.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"scan"` - `"quarantine"` - `"avmonitor"` |
| **pop3_outbreak_prevention**  string | Enable FortiGuard Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` |
| **replacemsg_group**  string | Replacement message group customized for this profile. |
| **scan_mode**  string | Choose between full scan mode and quick scan mode.  **Choices:**   - `"quick"` - `"full"` |
| **smb**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **smb_archive_block**  string | Select the archive types to block.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **smb_archive_log**  string | Select the archive types to log.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **smb_emulator**  string | Enable/disable the virus emulator.  **Choices:**   - `"disable"` - `"enable"` |
| **smb_options**  string | Enable/disable SMB AntiVirus scanning, monitoring, and quarantine.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"scan"` - `"quarantine"` - `"avmonitor"` |
| **smb_outbreak_prevention**  string | Enable FortiGuard Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` |
| **smtp**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **smtp_archive_block**  string | Select the archive types to block.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **smtp_archive_log**  string | Select the archive types to log.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **smtp_content_disarm**  string | Enable Content Disarm and Reconstruction for this protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **smtp_emulator**  string | Enable/disable the virus emulator.  **Choices:**   - `"disable"` - `"enable"` |
| **smtp_executables**  string | Treat Windows executable files as viruses for the purpose of blocking or monitoring.  **Choices:**   - `"default"` - `"virus"` |
| **smtp_options**  string | Enable/disable SMTP AntiVirus scanning, monitoring, and quarantine.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"scan"` - `"quarantine"` - `"avmonitor"` |
| **smtp_outbreak_prevention**  string | Enable FortiGuard Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` |

## [Notes](fmgr_secprof_av_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_secprof_av_module.md#id4)

```yaml+jinja
- name: DELETE Profile
  community.fortios.fmgr_secprof_av:
    name: "Ansible_AV_Profile"
    mode: "delete"

- name: CREATE Profile
  community.fortios.fmgr_secprof_av:
    name: "Ansible_AV_Profile"
    comment: "Created by Ansible Module TEST"
    mode: "set"
    inspection_mode: "proxy"
    ftgd_analytics: "everything"
    av_block_log: "enable"
    av_virus_log: "enable"
    scan_mode: "full"
    mobile_malware_db: "enable"
    ftp_archive_block: "encrypted"
    ftp_outbreak_prevention: "files"
    ftp_archive_log: "timeout"
    ftp_emulator: "disable"
    ftp_options: "scan"
```

## [Return Values](fmgr_secprof_av_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  **Returned:** always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.fortios)
