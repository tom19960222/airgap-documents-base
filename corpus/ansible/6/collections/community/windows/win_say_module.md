---
collection: ansible
version: "6"
title: "community.windows.win_say module – Text to speech module for Windows to speak messages and optionally play sounds"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_say_module.html
fetched_at: 2026-07-27T17:23:54+00:00
---
# community.windows.win_say module – Text to speech module for Windows to speak messages and optionally play sounds

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_say`.

- [Synopsis](win_say_module.md#synopsis)
- [Parameters](win_say_module.md#parameters)
- [Notes](win_say_module.md#notes)
- [See Also](win_say_module.md#see-also)
- [Examples](win_say_module.md#examples)
- [Return Values](win_say_module.md#return-values)

## [Synopsis](win_say_module.md#id1)

- Uses .NET libraries to convert text to speech and optionally play .wav sounds. Audio Service needs to be running and some kind of speakers or headphones need to be attached to the windows target(s) for the speech to be audible.

## [Parameters](win_say_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **end_sound_path**  path | Full path to a `.wav` file containing a sound to play after the text has been spoken.  Useful on conference calls to alert other speakers that ansible has finished speaking. |
| **msg**  string | The text to be spoken.  Use either `msg` or `msg_file`.  Optional so that you can use this module just to play sounds. |
| **msg_file**  path | Full path to a windows format text file containing the text to be spoken.  Use either `msg` or `msg_file`.  Optional so that you can use this module just to play sounds. |
| **speech_speed**  integer | How fast or slow to speak the text.  Must be an integer value in the range -10 to 10.  -10 is slowest, 10 is fastest.  Default: `0` |
| **start_sound_path**  path | Full path to a `.wav` file containing a sound to play before the text is spoken.  Useful on conference calls to alert other speakers that ansible has something to say. |
| **voice**  string | Which voice to use. See notes for how to discover installed voices.  If the requested voice is not available the default voice will be used. Example voice names from Windows 10 are `Microsoft Zira Desktop` and `Microsoft Hazel Desktop`. |

## [Notes](win_say_module.md#id3)

> **Note:**
>
> - Needs speakers or headphones to do anything useful.
> - To find which voices are installed, run the following Powershell commands.
>
>   > Add-Type -AssemblyName System.Speech
>   > $speech = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer
>   > $speech.GetInstalledVoices() | ForEach-Object { $_.VoiceInfo }
>   > $speech.Dispose()
> - Speech can be surprisingly slow, so it’s best to keep message text short.

## [See Also](win_say_module.md#id4)

> **See also:**
>
> [community.windows.win_msg](win_msg_module.md#ansible-collections-community-windows-win-msg-module)
> :   Sends a message to logged in users on Windows hosts.
>
> [community.windows.win_toast](win_toast_module.md#ansible-collections-community-windows-win-toast-module)
> :   Sends Toast windows notification to logged in users on Windows 10 or later hosts.

## [Examples](win_say_module.md#id5)

```yaml+jinja
- name: Warn of impending deployment
  community.windows.win_say:
    msg: Warning, deployment commencing in 5 minutes, please log out.

- name: Using a different voice and a start sound
  community.windows.win_say:
    start_sound_path: C:\Windows\Media\ding.wav
    msg: Warning, deployment commencing in 5 minutes, please log out.
    voice: Microsoft Hazel Desktop

- name: With start and end sound
  community.windows.win_say:
    start_sound_path: C:\Windows\Media\Windows Balloon.wav
    msg: New software installed
    end_sound_path: C:\Windows\Media\chimes.wav

- name: Text from file example
  community.windows.win_say:
    start_sound_path: C:\Windows\Media\Windows Balloon.wav
    msg_file: AppData\Local\Temp\morning_report.txt
    end_sound_path: C:\Windows\Media\chimes.wav
```

## [Return Values](win_say_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **message_text**  string | The text that the module attempted to speak.  Returned: success  Sample: `"Warning, deployment commencing in 5 minutes."` |
| **voice**  string | The voice used to speak the text.  Returned: success  Sample: `"Microsoft Hazel Desktop"` |
| **voice_info**  string | The voice used to speak the text.  Returned: when requested voice could not be loaded  Sample: `"Could not load voice TestVoice, using system default voice"` |

### Authors

- Jon Hawkesworth (@jhawkesworth)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
