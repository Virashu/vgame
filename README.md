<h1 align="center">PyGameTest (VGame)</h1>

<p align="center"><a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>


<p align="center">My try to build game engine on top of PyGame

This thing replicates Love2D<sup id="a1">[1](#f1)</sup>-like [interface](#how-to-use)

<br>

![cat](./.github/cat.webp)
<br>_funny silly cat (almost as this project😁)_


## How to install

### Using pip VCS features
```shell
python3 -m venv .env

pip install git+https://github.com/virashu/pygametest.git
```

### Manually
```shell
python3 -m venv .env

git clone https://github.com/virashu/pygametest.git
cd pygametest

pip install .
```

## How to use

Examples directory contains basic implementation.

Structure looks like this:

```python
from vgame import Scene, Runner

class MyGame(Scene):
    def load(self):
      # actions before game loads

    def update(self):
      # update loop
      # + delta time

    def draw(self):
      # draw loop
      # + graphics object

    def exit(self):
      # actions before exit


Runner.run(
    MyGame(width=800, height=600, framerate=120, tickrate=120, title="Game")
)

```

## TODO

- [x] Readme
- [x] Basic structure
- [x] Graphics
  - [x] Texture library
- [x] Backend
  - [x] Draw/update loops in separate threads
  - [x] Snapshots
  - [x] Snapshot synchronization
  - [x] PyGame sprite integration
  - [ ] Axis
  - [ ] Sounds
  - [ ] Event handling
  - [x] `stop` method

## Footnotes

<b id="f1">1</b> Love2D is an 2D game engine for lua available [here](https://love2d.org).
[↩](#a1)