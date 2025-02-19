# Dev Guideline

- select a unique name of the github repo considering the following domain
  - pypi
  - readthedocs
- login to pypi and generate a token
- create a virtual environment using pyenv
- install poetry and bumpversion in that env
  ```bash
  pyenv virtualenv 3.12.5 libozone_3.12.5
  curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
  add a package (dev dependency) use:  poetry add bumpversion --group dev
  ```

## How to update a feature

- first checkout to local `dev` branch.
- implement the feature
- check if all test cases are passed

## Build Site Doc

- add the git project to https://app.readthedocs.org/dashboard/
- while adding new modules, update mkdocs.yml file
- add .md files in docs/ folder
- check documentation in local env: `mkdocs build && mkdocs serve`
- To publish global: git commit and git push
    - site will be updated at https://libozone.readthedocs.io/

## Publish in Pypi

- make sure unit tests are running properly
    - `poetry run python -m unittest discover -s tests/`
- Update the version `bumpversion patch / major / minor`
    - it will auto commit to git
- build the whl file: `poetry build`
- set the token (onetime): `poetry config pypi-token.test-pypi <token>`
- publish to site: `poetry publish`
  - https://pypi.org/project/libozone/


## Others

- delete the content of the dist/ folder to save the space.
- to add a package (dev dependency) use `poetry add <package_name> --group dev`
