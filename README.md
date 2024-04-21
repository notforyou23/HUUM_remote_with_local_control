# HUUM Sauna Controller Documentation

## Local Control via Shortcuts

### Setup Instructions
1. Create a Shortcut:
   - Select the Run Script over SSH action.
   - Name the shortcut Sauna Status.
   - Command: python3 path/to/huum_shortcut.py status
   - Server IP: 192.169.4.20 (example IP address).
   - Enter the Raspberry Pi server's username and password.
   - Enable Show Script Result to display the output.

2. Duplicate for Additional Controls:
   - Duplicate the Sauna Status shortcut twice.
   - Rename to Sauna Start and Sauna Stop.
   - Modify commands:
     - Sauna Start: python3 path/to/huum_shortcut.py start 81.3 (include desired temperature in Celsius).
     - Sauna Stop: python3 path/to/huum_shortcut.py stop.

> Note: Ensure your Raspberry Pi is configured on your local network to support SSH access.

## API Integration for Remote Control

### Overview
- API Endpoints:
  - Get Sauna Status: GET https://api.huum.eu/action/home/status
  - Start Sauna: POST https://api.huum.eu/action/home/start (specify target temperature between 40°C and 110°C for three hours).
  - Stop Sauna: POST https://api.huum.eu/action/home/stop

### Response Structure
{
  "statusCode": 231,
  "door": true,
  "temperature": "23",
  "targetTemperature": "50",
  "startDate": 1507184846,
  "endDate": 1507184846,
  "duration": 0,
  "config": 2,
  "steamerError": 0,
  "paymentEndDate": null
}
- Fields:
  - statusCode: Current state (230: offline, 231: heating, 232: not heating, etc.).
  - door: Indicates if the sauna door is closed (true) or open (false).
  - temperature: Current internal temperature.
  - targetTemperature: Desired temperature setting.

### Script Usage
- Execute the script with the desired action and temperature (for starting):
  python huum_shortcut.py [action] [temperature if starting]
  - action: 'status', 'start', or 'stop'.
  - temperature: Required for 'start', a float in Celsius.

### Error Handling and Authentication
- Error Handling: Includes checks to ensure valid API responses and manage errors.
- Authentication: Uses credentials matching those in the official app, with HTTP requests managed via the requests library.

### Contributing
Contributions to enhance the script or add functionalities are encouraged, adhering to security best practices and coding standards.
