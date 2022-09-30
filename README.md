# Template for GitHub actions for DevOps

![Python package](https://github.com/miguelcifuentes/myfirstpypi/workflows/Python%20package/badge.svg)
![Upload Python Package](https://github.com/miguelcifuentes/myfirstpypi/workflows/Upload%20Python%20Package/badge.svg)

The related software just print `Hello World!`. To avoid conflicts with the package name, we use the Spanish translation _DesOper_

## Install
```bash
pip install -i https://test.pypi.org/simple/ myfirstpypi
```
## USAGE
```python
>>> from desoper import hello
>>> hello.hello()
Hello World!
```
