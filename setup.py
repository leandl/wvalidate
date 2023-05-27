from setuptools import find_packages, setup

with open("README.md", "r") as arq:
  readme = arq.read()

setup(
  name='wvalidate',
  version='0.0.1',
  license='MIT License',
  author='Leandro Crispim',
  long_description=readme,
  long_description_content_type="text/markdown",
  author_email='leandro.c25@aluno.ifsc.edu.br',
  keywords='validator',
  description=u'Simple data structure validator',
  packages=find_packages(),
  setup_requires=['pytest-runner'],
  tests_require=['pytest==4.4.1'],
  test_suite='tests'
)