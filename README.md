## Consulta CNPJ via API do ReceitaWS
Este projeto é uma aplicação Python simples que permite ao usuário consultar informações básicas de empresas brasileiras através do CNPJ utilizando a API pública do ReceitaWS. O script faz uma requisição à API do ReceitaWS e apresenta os dados da empresa de forma simplificada, incluindo razão social, código da atividade principal, número, CEP, município e estado.

## Pré-requisitos
Para executar este projeto, você precisará ter o Python instalado em seu sistema. Este projeto foi testado com Python 3.12, mas deve ser compatível com outras versões que suportam as bibliotecas utilizadas.

## Clonar o Projeto
Para obter uma cópia local do projeto, você primeiro precisa cloná-lo do GitHub. Certifique-se de que você tem o Git instalado em seu sistema. Siga os passos abaixo para clonar o projeto:

1. Abra o terminal.
2. Navegue até o diretório onde deseja clonar o projeto.
3. Execute o comando de clone do Git:

```bash
git clone https://github.com/JoaoCardoso00/busca-cnpj.git
```

Após a conclusão do clone, navegue até o diretório do projeto:

```bash
cd busca-cnpj
```

## Configuração do Ambiente
Recomenda-se criar um ambiente virtual para instalar as dependências do projeto. Para criar e ativar um ambiente virtual, siga os passos abaixo:

1. Navegue até o diretório do projeto pelo terminal.
2. Execute o comando para criar o ambiente virtual:
 - Windows: `python -m venv venv`
 - macOS/Linux: `python3 -m venv venv`
3. Ative o ambiente virtual:
- Windows: `.\venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`
## Instalação de Dependências
Com o ambiente virtual ativado, instale a biblioteca necessária utilizando o pip:

```bash
pip install requests
```
ou
```bash
pip3 install requests
```

## Executando o Projeto
Para executar o projeto, siga os passos abaixo:

1. Certifique-se de que o ambiente virtual está ativado.
2. No diretório do projeto, execute o script consulta_cnpj.py com o comando:
- Windows: `python consulta_cnpj.py`
- macOS/Linux: `python3 consulta_cnpj.py`
3. Quando solicitado, insira o CNPJ que deseja consultar e pressione Enter.

O script fará uma consulta à API do ReceitaWS e exibirá os dados da empresa no formato JSON.

## Desativação do Ambiente Virtual
Quando terminar de usar o projeto, você pode desativar o ambiente virtual com o comando deactivate.

