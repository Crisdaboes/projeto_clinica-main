Proyecto de Clínica para Programación para Internet 2
En qué consiste este proyecto:

Administrar médicos y especialidades y agendas
Crear una agenda para disponibilizar las consultas
Permitir al usuario elegir una consulta en día y horario de acuerdo con la agenda del médico.
Configurando el ambiente para ejecutar la aplicación web.
Descargue este repositorio:

shell
Copiar código
$ git clone git@github.com:Dan-Source/projeto_clinica.git
Cree una máquina virtual e instale las bibliotecas disponibles en el archivo requirements.txt:

Entre en la carpeta creada e inicie un ambiente virtual:

shell
Copiar código
$ cd projeto_clinica
$ python3 -m venv venv
Después debe activarlo con el siguiente comando:

shell
Copiar código
$ source ./venv/bin/activate
Una vez activado, instale las bibliotecas necesarias para ejecutar el proyecto:

ruby
Copiar código
 (venv)$ pip install -r requirements.txt
Para poder tener el primer acceso y configurar la aplicación, vamos a ejecutar el comando 'migrate' para generar la base de datos por defecto de Django (SQLite). Y después crear el superusuario:

shell
Copiar código
(venv)$ ./manage.py migrate
(venv)$ ./manage.py createsuperuser
Apodo/Usuario: admin
Correo electrónico: admin@mail.com
Contraseña: 
Contraseña (de nuevo):
Para iniciar el servidor después de este paso, debe:

shell
Copiar código
(venv)$ ./manage.py runserver
Para visualizar si todo está ejecutándose como se espera, vamos a acceder a la siguiente dirección:
http://localhost:8000/

O puede tener acceso al administrador de Django:
http://localhost:8000/admin

