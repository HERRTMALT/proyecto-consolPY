# juan cruzardo

- codificacion de la visualizacion  de datos con pandas
- coneccion con la base de datos con mysql.connector

---

# pedro

- diagramacion en pseint del proyecto para mostrar en clase y explicacion

---

# gennaro y rulo

- desarrollo de las funciones def, condicionales y bucles que se vallan a utilizar.

---

## comandos de git utiles para hacer el proyecto

- Instalacion:
	1. Descargar Git desde https://git-scm.com/downloads.
	2. Instalarlo dejando las opciones que aparecen por defecto.
	3. buscar una nueva aplicacion llamada "git bash"

- Configuracion inicial (solo una vez):
	```bash
	git config --global user.name "Tu nombre"
	git config --global user.email "tu-correo@example.com"
 	"git config --global core.editor "code --wait""
 	"git config --global init.defaultBranch main"
 	"git config --global color.ui auto"
 	"git config --global pull.rebase false"
	```

- Comandos principales:
	```bash
	git clone URL_DEL_REPOSITORIO   # Descargar el proyecto
	git remote -v                   # Ver el repositorio conectado
	git add .                       # Preparar todos los cambios
	git commit -m "Describe el cambio"  # Guardar los cambios
	git commit -a -m "Describe el cambio" # Atajo para archivos ya registrados
	git push                        # Subir los cambios a GitHub
	```

- Flujo normal de trabajo:
	```bash
	git add .
	git commit -m "Mi cambio"
	git push
	```

 ---

 ## Instalacion de los modulos de Python

1. Abrir la terminal de VS Code con `Ctrl + Ñ`.
2. Comprobar que Python esta instalado:

	```bash
	python --version
	```

	Si aparece la version de Python, continuar. Si aparece un error, descargar Python desde https://www.python.org/downloads/ y durante la instalacion marcar la opcion **Add Python to PATH**.

3. Comprobar que `pip` esta instalado:

	```bash
	python -m pip --version
	```

4. Instalar los modulos `pandas` y `mysql-connector-python`:

	```bash
	python -m pip install pandas mysql-connector-python
	```

5. Comprobar que los modulos funcionan correctamente:

	```bash
	python -c "import pandas; import mysql.connector; print('Modulos instalados correctamente')"
	```

Si `pip` no funciona, ejecutar primero:

```bash
python -m ensurepip --upgrade
```
