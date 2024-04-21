# HUUM sauna controller

# UPDATE FOR LOCAL CONTROL VIA SHORTCUTS
1. Create a new Shortcut
2. Choose the RUN SCRIPT OVER SSH
3. Name it SAUNA STATUS
4. Use this:  python3 path/to/huum_shortcut.py status
5. Add the "SHOW SCRIPT RESULT" option
6. Duplicate the shortcut twice, and then rename each respectively (Sauna Start; Sauna Stop)
7. Edit for each:
8. for Starting, include the desired temp in Celsius:  python3 path/to/huum_shortcut.py start 81.3
9. for Stopping:  python3 path/to/huum_shortcut.py stop

*this assumes you have a Raspberry Pi set up on your local network accessable via SSH.

GET - api.huum.eu/action/home/status - returns your current sauna status</br>
POST - api.huum.eu/action/home/start?targetTemperature=80 - wants targetTemperature as a parameter, which must be a number between 40 and 110, turns on the sauna for 3h</br>
POST - api.huum.eu/action/home/stop - turns off the sauna</br>
Basic authentication should be used and all requests must be over a https connection. The username and password are the same as in the app and the user must be connected to a sauna.</br>
All requests return the current state of the sauna in JSON: ({"statusCode": 232, "door": true, "temperature": "23", "targetTemperature": "50", "startDate": 1507184846, "endDate": 1507184846, "duration": 0, "config": 2, "steamerError": 0, "paymentEndDate" : SOMEDATE})</br>
statusCode:</br>
  230 - sauna offline</br>
  231 - online and heating</br>
  232 sauna online but not heating</br>
  233 sauna is beeing used by another user and is locked</br>
  400 sauna is put to emergency stop</br>
door: </br>
  true - the door is closed</br>
  false - the door is open and sauna can't be started</br>
temperature: The current temperature of the sauna</br>
targetTemperature: The temperature the sauna is trying to reach</br>
startDate: heating start time in UNIX</br>
endDate: heating end time</br>
duration: time of the remaining heating period</br>
config: </br>
  2 shows that the controller is configured to use a light system</br>
  1 shows that the controller is configured to use a steamer system</br>
  3 shows that the controller is configured to use both the light and steamer system .</br>
steamerError: if 1 then the steamer is empty of water and needs to be refilled also no steamer start is allowed</br>
paymentEndDate: shows the date when the payment period is ending. Only relevant for GSM controllers with our SIM card.</br>
GET - api.huum.eu/action/home/light - switches the light
