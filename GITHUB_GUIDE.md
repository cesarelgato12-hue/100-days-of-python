# Guía rápida para subir el proyecto a GitHub

## 1. Abre la carpeta en Visual Studio Code

Selecciona:

`File → Open Folder`

y abre la carpeta `100-days-of-python`.

## 2. Abre la terminal

Selecciona:

`Terminal → New Terminal`

## 3. Inicializa Git

```bash
git init
```

## 4. Guarda el primer cambio

```bash
git add .
git commit -m "Inicio del reto 100 Days of Code"
```

## 5. Conecta el repositorio de GitHub

Crea en GitHub un repositorio vacío llamado:

`100-days-of-python`

Después copia la dirección del repositorio y ejecuta:

```bash
git branch -M main
git remote add origin URL_DE_TU_REPOSITORIO
git push -u origin main
```

## Flujo para los siguientes días

```bash
git add .
git commit -m "Day 2: nombre del proyecto"
git push
```

## Antes de subir

Comprueba que no tenga:

- Contraseñas.
- Tokens.
- Claves API.
- Archivos `.env`.
- Material privado del curso.
