#### Como executar a aplicação web:
1. Clone esse repositório.

  `git clone https://github.com/fabriciocovalesci/tcc_predict_crypto.git`
  
2. Acesse a pasta **web**
3. Crie um virtualenv com Python 3. 

  `python3 -m venv .web`

4. Ative o virtualenv

  `OS Linux: source .web/bin/activate`                                
  `OS Windows: .web/Scripts/active`

5. Instale todas dependências do arquivo requirements.txt

  `pip3 install -r  requirements.txt`

6. Crie um arquivo **.env**  e adicione o conteudo que contém no arquivo de exemplo **env-example**

7. Execute a aplicação com o comando:

  `flask run`
