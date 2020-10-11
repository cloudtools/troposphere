# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	touch ../examples/__init__.py
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	rm -rf ../examples/__init__.py

index:
	# sphinx-apidoc won't overwrite existing files, so remove them first
	rm -rf ./apis

	# sphinx-apidoc won't generate a package without a __init__ file
	#     however, the troposphere tests fail if there is a __init__ file
	#     so, create the file, create the docs and then remove __init__.py
	# sleep is there to ensure the system has time to place the file
	#     before sphinx-apidoc is run
	touch ../examples/__init__.py
	sphinx-apidoc -o ./apis ../examples --tocfile examples_toc
	sphinx-apidoc -o ./apis ../troposphere --tocfile troposphere_toc
	sphinx-apidoc -o ./apis ../tests --tocfile tests_toc
	rm -rf ../examples/__init__.py
