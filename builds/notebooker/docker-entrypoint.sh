#!/bin/sh
set -e

##############
# Entrypoint
##############

# # fixes (not sure why is needed in alpine)
# touch /usr/local/lib/python3.7/site-packages/google/__init__.py

# configure extensions
jupyter contrib nbextension install --user
jupyter nbextension enable toc2/main
# rise slides
jupyter nbextension install rise --py --sys-prefix
jupyter nbextension enable rise --py --sys-prefix

# set password
echo "from notebook.auth import passwd" \
    > $JUPYTER_CONFIG_FILE
echo "c.NotebookApp.password = passwd('$NOTEBOOK_PASSWORD')" \
    >> $JUPYTER_CONFIG_FILE

# fix existing notebooks
jupyter trust *.ipynb

# run
jupyter notebook --no-browser --ip 0.0.0.0 --allow-root
