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
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

AG_FILE=troposphere_ag.rst
IZ_FILE=troposphere_iz.rst

index:
	printf "troposphere modules a - g\n-------------------------\n\n" > $(AG_FILE)
	ls ../troposphere/[a-g]*.py | sed 's#../troposphere/\(.*\).py#\1#' | xargs printf ".. automodule:: troposphere.%s\n    :members:\n\n" >> $(AG_FILE)
	printf "troposphere modules i - z\n-------------------------\n\n" > $(IZ_FILE)
	ls ../troposphere/[h-z]*.py | sed 's#../troposphere/\(.*\).py#\1#' | xargs printf ".. automodule:: troposphere.%s\n    :members:\n\n" >> $(IZ_FILE)
