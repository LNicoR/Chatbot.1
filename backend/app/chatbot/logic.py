import re
import random

def get_response(user_input):
    # La lógica completa de tu función de respuesta
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response, gif_url = check_all_message(split_message)
    return {"response": response, "gif_url": gif_url}

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    # Lógica completa de la función de probabilidad
    pass

def check_all_message(message):
    # Lógica completa de la función que verifica el mensaje
    pass

def unknown():
    responses = ['¿Puedes decirlo de nuevo?', 'No estoy seguro de lo que quieres decir.', 
                 'Por favor, intenta ser más específico.']
    return responses[random.randrange(len(responses))]
