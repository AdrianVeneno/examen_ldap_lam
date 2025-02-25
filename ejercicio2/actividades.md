https://aulasoftwarelibre.github.io/taller-de-docker/docker-compose/#docker-compose
docker run -d --name ejercicio2-martibd-1 -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=wordpress -e MYSQL_USER=manager -e MYSQL_PASSWORD=secret mariadb:10
docker run -d --name wordpress --link ejercicio2-martibd-1:db -p 8080:80 -e WORDPRESS_DB_HOST=db -e WORDPRESS_DB_NAME=wordpress -e WORDPRESS_DB_USER=manager -e WORDPRESS_DB_PASSWORD=secret wordpress:6

