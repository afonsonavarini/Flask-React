# CloudOpss

## Avaliação Técnica CloudOpss- Cadastro de Cliente com Back-end em Python com React como framework escolhido como preferência.

# Instalação

### 1. Instalar o virtualenv.

   OBS.: Acima do Python 3 o virtualenv já vem instalado por padrão, para versões abaixo seguir os seguintes pré-requisitos:
   
   #### Debian/Ubuntu: sudo apt install python-virtualenv
   #### CentOS/Fedora/Red Hat: sudo yum install python-virtualenv
   #### MacOS: sudo python2 -m pip install virtualenv
   #### Windows: py -2 -m pip install virtualenv
   
### 2. Dentro da pasta "api" abrir o terminal e digitar os seguintes comandos:

   #### Linux/MacOS: python3 -m venv <nome do ambiente>
   #### Windows: py -3 -m venv <nome do ambiente>
   OBS.: Seguir de acordo com as especificações encontradas no projeto.
  
### 3. Ativar o ambiente virtual:
  
  #### Linux/MacOS: . <nome do ambiente>/bin/activate
  #### Windows: <nome do ambiente>/Scripts/activate
  
 ### 4. Instalar o Flask e as demais dependências:
  
  #### pip install Flask
  
  #### pip install requests - Requisições ao Firebase.
  #### pip install flassger - Implementação do Swagger com Flask.
  #### pip install pyrebase4 - Executor do firebase em python.
  #### pip install pycryptodome - Necessário para que o pyrebase funcione corretamente.
  #### pip install logging - Criação de logs.
  
### 5. Execução do React.
  
  Abra o terminal na pasta "cliente" e execute o comando "npm start" para inicializar a aplicação em React.\
  OBS.: Ele irá instalar os pacotes necessários (node_modules).
  
# Importante
  
  1. Em "package.json" na pasta "cliente", ter certeza de possuir o seguintes critérios:\
      "proxy": "http://localhost:5000" \
      "react-scripts": "4.0.3"
  
  ### Exemplo:
      "name": "cliente",
      "version": "0.1.0",
      "private": true,
      "proxy": "http://localhost:5000",
      "dependencies": {
        "@testing-library/jest-dom": "^5.16.4",
        "@testing-library/react": "^13.3.0",
        "@testing-library/user-event": "^13.5.0",
        "axios": "^0.27.2",
        "firebase": "^9.8.3",
        "react": "^18.1.0",
        "react-dom": "^18.1.0",
        "react-scripts": "4.0.3",
        "web-vitals": "^2.1.4"
 
  2. No diretório: "api/Lib/site-packages" garantir que a pasta "Crypto" possua a primeira letra capitalizada.
  
  3. Em "server.py" na pasta "api" ajustar a variável "database" com o link do seu diretório do Realtime Database do Google Firebase.
  
  4. Em "server.py" na pasta "api" ajustar o dicionário "firebaseConfig" com o arquivo de configuração da aplicação do seu Storage do Google Firebase.
  
  5. (RECOMENDADO) Na aba "Regras" em seu Realtime Database e Storage do Google Firebase, recomenda-se manter da seguinte forma:
  
        rules_version = '2';\
        service firebase.storage {\
        match /b/{bucket}/o {\
          match /{allPaths=**} {\
            allow read, write\
            }\
        }\
      }
  
  # Considerações Finais:
  
  Em processo de desenvolvimento, o Git Flow, recurso pedido no desafio, corrompeu alguns arquivos do Back-end, sendo necessário que fosse refeito completamente.
  O Docker não foi implementado devido à configuração da máquina estar bloqueando acesso ao mesmo (problema em processo de resolução).
 
  Todas as funcionalidades especificadas no desafio foram cumpridas e se encontram presentes no projeto deste repositório.
  
  Dúvidas ou questionamentos, entrar em contato por:
  #### WhatsApp: (54) 99698-2868
  #### E-mail: afonsonavarini@hotmail.com
  #### LinkedIn: https://www.linkedin.com/in/afonsonavarini/
  
