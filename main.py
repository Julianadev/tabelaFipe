import requests
import pandas as pd

def tabela_fipe(codigoFipe):
    try:
        url = f'https://brasilapi.com.br/api/fipe/preco/v1/{codigoFipe}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return f'Erro na solicitação da API: {response.status_code}, {response.text}'
    except ConnectionError as e:
        return f'Ocorreu um erro na solicitação da API: {e}'

def salvando_excel(results):
    try:
        nome_arquivo = input('Digite um nome para o arquivo: ').strip()
        if nome_arquivo:
            if not nome_arquivo.endswith('.xlsx'):
                nome_arquivo += '.xlsx'

            df = pd.DataFrame(results)
            df.to_excel(nome_arquivo, index=False)
            print(f'Arquivo {nome_arquivo} foi salvo com sucesso!')
        else:
            print('Digite um nome para o arquivo')
    except Exception as e:
        print(f'Erro no arquivo: {e}')

def main():
    try:
        codigoFipe = input('Digite o código Fipe: ')
        response_content = tabela_fipe(codigoFipe)
        if 'erro' in response_content:
            print(f'Erro: {response_content["erro"]}')
        else:
            results = []

            for key in response_content:
                valor = key.get('valor', '')
                marca = key.get('marca', '')
                modelo = key.get('modelo', '')
                anoModelo = key.get('anoModelo', '')
                combustivel = key.get('combustivel', '')
                codigoFipe = key.get('codigoFipe', '')
                mesReferencia = key.get('mesReferencia', '')
                tipoVeiculo = key.get('tipoVeiculo', '')
                siglaCombustivel = key.get('siglaCombustivel', '')
                dataConsulta = key.get('dataConsulta', '')

                result = {
                    'valor': valor,
                    'marca': marca,
                    'modelo': modelo,
                    'anoModelo': anoModelo,
                    'combustivel': combustivel,
                    'codigoFipe': codigoFipe,
                    'mesReferencia': mesReferencia,
                    'tipoVeiculo': tipoVeiculo,
                    'siglaCombustivel': siglaCombustivel,
                    'dataConsulta': dataConsulta
                }

                results.append(result)

            print(results)

        salvar = input('Deseja salvar o resultado? S/N ')
        if salvar.upper() == 'S':
            salvando_excel(results)
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

if __name__ == "__main__":
    main()
