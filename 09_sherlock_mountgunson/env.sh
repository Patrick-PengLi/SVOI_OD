# Sourced by every script here: load the SAME python module the environment was built with, then activate it.
# The venv's python links to this module's libpython, so the module must be loaded first, in every shell and job.
PYMOD=python/3.12.1          # edit if module spider python shows a different 3.10+ version
ml purge >/dev/null 2>&1
ml $PYMOD
