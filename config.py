from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do Flask
FLASK_ENV = os.getenv('FLASK_ENV')
SECRET_KEY = os.getenv('SECRET_KEY')

# Configurações do Banco de Dados
DB_NAME = os.getenv('DB_NAME')
DB_PATH = os.getenv('DB_PATH')

# Outras configurações específicas do projeto
QUALQUER_VARIAVEL = os.getenv('QUALQUER_VARIAVEL')
