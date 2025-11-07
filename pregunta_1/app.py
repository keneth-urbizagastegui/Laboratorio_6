from flask import Flask, render_template, request
import requests

# Instancia de la aplicación Flask
app = Flask(__name__)

# --- INICIO DE NUEVO CÓDIGO ---

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Ruta principal que maneja la búsqueda de Pokémon.
    - GET: Muestra el formulario de búsqueda.
    - POST: Procesa el formulario, llama a la API y muestra los resultados.
    """

    # Variable para almacenar los datos del Pokémon
    pokemon_data = None
    error_message = None

    # -----------------------------------------------------
    # Lógica para cuando el usuario ENVÍA el formulario
    # -----------------------------------------------------
    if request.method == 'POST':
        # 1. Obtener el nombre del Pokémon del formulario HTML
        pokemon_name = request.form['pokemon_name'].lower().strip()  # Usamos .lower() para evitar errores

        # 2. Construir la URL de la PokeAPI (corregido: sin comillas invertidas)
        api_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'

        # 3. Realizar la solicitud a la API
        try:
            response = requests.get(api_url, timeout=10)

            # 4. Procesar la respuesta
            if response.status_code == 200:
                # ¡Éxito! Pokémon encontrado.
                data = response.json()

                # 5. Extraer SÓLO los datos que necesitamos
                pokemon_data = {
                    'name': data['name'].capitalize(),
                    'types': [t['type']['name'] for t in data.get('types', [])],
                    'moves': [m['move']['name'] for m in data.get('moves', [])[:4]],  # Tomamos los primeros 4 movimientos
                    'sprites': {
                        'front_default': data['sprites'].get('front_default'),
                        'back_default': data['sprites'].get('back_default'),
                        'front_shiny': data['sprites'].get('front_shiny'),
                        'back_shiny': data['sprites'].get('back_shiny')
                    }
                }
            elif response.status_code == 404:
                # Error: Pokémon no encontrado
                error_message = f"¡Error! No se pudo encontrar el Pokémon: '{pokemon_name}'"
            else:
                # Otro error de la API
                error_message = f"¡Error! La API respondió con estado {response.status_code}."

        except requests.exceptions.RequestException as e:
            # Error de conexión
            error_message = f"Error de conexión a la API: {e}"

    # -----------------------------------------------------
    # Renderizar el template
    # -----------------------------------------------------
    # Esta línea se ejecuta en AMBOS casos (GET o POST)
    # - Si es GET: pokemon_data es None y se muestra solo el formulario
    # - Si es POST (con éxito): pokemon_data tiene datos y se muestran
    # - Si es POST (con error): error_message tiene un mensaje y se muestra
    return render_template('index.html', data=pokemon_data, error=error_message)


# -----------------------------------------------------
# Código para ejecutar la aplicación
# -----------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)

# --- FIN DE NUEVO CÓDIGO ---