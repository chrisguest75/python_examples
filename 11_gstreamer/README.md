# GSTREAMER

Demonstrate a simple `gstreamer` pipeline.  

## Start

```sh
export PIPENV_VENV_IN_PROJECT=1
# install
pipenv install --dev

# lint and test code
pipenv run lint
pipenv run test

# enter venv
pipenv shell

# run with arguments
pipenv run start --process
pipenv run start:test 

# process audio (it requires a full path)
pipenv run start --process --file file://$(pwd)/audio/LNL208.mp3 --samples 100
```

## Debugging and Troubleshooting

```sh
# enter python
pipenv run python

> import main

> main.test.__doc__
```

## Created

```sh
# install
pipenv install --dev flake8 flake8-bugbear flake8-2020 black
pipenv install --dev pytest 
pipenv install pyyaml python-json-logger python-dotenv
```

## Resources

* [google-coral/project-posenet/gstreamer.py](https://github.com/google-coral/project-posenet/blob/master/gstreamer.py)
* Python GStreamer Tutorial blog [here](https://brettviren.github.io/pygst-tutorial-org/pygst-tutorial.html#sec-5)
* Gstreamer in Python exits instantly, but is fine on command line [here](https://stackoverflow.com/questions/47879923/gstreamer-in-python-exits-instantly-but-is-fine-on-command-line)  
* How to install Gstreamer Python Bindings [here](https://lifestyletransfer.com/how-to-install-gstreamer-python-bindings/)

