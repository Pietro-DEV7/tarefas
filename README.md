Esse projeto servirá para aprimorarmos nossa lógica de programação ao mesmo tempo em que 
explorarmos conceitos e técnica de programação back-end e fullstack. Vamos utilizar e desenvolver 
o conceito de MVC (Model-View-Controller), algumas particularidades de programação orientada a objetos, programação funcional, persistencia de dados (MySQL), microframework Flask e gerenciador 
de pacotes python (Astral UV).

Alguns passos iniciais para o projeto:

1. Caso não esteja instalado, prepare UV no seu OS:
``` bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

2. Faça a inicialização do projeto com o comando:
```bash 
UV init 
```

3. Crie ambiente virtual:
``` bash
uv venv
```

Ative o ambiente virtual:
```Bash
.\venv\Script\active.ps1
source .venv/script/active
source .venv/bin/active

4. Instalar o Flask 
```Bash
uv add flask
```

Será criado um arquivo uv.lock contendo as dependencias (requirimentos) e versões dos pacotes do
seu projeto.

5. Crie um arquivo app.py contendo o código inicial do projeto
```python

from flask import flask

app = flask(__nome__)

@app.route('/test')
def test()
    return 'Servidor online!'
```

6. Teste a aplicação iniciando o servidor do Flask
```Bash 
uv run flask run
```
