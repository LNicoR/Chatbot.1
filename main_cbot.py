from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import re
import random

app = FastAPI()
# Configurar CORS para permitir el frontend (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://cbot-ui.onrender.com"],  # Cambia al dominio donde alojes el frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class UserInput(BaseModel):
    message: str

def get_response(user_input):
    """
    Procesa la entrada del usuario y devuelve una respuesta generada por el bot junto con un gif.
    
    Args:
    user_input (str): Mensaje del usuario.
    
    Returns:
    dict: Respuesta del bot y enlace del gif.
    """
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response, gif_url = check_all_message(split_message)
    return {"response": response, "gif_url": gif_url}

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    """
    Calcula la probabilidad de que un mensaje del usuario contenga palabras reconocidas.
    
    Args:
    user_message (list): Lista de palabras del mensaje del usuario.
    recognized_words (list): Palabras que el bot reconoce.
    single_response (bool): Indica si se debe dar una respuesta única.
    required_words (list): Lista de palabras requeridas para considerar el mensaje como válido.
    
    Returns:
    int: Probabilidad en porcentaje de que el mensaje coincida con la respuesta esperada.
    """
    message_certainty = 0
    has_required_words = True
    
    for word in user_message:
        if word in recognized_words:
            message_certainty += 1
    
    percentage = float(message_certainty) / float(len(recognized_words))
    
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_message(message):
    """
    Evalúa todas las posibles respuestas y devuelve la mejor coincidencia junto con el gif asociado.
    
    Args:
    message (list): Lista de palabras del mensaje del usuario.
    
    Returns:
    tuple: Respuesta del bot y enlace del gif.
    """
    highest_prob = {}

    def response(bot_response, list_of_words, gif_url=None, single_response=False, required_words=[]):
        """
        Agrega una respuesta y su probabilidad de coincidencia al diccionario de probabilidades.
        
        Args:
        bot_response (str): Respuesta del bot.
        list_of_words (list): Palabras reconocidas para esta respuesta.
        gif_url (str): URL de un gif relacionado con la respuesta.
        single_response (bool): Indica si se debe dar una respuesta única.
        required_words (list): Palabras requeridas para considerar la respuesta válida.
        """
        nonlocal highest_prob
        highest_prob[(bot_response, gif_url)] = message_probability(message, list_of_words, single_response, required_words)

    # Definición de respuestas posibles con URL de gifs
    response(
        "¡Hola! ¿En qué puedo ayudarte hoy?",
        ['hola', 'saludos', 'buenas', 'quehubo'],
        gif_url="https://tenor.com/es/view/giffany-gravity-falls-gif-sprite-book-of-bill-gif-6020263351307620049",
        single_response=True
    )
    response(
        "Aquí tienes nuestro enlace a la página web: https://example.com",
        ['pagina', 'web', 'enlace', 'sitio'],
        gif_url="https://tenor.com/es/view/giffany-gravity-falls-gif-sprite-book-of-bill-gif-12544109780257466418",
        single_response=True
    )
    response(
        "Estamos ubicados en la Avenida Calle 32 No. 17-30",
        ['direccion', 'ubicacion', 'donde'],
        gif_url="https://tenor.com/es/view/giffany-gravity-falls-gif-sprite-book-of-bill-gif-12544109780257466418",
        single_response=True
    )
    response(
        "Nuestro número de teléfono es: +57 123 456 7890",
        ['telefono', 'numero', 'contacto'],
        gif_url="https://tenor.com/es/view/giffany-gravity-falls-gif-sprite-book-of-bill-gif-12544109780257466418",
        single_response=True
    )
    response(
        "Gracias por tu visita. ¡Que tengas un gran día!",
        ['adios', 'gracias', 'nos vemos'],
        gif_url="https://tenor.com/es/view/giffany-gravity-falls-gif-sprite-book-of-bill-gif-12062962864236644735",
        single_response=True
    )
    
    best_match = max(highest_prob, key=highest_prob.get)
    response_text, gif_url = best_match
    return response_text, gif_url or ""

def unknown():
    """
    Devuelve una respuesta predeterminada cuando no hay coincidencia con el mensaje del usuario.
    
    Returns:
    str: Respuesta predeterminada del bot.
    """
    responses = ['¿Puedes decirlo de nuevo?', 'No estoy seguro de lo que quieres decir.', 
                 'Por favor, intenta ser más específico.']
    return responses[random.randrange(len(responses))]

@app.post("/chat")
async def chat(user_input: UserInput):
    return get_response(user_input.message)
