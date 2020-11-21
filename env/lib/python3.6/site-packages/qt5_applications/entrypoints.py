import functools
import os
import subprocess
import sys

import qt5_applications


fspath = getattr(os, 'fspath', str)


def run(application_name, environment=os.environ):
    modified_environment = qt5_applications.create_environment(reference=environment)
    application_path = qt5_applications.application_path(application_name)

    completed_process = subprocess.run(
        [
            fspath(application_path),
            *sys.argv[1:],
        ],
        env=modified_environment,
    )

    sys.exit(completed_process.returncode)


# designer = functools.partial(run, application_name='designer')

# ----  start of generated wrapper entry points

assistant = functools.partial(run, application_name='assistant')
canbusutil = functools.partial(run, application_name='canbusutil')
designer = functools.partial(run, application_name='designer')
lconvert = functools.partial(run, application_name='lconvert')
licheck64 = functools.partial(run, application_name='licheck64')
linguist = functools.partial(run, application_name='linguist')
lprodump = functools.partial(run, application_name='lprodump')
lrelease = functools.partial(run, application_name='lrelease')
lrelease_pro = functools.partial(run, application_name='lrelease-pro')
lupdate = functools.partial(run, application_name='lupdate')
lupdate_pro = functools.partial(run, application_name='lupdate-pro')
moc = functools.partial(run, application_name='moc')
pixeltool = functools.partial(run, application_name='pixeltool')
qcollectiongenerator = functools.partial(run, application_name='qcollectiongenerator')
qdbus = functools.partial(run, application_name='qdbus')
qdbuscpp2xml = functools.partial(run, application_name='qdbuscpp2xml')
qdbusviewer = functools.partial(run, application_name='qdbusviewer')
qdbusxml2cpp = functools.partial(run, application_name='qdbusxml2cpp')
qdistancefieldgenerator = functools.partial(run, application_name='qdistancefieldgenerator')
qdoc = functools.partial(run, application_name='qdoc')
qgltf = functools.partial(run, application_name='qgltf')
qhelpgenerator = functools.partial(run, application_name='qhelpgenerator')
qlalr = functools.partial(run, application_name='qlalr')
qmake = functools.partial(run, application_name='qmake')
qml = functools.partial(run, application_name='qml')
qmlcachegen = functools.partial(run, application_name='qmlcachegen')
qmleasing = functools.partial(run, application_name='qmleasing')
qmlformat = functools.partial(run, application_name='qmlformat')
qmlimportscanner = functools.partial(run, application_name='qmlimportscanner')
qmllint = functools.partial(run, application_name='qmllint')
qmlmin = functools.partial(run, application_name='qmlmin')
qmlplugindump = functools.partial(run, application_name='qmlplugindump')
qmlpreview = functools.partial(run, application_name='qmlpreview')
qmlprofiler = functools.partial(run, application_name='qmlprofiler')
qmlscene = functools.partial(run, application_name='qmlscene')
qmltestrunner = functools.partial(run, application_name='qmltestrunner')
qmltyperegistrar = functools.partial(run, application_name='qmltyperegistrar')
qscxmlc = functools.partial(run, application_name='qscxmlc')
qtattributionsscanner = functools.partial(run, application_name='qtattributionsscanner')
qtdiag = functools.partial(run, application_name='qtdiag')
qtpaths = functools.partial(run, application_name='qtpaths')
qtplugininfo = functools.partial(run, application_name='qtplugininfo')
qtwaylandscanner = functools.partial(run, application_name='qtwaylandscanner')
qvkgen = functools.partial(run, application_name='qvkgen')
rcc = functools.partial(run, application_name='rcc')
repc = functools.partial(run, application_name='repc')
sdpscanner = functools.partial(run, application_name='sdpscanner')
tracegen = functools.partial(run, application_name='tracegen')
uic = functools.partial(run, application_name='uic')
xmlpatterns = functools.partial(run, application_name='xmlpatterns')
xmlpatternsvalidator = functools.partial(run, application_name='xmlpatternsvalidator')

# ----  end of generated wrapper entry points

