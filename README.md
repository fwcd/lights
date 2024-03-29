# Lights
A small CLI utility for controlling your smart lamps at home.

![Icon](lights-icon.png)

Currently only Philips Hue lamps are supported, but adding support for other backends is easy.

## Getting Started
* Optionally setup a virtual environment:
    * Create a venv using `python3 -m venv venv`
    * Activate the venv using `source venv/bin/activate`
* Make sure that Wheel is installed using `pip3 install wheel`
* Finally install the dependencies with `pip3 install -r requirements.txt`

## Usage
`lights [-h] [-b HUE_BRIDGE_IP] [-n NAME] ...`

> Note that you can alternatively provide the environment variables `LIGHTS_HUE_BRIDGE_IP` and `LIGHTS_NAME`.

> If no lights are selected, the tool will automatically select all of the available lights.

Examples:
* `lights on`
* `lights off`
* `lights toggle`
* `lights color blue`
* `lights dim 50`
* `lights -n "My Lamp" on`

## Installing
* First make sure you are not in a virtual environment
* Then run `pip3 install .`
* If your Python packages are available on your `PATH` you should now be able to invoke `lights` from anywhere
