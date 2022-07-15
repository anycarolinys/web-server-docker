# Servidor:  _Web Server em Python 2_

## _Any Caroliny Souza Silva_

 
__O servidor web utiliza o módulo socket do Python para receber requisições HTTP. Ao ser conectado por um cliente é retornado um arquivo HTML com uma mensagem de confirmação, o endereço e da porta do host conectado, além do código 200 de status de sucesso da requisição__.

__Para criar o contâiner com Dockerfile foram necessários os seguintes comandos:__
> docker build -t imagem-any .  
> docker run -d -p 22214:80 -it --rm --name container-any imagem-any  
> docker commit -a "Any Caroliny" -m "Servidor Web em Python 2" container-any container:1.0  

##  Porta do servidor:

> 22214

## Exemplo de uso:

> wget http://172.17.0.1:22214
