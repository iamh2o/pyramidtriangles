# Pyramid Triangles

Codebase to drive pyramid triangle art.

![Build
Status](https://travis-ci.com/pyramidscheme/pyramidtriangles.svg?branch=master)

## Requirements

* [Python 3](https://www.python.org), [poetry](https://poetry.eustace.io/)

```sh

# Install Python 3 (any method will do)
## Ideally, use a virtual env
virtualenv --python=python3 ve
...
source ve/bin/activate

.. or ..

brew install python
export PATH="$(brew --prefix python)/libexec/bin:${PATH}"

# Install Poetry
curl -fsSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# Install dependencies
poetry install  (if using a ve, source ve/bin/activate first)
```

* [Processing 2.2.1+](https://www.processing.org) (for simulator only)

## Getting Started

First, check out the repository:

    git clone git@github.com:pyramidscheme/pyramidtriangles.git

The simulator lives in the `Simulators/TriangleSimulator/` directory.  Open the file `TriangleSimulator.pde` in
Processing, and run it.

To start the lighting software talking to the simulator:

    poetry run python go_tri.py --simulator   (or if you are running a ve, python go_tri.py --simulator)

You can also specify which show to run by using the name of the show:

    poetry run python go_tri.py --simulator UpDown (or if you are running a ve, python go_tri.py --simulator UpDown)

You can also choose which show is running through the web interface:

[http://localhost:9990/](http://localhost:9990/)

## Writing Shows

See the files in `doc/`

## OSC Control

Lighting can be controlled wirelessly over OSC. We're using [TouchOSC](http://hexler.net/software/touchosc), which is
available for [iOS](https://itunes.apple.com/app/touchosc/id288120394) and
[Android](https://play.google.com/store/apps/details?id=net.hexler.touchosc_a).  (It costs $4.99, but it's worth it,
we promise!)

You'll need to install the app on your phone or tablet, then install a layout.

	1. Download the TouchOSC Editor from the TouchOSC page (scroll down to 'Downloads') 
	2. Open the show control layout from the baaahs repository (misc/ShowControl.touchosc)
	3. Click 'Sync' in the TouchOSC Editor menubar and follow the on-screen instructions

For more details on controlling shows with OSC, check the 'doc' directory in this repository.

## Hardware Support

Communicating with the hardware requires [OLA.](https://www.openlighting.org/ola/)

OS X:

    brew install ola

Debian / Ubuntu:

    sudo apt-get install ola ola-python ola-rdm-tests

## History

Credit to Mostly Greg Brown, and a bit to JEM for writing the original codebase on which we are building.  That was
the [BAAAHS panel controlling s/w](https://bitbucket.org/grgbrn/baaahs2014/src/default/)

## Actually Running The Thing w/ DMXking LeDMX4pro

-2)Connect your DMX4pro to a network that looks like it's configured network (console does not seem to be able to re-set the IP).  192.168.0.*, 255.255.255.0, 192.168.0.254
-1)Power the DMX4pro on
0) ping it to see if it is visible to your network
1) source your ve
2) start ola daemon ('olad').  This should start a server who has a UI you can access at localhost:9090
3)go to localhost:9090
4)click 'add universe', give it universe #0 and any name you like.
5)Add the 'Device' ArtNet [IP] Artnet Universe 0:0:0 Direction  == OUTPUT
6) Save
7) from sourced ve, type python ./go_led.py
8)Open DMX4pro condiguration tool.  You should be able to see the OLA artnet and the DMX4pro.
9)From localhost:9090 (OMG! There is a much better 'new ola UI' which you can access by clicking the tiny link to it at the obttomo of this page that loads for localhost:9090), click on your universe.  The DMX Monitor tab shows you IRT what DMX is being sent. DMX Console lets you manually send DMX to every channel.
10) IF you have cherrypy installed, you can go to the simple web interface that should have started on localhost:9990. you can shoose shows, set cycle interval,etc.
11) simulator possibly coming!
