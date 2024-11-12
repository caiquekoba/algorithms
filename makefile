environment_name = algorithms

.PHONY: create_environment requirements.txt

requirements.txt: requirements/requirements.in
	pip-compile --upgrade requirements/requirements.in
# The --upgrade option here causes it to check PyPI for the maximum version of each package that matches the lines in requirements.in - without this it may settle for packages that are currently in your local cache.

create_algorithms_environment: environment_creation.yml
	conda env create --file environment_creation.yml
	
update_algorithms_environment: environment_update.yml
	conda env update --file environment_update.yml --prune 
# The --prune option removes any packages from the environment that are not listed in the .yml file. This ensures that your environment matches the .yml file exactly.

delete_algorithms_environment:
	conda remove --name ${environment_name} --all
# The --all flag removes all the packages installed in that environment.