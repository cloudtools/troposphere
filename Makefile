.PHONY: spec test

PYDIRS=setup.py examples scripts tests troposphere

help: ## show this message
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%-30s %s\n" "target" "help" ; \
	printf "%-30s %s\n" "------" "----" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-30s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done

regen: CloudFormationResourceSpecification.json ## regenerates troposphere code
	./scripts/regen

fix: fix-black fix-isort ## run both fix-black and fix-isort

fix-black: ## automatically fix all black errors
	@black ${PYDIRS}

fix-isort: ## automatically fix all isort errors
	@isort ${PYDIRS}

clean:
	rm -rf ${p39dir} troposphere.egg-info

lint: lint-flake8 ## run all linters

lint-black: ## run black
	@echo "Running black... If this fails, run 'make fix-black' to resolve."
	@black ${PYDIRS} --check --color --diff
	@echo ""

lint-flake8: ## run flake8
	@echo "Running flake8..."
	@flake8 --version
	@flake8 --config=setup.cfg --show-source ${PYDIRS}
	@echo ""

lint-isort: ## run isort
	@echo "Running isort... If this fails, run 'make fix-isort' to resolve."
	@isort ${PYDIRS} --check-only
	@echo ""

release-test:
	python -m build --sdist --wheel .
	make release-test-39

p39dir=p39
release-test-39:
	@echo "Python 3.9 test"
	ver=`python -c 'import troposphere; print(troposphere.__version__)'` && \
	rm -rf ${p39dir} && \
	python3.9 -m venv ${p39dir} && \
	. ${p39dir}/bin/activate && \
	pip3.9 install dist/troposphere-$${ver}-py3-none-any.whl && \
	python -c 'import troposphere; print(troposphere.__version__)' && \
	deactivate && \
	rm -rf ${p39dir}

spec:
	curl -O https://d1uauaxba7bl26.cloudfront.net/latest/CloudFormationResourceSpecification.zip
	rm -rf spec
	mkdir spec
	unzip -d spec CloudFormationResourceSpecification.zip
	rm CloudFormationResourceSpecification.zip
	curl -O --compressed https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json
	SPECVERSION=$$(jq -r .ResourceSpecificationVersion CloudFormationResourceSpecification.json) && \
	/bin/echo "Downloaded version:" $${SPECVERSION} && \
	mkdir -p .backup && \
	ln -f CloudFormationResourceSpecification.json .backup/CloudFormationResourceSpecification_$${SPECVERSION}.json

test: ## run tests
	@python setup.py test
