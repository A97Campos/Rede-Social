Como utilizar 
 - No terminal:
      -docker-compose up -d --build;
      -docker-compose exec web python manage.py migrate;
      -docker-compose exec web python manage.py collectstatic --no-input.
  - Abra o navegador e vá para `http://127.0.0.1:8000/` para ver a aplicação em execução.
