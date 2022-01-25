Documentação dos componentes Bootstrap 
https://getbootstrap.com/docs/4.5/components/alerts/

Truques CSS
https://css-tricks.com/snippets/css/a-guide-to-flexbox/


https://imasters.com.br/desenvolvimento/conhecendo-o-jinja2-um-mecanismo-para-templates-no-flask



Auto Indent HTML
Ctrl + Alt + L


URL_FOR

 url_for('name of the function of the route','parameters (if required)')
 
 
 
 
 TODO:
 
 > página home para pessoas logadas, com uma lista de todos Seus pokemons cadastrados
 > Página de perfil da pessoa logada, com imagem, nome
 > Trocar para nas opções ter uma tela de procurar pokemon
 > Adicionar banco de dados  ok
 > Criar AUTH com mais segurança
 

 
 
 
 
Instalar psicopg windows
pip install --upgrade pip
 
http://www.stickpeople.com/projects/python/win-psycopg/


Requirements from pipenv
pipenv run pip freeze > requirements.txt


Push heroku master: 
git push heroku master

Logs Heroku:
heroku logs --tail



Guia Studio Ghibli

Página inicial > Imagens de todos os filmes e seus títulos

Pagina Inicial Logada > opção de clicar em um filme para olhar os detalhes do mesmo

Pagina de detalhamento de filme, pessoa pode colocar um depoimento, adicionar como favorito.

Página de perfil da pessoa, onde ela pode editar seu nome, foto e ver a lista de todos os depoimentos realizados.




Tabelas:

user:
- id, name, email, password, image


movie:
- id, imagem, titulo, description, year


testimony:
- id, message, id_user fk, id_movie fk


favorites:
- id, id_usrt fk, id_movie fk
