# NIX

Create an environment to run a python3 application.  

NOTES:

* The flake file has to be in the git index (committed or staged) before you can enter develop.

TODO:

* git
* code
* bashrc or zshrc

## Prereqs

Install Nix using determinate systems installer.  

REF: [github.com/chrisguest75/nix-examples/15_determinate_install/README.md](https://github.com/chrisguest75/nix-examples/blob/master/15_determinate_install/README.md)  

```sh
# check flakes are enabled
cat /etc/nix/nix.conf 
```

## Development (pure)

Open a pure shell and install packages

REF: [pipenv_pure/README.md](./pipenv_pure/README.md)

## Development (flake)

Open a flake and install packages

REF: [pipenv_flake/README.md](./pipenv_flake/README.md)

## Resources

* https://nixos.org/manual/nixpkgs/stable/#python
* https://gist.github.com/araa47/10537f74ee061b26e18ae21d4bfca7d9
* https://sid-kap.github.io/posts/2018-03-08-nix-pipenv.html
* https://github.com/nix-community/dream2nix
