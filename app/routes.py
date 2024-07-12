from flask import render_template, request, current_app as app
from business import BusinessLogic
from datetime import datetime

# Define la ruta raíz y los métodos HTTP permitidos (GET y POST)
@app.route('/', methods=['GET', 'POST'])
def index():
    # Inicializa las variables para la fecha, error y tipo de cambio
    fecha = None
    error = None
    tipo_cambio = None
    
    
    if request.method == 'POST':

        # Obtiene la fecha del formulario
        fecha = request.form.get('fecha')
        # Instancia la lógica de negocio
        business_logic = BusinessLogic()

        try:
            # Convierte la fecha del formato de formulario a un objeto datetime
            fecha_obj = datetime.strptime(fecha, '%Y-%m-%d')
            # Formatea la fecha al formato 'dd/mm/yyyy' para la consulta
            fecha_formateada = fecha_obj.strftime('%d/%m/%Y')
            # Consulta el tipo de cambio utilizando la lógica de negocio
            tipo_cambio = business_logic.consultar_tipo_cambio(fecha_formateada)
            # Imprime el tipo de cambio en la consola (para depuración)
            print(tipo_cambio)

        except Exception as e:
            # Captura y almacena cualquier error ocurrido durante el proceso
            error = str(e)
    
    
    return render_template('index.html', error=error, fecha=fecha, tipo_cambio=tipo_cambio)

# Ejecuta la aplicación en modo depuración si este archivo se ejecuta directamente
if __name__ == '__main__':
    app.run(debug=True)
