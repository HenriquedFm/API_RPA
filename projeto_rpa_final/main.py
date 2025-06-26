from api_client import obter_piada
from database import criar_banco, inserir_dado
from processor import processar_texto
from email_sender import enviar_email

def main():
    print("📡 Coletando dados da API...")
    piada = obter_piada()
    print("✅ Piada recebida:", piada)

    print("🗃️ Criando banco de dados e inserindo dados...")
    criar_banco()
    inserir_dado(piada)

    print("🔍 Processando dados com regex...")
    palavras_ch = processar_texto(piada)
    print("✅ Palavras com 'ch':", palavras_ch)

    print("📧 Enviando e-mail com o relatório...")
    corpo = f'''
Relatório Final - Projeto RPA

Piada coletada:
{piada}

Palavras com 'ch' encontradas:
{', '.join(palavras_ch) if palavras_ch else 'Nenhuma'}
    '''
    enviar_email('aluno@teste.com', 'Relatório Chuck Norris', corpo)

if __name__ == '__main__':
    main()
