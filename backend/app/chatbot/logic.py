import re
import random

def get_response(user_input):
    # La lógica completa de tu función de respuesta
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_message(split_message)
    if response == "":
        response = unknown()
    return {"response": response}

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):

    message_certainty = 0
    has_required_words = True
    
    for word in user_message:
        if word in recognized_words:
            message_certainty += 1
    
    percentage = float(message_certainty) / float(len(recognized_words)) if recognized_words else 0
    
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_message(message):

    highest_prob = {}

    def response(bot_response, list_of_words,  single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Definición de respuestas posibles con URL de gifs
    response(
    "¡Hola! Bienvenido a Motel Paraíso. ¿En qué puedo ayudarte hoy? 😊",
    ['hola', 'saludos', 'buenas', 'hola motel', 'motel', 'qué ofrecen'],
    single_response=True
    )

    response(
    "Ofrecemos habitaciones cómodas y privadas, perfectas para descansar o celebrar momentos especiales. ¿Quieres conocer las tarifas o servicios adicionales?",
    ['habitaciones', 'comodidad', 'servicios', 'qué ofrecen', 'comodidades'],
    single_response=True
    )

    response(
    "Contamos con habitaciones estándar, suites temáticas y premium. Todas incluyen parqueadero privado, Wi-Fi, TV por cable y servicio a la habitación. ¿Te interesa algún tipo en especial?",
    ['habitaciones', 'suite', 'premium', 'servicio', 'comodidades'],
    single_response=True
    )

    response(
    "Nuestras tarifas dependen del tipo de habitación y la duración de tu estadía. Por ejemplo, la habitación estándar comienza desde $XX por hora. ¿Deseas conocer más detalles?",
    ['tarifas', 'precios', 'costo', 'habitaciones', 'precio'],
    single_response=True
    )

    response(
    "Estamos ubicados en la Avenida Principal #123. Tenemos fácil acceso y parqueadero privado para tu comodidad. ¿Cómo planeas llegar?",
    ['ubicación', 'dónde están', 'dirección', 'parqueadero', 'queda'],
    single_response=True
    )

    response(
    "Por supuesto, nuestras habitaciones temáticas son ideales para una experiencia única. Algunas opciones incluyen habitaciones estilo tropical, románticas y de lujo. ¿Cuál te interesa?",
    ['temáticas', 'tematica', 'temas', 'habitaciones temáticas', 'especial'],
    single_response=True
    )

    response(
    "Tenemos promociones especiales para parejas. Por ejemplo, paquetes románticos que incluyen decoración, bebidas y más. ¿Quieres detalles?",
    ['promociones', 'descuentos', 'ofertas', 'paquetes'],
    single_response=True
    )

    response(
    "Sí, ofrecemos servicio a la habitación con un menú variado que incluye comidas, bebidas y snacks. ¿Te interesa algo en particular?",
    ['servicio', 'comida', 'bebidas', 'snacks', 'menú'],
    single_response=True
    )

    response(
    "Nuestras habitaciones son desinfectadas y acondicionadas después de cada uso. Priorizamos la limpieza y la comodidad para tu tranquilidad.",
    ['limpieza', 'higiene', 'seguridad', 'desinfección'],
    single_response=True
    )

    response(
    "Gracias por tu visita. ¡Esperamos verte pronto en Motel Paraíso! 😊",
    ['gracias', 'adios', 'nos vemos', 'chau'],
    single_response=True
    )

    
    best_match = max(highest_prob, key=highest_prob.get)
    return best_match if highest_prob[best_match] > 0 else ""


def unknown():
    responses = ['¿Puedes decirlo de nuevo?', 'No estoy seguro de lo que quieres decir.', 
                 'Por favor, intenta ser más específico.']
    return responses[random.randrange(len(responses))]
