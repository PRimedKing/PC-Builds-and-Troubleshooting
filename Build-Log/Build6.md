# Build 6: Ryzen 9 9900X — Flagship Build, Sensor Defect & Full Tune

## Parts Used
- CPU: AMD Ryzen 9 9900X
- Motherboard: MSI MAG X870E Tomahawk WiFi
- GPU: PowerColor Red Devil Radeon RX 9070 XT
- RAM: 32GB Corsair Vengeance RGB DDR5-6000 CL36
- Cooler: Arctic Liquid Freezer III 360 AIO
- PSU: be quiet! Pure Power 13 M 1000W
- Thermal Paste: Arctic MX-7
- Case: Lian Li 217 (Black)

## Build Steps
1. Mounted motherboard, CPU, and AIO cold plate with MX-7.
2. Installed RAM, GPU, and storage; routed and managed cables.
3. Connected PSU and front-panel wiring; first boot to BIOS.
4. Updated BIOS from v2.A91 to v2.AC24.
5. Enabled EXPO Profile 1 (DDR5-6000, CL36) and installed the OS.

## Issues & Solutions
- Issue: CPU temperature sensor latches at ~70°C after fast temperature spikes, and the PC occasionally hangs on shutdown. Tell in HWiNFO: CPU Package Power reads 0 W while the sensor is latched.
- Diagnosis: Board and CPU were RMA'd once — no fault found, and the board is out of warranty. The latching behavior is reported by other owners of this board/CPU combination, so I treated it as a platform quirk to manage, not a dead part.
- Solution: Tuned the CPU to stay clear of the spike behavior — Curve Optimizer −15 all-core, PPT 180W / TDC 110A / EDC 150A, 85°C thermal cap. No latch observed during validation runs.

## Optimization Notes
- GPU: −80mV voltage offset, +10% power limit. Result: 32°C idle, 56°C max under stress test, 3184 MHz peak clock.
- CPU validation: Cinebench 2026, 10-minute multi-core loop — 7042 points, max CPU temp 68°C, sensor did not latch.
- USB standby power (charging devices with the PC off): on this board the lever is Resume By USB Device = Enabled with ErP Ready = Disabled — there is no separate S4/S5 USB power toggle in this firmware.
- Still open: an extended gaming session as the final stability check.
