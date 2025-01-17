# flake.nix
{
    description = "A flake for developing with python 3.11.8";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = {nixpkgs, ...}: let
    system = "x86_64-linux";
    #       ↑ Swap it for your system if needed
    #       "aarch64-linux" / "x86_64-darwin" / "aarch64-darwin"
    pkgs = nixpkgs.legacyPackages.${system};
  in {
    devShells.${system}.default = pkgs.mkShell {

      packages = [ 
          pkgs.python311Full 
          pkgs.python311Packages.pip 
          pkgs.python311Packages.cmake
          pkgs.python311Packages.pycairo
          pkgs.pipenv 
          pkgs.cairo
          pkgs.pkg-config
          pkgs.gobject-introspection
          pkgs.gst_all_1.gstreamer
          pkgs.gst_all_1.gst-plugins-good
          pkgs.gst_all_1.gst-plugins-ugly
          pkgs.gst_all_1.gst-plugins-bad
          pkgs.gst_all_1.gst-plugins-base
       ];

      env = {
        PIPENV_IGNORE_VIRTUALENVS=1;
        PIPENV_VENV_IN_PROJECT=1;
        NIX_LD_LIBRARY_PATH = pkgs.lib.strings.makeLibraryPath [
          pkgs.stdenv.cc.cc
        ];
        NIX_LD = pkgs.lib.fileContents "${pkgs.stdenv.cc}/nix-support/dynamic-linker";
      };

      shellHook = ''
        echo "***************************************************"
        echo "*** Welcome to python"
        echo "***************************************************"
        echo ""
        python --version
      '';       
    };
  };
}
