import requests
from requests.auth import HTTPBasicAuth
import sys

def get_status():
    response = requests.get(
        'https://api.huum.eu/action/home/status',
        auth=HTTPBasicAuth('USERNAME', 'PASSWORD')
    )
    return interpret_status(response.json(), action='status')

def start_sauna(target_temperature):
    if not 40 <= target_temperature <= 110:
        return "Error: Target temperature must be between 40 and 110 degrees Celsius."
    headers = {'Content-Type': 'application/json'}
    data = {'targetTemperature': target_temperature}
    response = requests.post(
        'https://api.huum.eu/action/home/start',
        json=data,
        auth=HTTPBasicAuth('USERNAME', 'PASSWORD')
    )
    if response.status_code != 200:
        return f"Error: {response.json().get('message', 'Failed to start sauna.')}"
    return interpret_status(response.json(), action='start')

def stop_sauna():
    response = requests.post(
        'https://api.huum.eu/action/home/stop',
        auth=HTTPBasicAuth('USERNAME', 'PASSWORD')
    )
    if response.status_code != 200:
        return f"Error: {response.json().get('message', 'Failed to stop sauna.')}"
    return interpret_status(response.json(), action='stop')

def interpret_status(data, action):
    status_code_messages = {
        230: "offline.",
        231: "online and heating up.",
        232: "online but not heating right now.",
        233: "currently in use by another user and is locked.",
        400: "in emergency stop mode."
    }

    status = status_code_messages.get(data['statusCode'], "with an unknown status.")
    door_status = "closed" if data['door'] else "open"
    temperature_celsius = float(data['temperature'])
    temperature_fahrenheit = round((temperature_celsius * 9 / 5) + 32, 1)

    base_message = f"The sauna is {status} The door is {door_status}. The current temperature inside is {temperature_fahrenheit} degrees Fahrenheit."

    if action == 'status':
        message = f"Checked sauna status. {base_message}"
    elif action == 'start' and 'targetTemperature' in data:
        target_temp_celsius = float(data['targetTemperature'])
        target_temp_fahrenheit = round((target_temp_celsius * 9 / 5) + 32, 1)
        message = f"Started heating the sauna. It's set to reach a target temperature of {target_temp_fahrenheit} degrees Fahrenheit. {base_message}"
    elif action == 'stop':
        message = f"Stopped the sauna. {base_message}"
    else:
        message = base_message

    return message

if __name__ == "__main__":
    action = sys.argv[1]
    if action == 'status':
        print(get_status())
    elif action == 'start':
        if len(sys.argv) > 2:
            temp_fahrenheit = float(sys.argv[2])
            print(start_sauna(temp_fahrenheit))
        else:
            print("Temperature parameter missing for starting the sauna.")
    elif action == 'stop':
        print(stop_sauna())
    else:
        print('Invalid action')
