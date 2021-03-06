{ buildPythonApplication, fetchPypi, pandas, pyyaml, click, appdirs }:
let
in buildPythonApplication rec {
  pname = "freilanz";
  version = "0.1.0";
  src = ./..;
  propagatedBuildInputs = [ pandas pyyaml click ];
  doCheck = false;
}
