{
  description = "cel-in-py";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
    nixdoc.url = "github:nix-community/nixdoc";
  };

  outputs = { self, nixpkgs, flake-parts, ... }@inputs:
    flake-parts.lib.mkFlake { inherit inputs; }
      {
        systems = [
          "x86_64-linux"
        ];

        flake = { };

        perSystem = { config, self', inputs', pkgs, system, ... }:
          let

            py = pkgs.python3.withPackages (p: with p; [
              antlr4-python3-runtime
              cookiecutter
              pytest
              debugpy
            ]);
            
            antlr4 = pkgs.antlr4;

          in
          {
            devShells.default = pkgs.mkShell {
              nativeBuildInputs = [
                antlr4
                py
                pkgs.tree
              ];

              shellHook = ''
                export PYTHONPATH=$PYTHONPATH:$antlr4/lib/python3.8/site-packages
              '';
            };

            packages = {
              default = py;
            };
          };
      };
}
