import re
import random

def get_response(user_input):
    # La lógica completa de tu función de respuesta
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response, gif_url = check_all_message(split_message)
    return {"response": response}

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
        nonlocal highest_prob
        highest_prob[(bot_response, gif_url)] = message_probability(message, list_of_words, single_response, required_words)

    # Definición de respuestas posibles con URL de gifs
    response(
        "¡Hola! ¿En qué puedo ayudarte hoy?",
        ['hola', 'saludos', 'buenas'],
        single_response=True
    )
    response(
        "Tenemos excelentes profesores en la institución pero Andrea Huertas es la mejor",
        ['quien', 'quién', 'mejor', 'profesor', 'profesora'],
        single_response=True
    )
    response(
        "Nuestras facultades son: Facultad de Ingeniería, Escuela de Negocios y la Facultad de Ciencias Sociales y de la Educación, ¿Sobre cuál quieres conocer los programas?",
        ['facultades'],
        single_response=True
    )
    response(
        "La facultad de Ingeniería, cuenta con las siguientes programas: Ingeniería Multimedia (Pregrado-Bogotá), Ciencia de datos (Pregrado-Bogotá y Virtual), Ingeniería Industrial (Pregrado-Bogotá), Ingeniería de Telecomunicaciones (Pregrado-Bogotá y Meta), Ingeniería de Sistemas (Pregrado-Bogotá, Meta y Virtual), Ingeniería de Software (Pregrado-Bogotá y Virtual)",
        ['facultad', 'ingeniería','ingenieria', 'carreras', 'programas'],
        single_response=True
    )
    response(
        "La Escuela de Negocios, cuenta con los siguientes programas: Administración Financiera (Pregrado-Bogotá y Virtual), Contaduría Pública (Pregrado-Bogotá, Meta y Virtual), Finanzas y Negocios Internacionales (Pregrado-Bogotá y Virtual), Administración de Empresas (Pregrado-Bogotá y Virtual), Profesional en Negocios y Logística Internacional (Pregrado-Bogotá y Virtual), Administración de Servicios de Salud (Pregrado-Bogotá), Mercadeo y Publicidad (Pregrado-Bogotá y Virtual), Administración en Salud (Pregrado-Virtual)",
        ['facultad', 'escuela', 'negocios' , 'carreras', 'programas'],
        single_response=True
    )
    response(
        "La Facultad de Ciencias Sociales y de la Educación, cuenta con los siguientes programas: Licenciatura en Bilingüismo con Énfasis en Inglés (Pregrado-Bogotá y Meta), Licenciatura en Educación Infantil (Pregrado-Bogotá y Meta), Profesional en Lenguas (Pregrado-Bogotá y Virtual), Profesional en Deporte y Actividad Física (Pregrado-Bogotá), Diseño Visual (Pregrado-Bogotá y Virtual), Comunicación Social (Pregrado-Bogotá)",
        ['facultad', 'ciencias', 'sociales' , 'educación', 'carreras','programas'],
        single_response=True
    )
    response(
        "Tenemos diferentes programas ¿Cuál es de tu interés (pregrado/postgrado)?",
        ['programas', 'carreras'],
        single_response=True
    )
    response(
        "Nuestros programas de pregrado son: Ingeniería Multimedia (Pregrado-Bogotá), Ciencia de datos (Pregrado-Bogotá y Virtual), Ingeniería Industrial (Pregrado-Bogotá), Ingeniería de Telecomunicaciones (Pregrado-Bogotá y Meta), Ingeniería de Sistemas (Pregrado-Bogotá, Meta y Virtual), Ingeniería de Software (Pregrado-Bogotá y Virtual), Administración Financiera (Pregrado-Bogotá y Virtual), Contaduría Pública (Pregrado-Bogotá, Meta y Virtual), Finanzas y Negocios Internacionales (Pregrado-Bogotá y Virtual), Administración de Empresas (Pregrado-Bogotá y Virtual), Profesional en Negocios y Logística Internacional (Pregrado-Bogotá y Virtual), Administración de Servicios de Salud (Pregrado-Bogotá), Mercadeo y Publicidad (Pregrado-Bogotá y Virtual), Administración en Salud (Pregrado-Virtual), Licenciatura en Bilingüismo con Énfasis en Inglés (Pregrado-Bogotá y Meta), Licenciatura en Educación Infantil (Pregrado-Bogotá y Meta), Profesional en Lenguas (Pregrado-Bogotá y Virtual), Profesional en Deporte y Actividad Física (Pregrado-Bogotá), Diseño Visual (Pregrado-Bogotá y Virtual), Comunicación Social (Pregrado-Bogotá)",
        ['pregrado', 'carreras', 'programas'],
        single_response=True
    )
    response(
        "Tenemos diferentes programas de pregrado y postgrado en nuestras modalidades. ¿En qué modalidad estás interesado?",
        ['postgrado', 'carreras', 'programas'],
        single_response=True
    )
    response(
        "Aquí tienes nuestro enlace a la página web: https://ucompensar.edu.co/",
        ['pagina', 'web', 'enlace', 'sitio'],
        gif_url="https://tenor.com/es/view/giffany-gravity-falls-gif-sprite-book-of-bill-gif-12544109780257466418",
        single_response=True
    )
    response(
        "Contamos con sedes en Bogotá, Villavicencio y Formación virtual. ¿En cuél tienes interés?",
        ['sedes', 'dirección'],
        gif_url="https://tenor.com/es/view/giffany-gravity-falls-gif-sprite-book-of-bill-gif-12544109780257466418",
        single_response=True
    )
    response(
        "Nuestra sede Teusaquillo en Bogotá, se encuentra ubicada en Avenida (Calle) 32 No. 17-30. Teléfono aspirantes: 601 3380666. WhatsApp: (+57) 3173002952",
        ['bogotá', 'sede', 'dirección'],
        gif_url="https://tenor.com/es/view/giffany-gravity-falls-gif-sprite-book-of-bill-gif-12544109780257466418",
        single_response=True
    )
    response(
        "Puedes estudiar en nuestra sede virtual. Línea nacional: 01 8000 110 666. Correo: aspirantes@ucompensar.edu.co. WhatsApp: (+57) 3173002952",
        ['virtual', 'línea', 'correo'],
        gif_url="https://tenor.com/es/view/giffany-gravity-falls-gif-sprite-book-of-bill-gif-12544109780257466418",
        single_response=True
    )
    response(
        "La Sede en Meta está ubicada en Sede Educación Cofrem, Carrera 35 No. 20A – 02, Villavicencio. Teléfono: 608 6818640. WhatsApp: (+57) 3173002952",
        ['meta', 'villavicencio', 'sede', 'dirección'],
        gif_url="https://tenor.com/es/view/giffany-gravity-falls-gif-sprite-book-of-bill-gif-12544109780257466418",
        single_response=True
    )
    response(
        "Para el resto del país, puedes comunicarte al teléfono nacional 01 8000 110 666.",
        ['país', 'teléfono', 'nacional'],
        gif_url="https://tenor.com/es/view/giffany-gravity-falls-gif-sprite-book-of-bill-gif-12544109780257466418",
        single_response=True
    )
    response(
        "Consulta la normatividad institucional en: https://ucompensar.edu.co/documentos-de-interes/",
        ['normatividad', 'institucional', 'consulta'],
        gif_url="https://tenor.com/es/view/giffany-gravity-falls-gif-sprite-book-of-bill-gif-12544109780257466418",
        single_response=True
    )
    response(
        "Si cerraron el grupo en el que te matriculaste, puedes: a) Cursar otro programa o asignatura, b) Inscribir otra asignatura (con ajustes en el valor si corresponde), o c) Solicitar devolución del 100% del valor pagado. (Art. 7 de PAF)",
        ['cerraron', 'grupo', 'matrícula'],
        gif_url="https://tenor.com/es/view/giffany-gravity-falls-gif-sprite-book-of-bill-gif-12544109780257466418",
        single_response=True
    )    
    response(
        "Puedes solicitar un segundo evaluador de tu nota. En primera instancia, pide revisión a tu docente; en segunda instancia, solicita formalmente en CRM que designen un evaluador alterno. (Art. 35 del RE)",
        ['segundo', 'evaluador', 'nota'],
        gif_url="https://tenor.com/es/view/giffany-gravity-falls-gif-sprite-book-of-bill-gif-12544109780257466418",
        single_response=True
    )
    response(
        "Para inscribirte, ingresa y llena el formulario aquí: https://academico.ucompensar.edu.co:8091/academusoft/academico/inscripcionLineaBootstrap/ind_ins_pub_seguro.jsp?_gl=1*1nivft2*_gcl_au*MTY1NDQzMjUwOS4xNzMwODM0MDAx*_ga*NjQ1MjUyNzQ1LjE3MzA4MzM5NzQ.*_ga_XGQ6YMBJF1*MTczMDgzMzk3NC4xLjEuMTczMDgzNjM3Ni40MS4wLjA.",
        ['inscribirme', 'formulario', 'inscripción', 'inscripcion', 'proceso'],
        gif_url="https://tenor.com/es/view/giffany-gravity-falls-gif-sprite-book-of-bill-gif-12544109780257466418",
        single_response=True
    )
    response(
        "Verifica tu estado de admisión tres días hábiles después de enviar los documentos. Consulta aquí: https://academico.ucompensar.edu.co:8091/academusoft/academico/inscripcionLinea4/consultaPublica/inicio.jsp?_gl=1*fzqthx*_gcl_au*MTY1NDQzMjUwOS4xNzMwODM0MDAx*_ga*NjQ1MjUyNzQ1LjE3MzA4MzM5NzQ.*_ga_XGQ6YMBJF1*MTczMDgzMzk3NC4xLjEuMTczMDgzNjU2Ni41OS4wLjA.",
        ['estado', 'admisión', 'verificar'],
        gif_url="https://tenor.com/es/view/giffany-gravity-falls-gif-sprite-book-of-bill-gif-12544109780257466418",
        single_response=True
    )
    response(
        "Nuestro número de teléfono para todo el país es: 01 8000 110 666",
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
    responses = ['¿Puedes decirlo de nuevo?', 'No estoy seguro de lo que quieres decir.', 
                 'Por favor, intenta ser más específico.']
    return responses[random.randrange(len(responses))]
