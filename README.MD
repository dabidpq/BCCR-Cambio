# Proyecto de Consulta de Tipo de Cambio BCCR

Este proyecto es una aplicación web desarrollada con Flask que permite consultar el tipo de cambio de compra y venta del Banco Central de Costa Rica (BCCR) para una fecha específica, utilizando servicios web SOAP.

## Requisitos

- Python
- Flask
- zeep
- lxml

## Instalación y Configuración

1. **Clonar el repositorio:**

    
    git clone https://github.com/tu-usuario/proyecto-bccr.git
    cd proyecto-bccr
   

2. **Crear y activar un entorno virtual:**

  
    python -m venv venv
    venv\Scripts\activate  # Para Windows
   

## Ejecución de la Aplicación

1. **Ejecutar la aplicación:**

   
    desde run.py
   

2. **Abrir el navegador y navegar a:**

    ```
    http://127.0.0.1:5000
    ```

## Uso

1. Seleccione una fecha utilizando el formulario en la página principal.
2. Haga clic en "Consultar" para obtener los tipos de cambio de compra y venta para la fecha seleccionada.
3. Los resultados serán mostrados en la misma página.

## Arquitectura del Proyecto

El proyecto está estructurado en cuatro capas principales:

- **Presentación (Interfaz de Usuario):** Contiene los archivos HTML y CSS para la interfaz de usuario.
- **Negocio:** Contiene la lógica de negocio para procesar las solicitudes y respuestas del servicio web.
- **Acceso a Datos:** Contiene el código para realizar solicitudes al servicio web SOAP del BCCR.
- **Entidades:** Contiene las clases que representan los datos de tipo de cambio.

