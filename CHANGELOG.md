# Changelog

## [v0.0.0] - Initial Scaffolding
- Project structure created (src/, tests/)
- Git repo initialized
- Python venv configured
- .gitignore added

## [v0.1.0] - ARP Network Scan
- Added `scan()` function that sends ARP requests across a network range and returns each responding device's IP and MAC address
- Network range and interface configurable via `NETWORK_RANGE` and `NETWORK_IFACE` (loaded from `.env` with python-dotenv)
- Added `.env.example` as a config template
- Added `requirements.txt` (scapy, python-dotenv)
- Running `scanner.py` directly prints a list of found devices

## [v0.2.0] - Runs as a systemd Service
- Added Makefile: `make install` puts netwatch in `/opt/netwatch` with its own venv, and creates `/etc/netwatch/netwatch.env` from `.env.example` without overwriting an existing config
- Added `netwatch.service`: runs as a dedicated `netwatch` user with only `CAP_NET_RAW`, no root needed
- Added `netwatch.timer`: scans every 5 minutes, starting 1 minute after boot
