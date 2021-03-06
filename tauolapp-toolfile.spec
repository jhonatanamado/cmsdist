### RPM external tauolapp-toolfile 1.1.8
Requires: tauolapp
%prep

%build

%install

mkdir -p %i/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/tauolapp.xml
<tool name="tauolapp" version="@TOOL_VERSION@">
  <lib name="TauolaCxxInterface"/>
  <lib name="TauolaFortran"/>
  <lib name="TauolaTauSpinner"/>
  <lib name="TauolaHepMC"/>
  <lib name="TauolaHEPEVT"/>
  <client>
    <environment name="TAUOLAPP_BASE" default="@TOOL_ROOT@"/>
    <environment name="LIBDIR" default="$TAUOLAPP_BASE/lib"/>
    <environment name="INCLUDE" default="$TAUOLAPP_BASE/include"/>
  </client>
  <runtime name="ROOT_INCLUDE_PATH" value="$INCLUDE" type="path"/>
  <use name="root_cxxdefaults"/>
  <use name="hepmc"/>
  <use name="f77compiler"/>
  <use name="pythia8"/>
  <use name="lhapdf"/>
</tool>
EOF_TOOLFILE

## IMPORT scram-tools-post


