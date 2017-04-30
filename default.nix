{ pkgs ? import <nixpkgs> {}
, todo ? ./.
}:

{
  todo = pkgs.pythonPackages.buildPythonPackage {
    name = "todo";
    src = todo;
    buildInputs = with pkgs.pythonPackages ;[
    pyramid
    pytest
    pyramid_tm
    webtest
    zope_sqlalchemy
    transaction
    cornice
    ];
  };
}
