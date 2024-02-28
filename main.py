import requests
import re

def validar_cnpj(cnpj):
    # Remove caracteres não numéricos
    cnpj = re.sub('[^0-9]', '', cnpj)
    padrao_cnpj_regex = r'\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}'

    return re.match(padrao_cnpj_regex, cnpj)

def consultar_cnpj(cnpj):
    if not validar_cnpj(cnpj):
        return "CNPJ inválido. Por favor, insira um CNPJ no formato correto."

    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'status' in data and data['status'] == 'ERROR':
                return "CNPJ não localizado na API."
            else:
                resultado = {
                    "razao_social": data['nome'],
                    "codigo_atividade_principal": data['atividade_principal'][0]['code'],
                    "endereco": {
                        "numero": data['numero'],
                        "cep": data['cep'],
                        "municipio": data['municipio'],
                        "estado": data['uf'],
                    }
                }
                return resultado
        else:
            return f"Erro ao fazer a requisição: Status code {response.status_code}"
    except Exception as e:
        return f"Erro ao consultar o CNPJ: {str(e)}"

if __name__ == "__main__":
    cnpj_input = input("Digite o CNPJ da empresa: ")
    resultado = consultar_cnpj(cnpj_input)
    print(resultado)
