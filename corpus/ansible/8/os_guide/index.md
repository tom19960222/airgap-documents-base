---
collection: ansible
version: "8"
title: "Using Ansible on Windows and BSD"
source_url: https://docs.ansible.com/projects/ansible/8/os_guide/index.html
fetched_at: 2026-07-28T00:57:45+00:00
---
# Using Ansible on Windows and BSD

> **Note:**
>
> **Making Open Source More Inclusive**
>
> Red Hat is committed to replacing problematic language in our code, documentation, and web properties. We are beginning with these four terms: master, slave, blacklist, and whitelist. We ask that you open an issue or pull request if you come upon a term that we have missed. For more details, see [our CTO Chris Wright’s message](https://www.redhat.com/en/blog/making-open-source-more-inclusive-eradicating-problematic-language).

Welcome to the Ansible guide for Microsoft Windows and BSD.
Because Windows is not a POSIX-compliant operating system, Ansible interacts with Windows hosts differently to Linux/Unix hosts.
Likewise managing hosts that run BSD is different to managing other Unix-like host operating systems.
Find out everything you need to know about using Ansible on Windows and with BSD hosts.

- [Setting up a Windows Host](windows_setup.md)
  - [Host Requirements](windows_setup.md#host-requirements)
  - [WinRM Setup](windows_setup.md#id1)
  - [Windows SSH Setup](windows_setup.md#windows-ssh-setup)
- [Using Ansible and Windows](windows_usage.md)
  - [Use Cases](windows_usage.md#use-cases)
  - [Path Formatting for Windows](windows_usage.md#path-formatting-for-windows)
  - [Limitations](windows_usage.md#limitations)
  - [Developing Windows Modules](windows_usage.md#developing-windows-modules)
- [Windows Remote Management](windows_winrm.md)
  - [What is WinRM?](windows_winrm.md#what-is-winrm)
  - [WinRM authentication options](windows_winrm.md#winrm-authentication-options)
  - [Non-Administrator Accounts](windows_winrm.md#non-administrator-accounts)
  - [WinRM Encryption](windows_winrm.md#winrm-encryption)
  - [Inventory Options](windows_winrm.md#inventory-options)
  - [IPv6 Addresses](windows_winrm.md#ipv6-addresses)
  - [HTTPS Certificate Validation](windows_winrm.md#https-certificate-validation)
  - [TLS 1.2 Support](windows_winrm.md#tls-1-2-support)
  - [WinRM limitations](windows_winrm.md#winrm-limitations)
- [Desired State Configuration](windows_dsc.md)
  - [What is Desired State Configuration?](windows_dsc.md#what-is-desired-state-configuration)
  - [Host Requirements](windows_dsc.md#host-requirements)
  - [Why Use DSC?](windows_dsc.md#why-use-dsc)
  - [How to Use DSC?](windows_dsc.md#how-to-use-dsc)
  - [Custom DSC Resources](windows_dsc.md#custom-dsc-resources)
  - [Examples](windows_dsc.md#examples)
- [Windows performance](windows_performance.md)
  - [Optimize PowerShell performance to reduce Ansible task overhead](windows_performance.md#optimize-powershell-performance-to-reduce-ansible-task-overhead)
  - [Fix high-CPU-on-boot for VMs/cloud instances](windows_performance.md#fix-high-cpu-on-boot-for-vms-cloud-instances)
- [Windows Frequently Asked Questions](windows_faq.md)
  - [Does Ansible work with Windows XP or Server 2003?](windows_faq.md#does-ansible-work-with-windows-xp-or-server-2003)
  - [Are Server 2008, 2008 R2 and Windows 7 supported?](windows_faq.md#are-server-2008-2008-r2-and-windows-7-supported)
  - [Can I manage Windows Nano Server with Ansible?](windows_faq.md#can-i-manage-windows-nano-server-with-ansible)
  - [Can Ansible run on Windows?](windows_faq.md#can-ansible-run-on-windows)
  - [Can I use SSH keys to authenticate to Windows hosts?](windows_faq.md#can-i-use-ssh-keys-to-authenticate-to-windows-hosts)
  - [Why can I run a command locally that does not work under Ansible?](windows_faq.md#why-can-i-run-a-command-locally-that-does-not-work-under-ansible)
  - [This program won’t install on Windows with Ansible](windows_faq.md#this-program-won-t-install-on-windows-with-ansible)
  - [What Windows modules are available?](windows_faq.md#what-windows-modules-are-available)
  - [Can I run Python modules on Windows hosts?](windows_faq.md#can-i-run-python-modules-on-windows-hosts)
  - [Can I connect to Windows hosts over SSH?](windows_faq.md#can-i-connect-to-windows-hosts-over-ssh)
  - [Why is connecting to a Windows host through SSH failing?](windows_faq.md#why-is-connecting-to-a-windows-host-through-ssh-failing)
  - [Why are my credentials being rejected?](windows_faq.md#why-are-my-credentials-being-rejected)
  - [Why am I getting an error SSL CERTIFICATE_VERIFY_FAILED?](windows_faq.md#why-am-i-getting-an-error-ssl-certificate-verify-failed)
- [Managing BSD hosts with Ansible](intro_bsd.md)
  - [Connecting to BSD nodes](intro_bsd.md#connecting-to-bsd-nodes)
  - [Bootstrapping BSD](intro_bsd.md#bootstrapping-bsd)
  - [Setting the Python interpreter](intro_bsd.md#setting-the-python-interpreter)
  - [Which modules are available?](intro_bsd.md#which-modules-are-available)
  - [Using BSD as the control node](intro_bsd.md#using-bsd-as-the-control-node)
  - [BSD facts](intro_bsd.md#bsd-facts)
  - [BSD efforts and contributions](intro_bsd.md#bsd-efforts-and-contributions)
