Importamos las bibliotecas necesarias: requests, json y os. Estas bibliotecas nos permiten realizar solicitudes HTTP, trabajar con archivos JSON y manipular el sistema de archivos.

Definimos la función obtener_informacion_pokemon(nombre_pokemon) para obtener la información del Pokémon desde la API. Esta función recibe el nombre del Pokémon como entrada.

Creamos la URL de la API utilizando el nombre del Pokémon proporcionado y lo convertimos a minúsculas para evitar errores de formato.

Realizamos una solicitud GET a la API utilizando la biblioteca requests y la URL que creamos. La respuesta de la API contiene los datos del Pokémon en formato JSON.

Verificamos si el código de respuesta de la solicitud es 404, lo cual indica que el Pokémon no fue encontrado. Si es así, retornamos None para indicar que no se encontró información del Pokémon.

Si la solicitud fue exitosa, convertimos la respuesta JSON en un diccionario utilizando el método json() de la respuesta. Luego, extraemos los datos relevantes del diccionario, como la URL de la imagen, peso, tamaño, movimientos, habilidades y tipos del Pokémon.

Creamos un diccionario llamado pokemon_info que contiene toda la información del Pokémon que hemos obtenido. Cada dato del Pokémon se almacena en una clave correspondiente en el diccionario.

Retornamos el diccionario pokemon_info con la información del Pokémon.

Definimos la función mostrar_informacion_pokemon(pokemon_info) que recibe como entrada el diccionario pokemon_info. Esta función se encarga de mostrar la información del Pokémon en la consola.

Verificamos si el diccionario pokemon_info es None, lo cual indica que el Pokémon no fue encontrado. En ese caso, mostramos un mensaje de error.

Si el Pokémon fue encontrado, mostramos la URL de la imagen, peso, tamaño, movimientos, habilidades y tipos del Pokémon utilizando la información almacenada en el diccionario pokemon_info.

Definimos la función guardar_info_pokemon(pokemon_info) que recibe como entrada el diccionario pokemon_info. Esta función se encarga de guardar la información del Pokémon en un archivo JSON.

Verificamos si la carpeta "pokedex" existe en el sistema de archivos. Si no existe, la creamos utilizando la función os.makedirs().

Construimos el nombre del archivo JSON utilizando el nombre del Pokémon en minúsculas y lo guardamos en la carpeta "pokedex". Abrimos el archivo en modo escritura y utilizamos la función json.dump() para escribir el diccionario pokemon_info en formato JSON en el archivo.

Definimos la función main() como el punto de entrada principal del programa.

Solicitamos al usuario que ingrese el nombre del Pokémon que desea buscar.

Llamamos a la función obtener_informacion_pokemon() para obtener la información del Pokémon basada en el nombre proporcionado.

Llamamos a la función mostrar_informacion_pokemon() para mostrar la información del Pokémon en la consola.

Llamamos a la función guardar_info_pokemon() para guardar la información del Pokémon en un archivo JSON.

Ejecutamos el programa llamando a la función main()
