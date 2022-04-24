# Jupyter Book (Got these file from "Site" class repository Makefile)

html: 
	jupyter-book build .

conf.py: _config.yml _toc.yml
	jupyter-book config sphinx .

html-hub: conf.py
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	@echo "Start the Python http server and visit:"
	@echo "https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html"

# clean up the figures, audio and _build folders.
.PHONY: clean
clean:
	rm -rf figures/* audio/* _build/*

# Environment 
.PHONY : env
env :
	mamba env create -f environment.yml --name ligo
	conda activate ligo
	python -m ipykernel install --user --name ligo --display-name "LIGO Kernel"