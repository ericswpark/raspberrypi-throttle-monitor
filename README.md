# raspberrypi-throttle-monitor

CLI tool to monitor your Raspberry Pi status. Uses
`vcgencmd get_throttled` to fetch system information.

Thanks to the original project,
[throttle-status][original-project] by M4XDMG.

[original-project]: https://github.com/M4XDMG/throttle-status

# Setup

1. Clone or download repository
2. Use the `run.sh` script.


# Full Output

```
111100000000000001111
||||             ||||_ under-voltage
||||             |||_ currently throttled
||||             ||_ arm frequency capped
||||             |_ soft temperature reached
||||_ under-voltage has occurred since last reboot
|||_ throttling has occurred since last reboot
||_ arm frequency capped has occurred since last reboot
|_ soft temperature reached since last reboot
```