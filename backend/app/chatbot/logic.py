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
        "Tenemos diferentes programas ¿Cuál es de tu interés (pregrado o postgrado)?",
        ['programas', 'carreras'],
        single_response=True
    )
    response(
        "Nuestros programas de pregrado son: Ingeniería Multimedia (Pregrado-Bogotá), Ciencia de datos (Pregrado-Bogotá y Virtual), Ingeniería Industrial (Pregrado-Bogotá), Ingeniería de Telecomunicaciones (Pregrado-Bogotá y Meta), Ingeniería de Sistemas (Pregrado-Bogotá, Meta y Virtual), Ingeniería de Software (Pregrado-Bogotá y Virtual), Administración Financiera (Pregrado-Bogotá y Virtual), Contaduría Pública (Pregrado-Bogotá, Meta y Virtual), Finanzas y Negocios Internacionales (Pregrado-Bogotá y Virtual), Administración de Empresas (Pregrado-Bogotá y Virtual), Profesional en Negocios y Logística Internacional (Pregrado-Bogotá y Virtual), Administración de Servicios de Salud (Pregrado-Bogotá), Mercadeo y Publicidad (Pregrado-Bogotá y Virtual), Administración en Salud (Pregrado-Virtual), Licenciatura en Bilingüismo con Énfasis en Inglés (Pregrado-Bogotá y Meta), Licenciatura en Educación Infantil (Pregrado-Bogotá y Meta), Profesional en Lenguas (Pregrado-Bogotá y Virtual), Profesional en Deporte y Actividad Física (Pregrado-Bogotá), Diseño Visual (Pregrado-Bogotá y Virtual), Comunicación Social (Pregrado-Bogotá)",
        ['pregrado', 'carreras', 'programas'],
        single_response=True
    )
    response(
        "Nuestros programas de postgrado son: Especialización en Gerencia para el Desarrollo del Talento (Postgrado-Virtual), Especialización en Contabilidad y Auditoría en Entornos Digitales (Postgrado-Virtual), Especialización en Experiencia y Servicio al Cliente (Postgrado-Virtual), Especialización en Contabilidad y Auditoría en Entornos Digitales (Postgrado-Bogotá), Especialización en Análisis y Planeación Estratégica de Medios (Postgrado-Bogotá), Especialización en Narrativas y Lenguajes Digitales (Postgrado-Bogotá y Virtual), Especialización en Finanzas (Postgrado-Presencial y Virtual), Especialización en Inteligencia y Prospectiva de Negocios (Postgrado-Presencial y Virtual), Especialización en Seguridad Informática (Postgrado-Bogotá), Especialización en Gerencia de la Comunicación Estratégica (Postgrado-Bogotá y Virtual), Especialización en Seguridad y Salud en el Trabajo (Postgrado-Bogotá y Virtual), Especialización en Big Data (Postgrado-Bogotá y Virtual), ",
        ['postgrado', 'carreras', 'programas'],
        single_response=True
    )
    response(
        "Aquí tienes nuestro enlace a la página web: https://ucompensar.edu.co/",
        ['pagina', 'web', 'enlace', 'sitio'],
        single_response=True
    )
    response(
        "Puedes consultar el reglamento estudiantil en: https://ucompensar.edu.co/wp-content/uploads/2023/08/Reglamento-estudiantil-v2.pdf",
        ['estudiantil','reglamento'],
        single_response=True
    )
    response(
        "Puedes consultar el reglamento docente en: https://ucompensar.edu.co/wp-content/uploads/2022/07/Reglamento-Docente-ucompensar.pdf",
        ['docente','reglamento'],
        single_response=True
    )
    response(
        "Puedes consultar el Proyecto Educativo Institucional en: https://ucompensar.edu.co/wp-content/uploads/2021/06/PEI_Proyecto_Educativo_Institucional.pdf",
        ['proyecto','educativo','institucional','pei'],
        single_response=True
    )
    response(
        "Contamos con sedes en Bogotá, Villavicencio y Formación virtual. ¿En cuál tienes interés?",
        ['sedes', 'dirección', 'ubicados', 'queda','ubicada'],
        single_response=True
    )
    response(
        "Nuestra sede Teusaquillo en Bogotá, se encuentra ubicada en Avenida (Calle) 32 No. 17-30. Teléfono aspirantes: 601 3380666. WhatsApp: (+57) 3173002952",
        ['bogotá', 'sede', 'dirección', 'bogota','contacto','telefono'],
        single_response=True
    )
    response(
        "Puedes estudiar en nuestra sede virtual. Línea nacional: 01 8000 110 666. Correo: aspirantes@ucompensar.edu.co. WhatsApp: (+57) 3173002952",
        ['virtual', 'línea', 'correo','contacto','telefono','estudiar'],
        single_response=True
    )
    response(
        "La Sede en Meta está ubicada en Sede Educación Cofrem, Carrera 35 No. 20A - 02, Villavicencio. Teléfono: 608 6818640. WhatsApp: (+57) 3173002952",
        ['meta', 'villavicencio', 'sede', 'dirección','telefono'],
        single_response=True
    )
    response(
        "Para el resto del país, puedes comunicarte al teléfono nacional 01 8000 110 666.",
        ['país', 'teléfono', 'nacional','contacto'],
        single_response=True
    )
    response(
        "Consulta la normatividad institucional en: https://ucompensar.edu.co/documentos-de-interes/",
        ['normatividad', 'institucional', 'consulta'],
        single_response=True
    )
    response(
        "Consulta aquí las diferentes opciones de financiación: https://ucompensar.edu.co/zona-financiera/opciones-de-financiacion/",
        ['financiar', 'financiación', 'financiamiento','financiacion', 'prestamo', 'icetex','préstamos', 'prestamos', 'descuentos','compensar'],
        single_response=True
    )
    response(
        "Nuestras publicaciones destacadas son: <ul> <li>Sistemas Logísticos en la comercialización de productos agrícolas basados en la industria 4.0</li> <li>Creatividad y Design Thinking</li></ul>",
        ['publicaciones','destacadas','importantes']
    )
    response(
        "Consulta aquí toda la información acerca de semilleros de investigación: https://ucompensar.edu.co/semilleros/",
        ["semilleros","semillero"],
        single_response=True
    )
    response(
        "La Investigación en la Fundación Universitaria Compensar se concentra en el desarrollo de actividades de ciencia, tecnología e innovación, siguiendo un enfoque aplicado; basadas en la generación de soluciones pertinentes para el sector productivo, organizaciones y comunidades, en permanente escucha de sus necesidades que son el pilar de nuestro relacionamiento Universidad – Empresa y que activan los distintos escenarios de investigación aplicada tanto por parte de los grupos de investigación como para la investigación formativa.",
        ['investigación','investigacion'],
        single_response=True
    )
    response(
        "Cacharreando es un programa de radio dedicado a la investigación en UCompensar. Esta iniciativa, materializada en 2023 por los líderes de los grupos de investigación, busca compartir con la comunidad académica los avances y novedades de la investigación en UCompensar. Te invitamos a conocer CACHARREANDO a través de su micrositio en nuestro campus virtual.",
        ['cacharreando'],
        single_response=True
    )
    response(
        "Si cerraron el grupo en el que te matriculaste, puedes: a) Cursar otro programa o asignatura, b) Inscribir otra asignatura (con ajustes en el valor si corresponde), o c) Solicitar devolución del 100% del valor pagado. (Art. 7 de PAF)",
        ['cerraron', 'grupo', 'matrícula','matriculé','matricule','cerro','cerró',],
        single_response=True
    )    
    response(
        "Puedes solicitar un segundo evaluador de tu nota. En primera instancia, pide revisión a tu docente; en segunda instancia, solicita formalmente en CRM que designen un evaluador alterno. (Art. 35 del RE)",
        ['segundo', 'evaluador', 'nota'],
        single_response=True
    )
    response(
        "Para inscribirte, ingresa y llena el formulario aquí: https://academico.ucompensar.edu.co:8091/academusoft/academico/inscripcionLineaBootstrap/ind_ins_pub_seguro.jsp?_gl=1*1nivft2*_gcl_au*MTY1NDQzMjUwOS4xNzMwODM0MDAx*_ga*NjQ1MjUyNzQ1LjE3MzA4MzM5NzQ.*_ga_XGQ6YMBJF1*MTczMDgzMzk3NC4xLjEuMTczMDgzNjM3Ni40MS4wLjA.",
        ['inscribirme', 'formulario', 'inscripción', 'inscripcion', 'proceso', 'inscribo','matrícula','matricula','matricularme','matriculo', 'matricular'],
        single_response=True
    )
    response(
        "Verifica tu estado de admisión tres días hábiles después de enviar los documentos. Consulta aquí: https://academico.ucompensar.edu.co:8091/academusoft/academico/inscripcionLinea4/consultaPublica/inicio.jsp?_gl=1*fzqthx*_gcl_au*MTY1NDQzMjUwOS4xNzMwODM0MDAx*_ga*NjQ1MjUyNzQ1LjE3MzA4MzM5NzQ.*_ga_XGQ6YMBJF1*MTczMDgzMzk3NC4xLjEuMTczMDgzNjU2Ni41OS4wLjA.",
        ['estado', 'admisión', 'verificar','admision'],
        single_response=True
    )
    response(
        "Nuestro número de teléfono para todo el país es: 01 8000 110 666",
        ['telefono', 'numero', 'contacto'],
        single_response=True
    )
    response(
        "Ofrecemos una Beca del 75% para estudiantes nuevos, dirigida a estudiantes nuevos en programas de Técnico Laboral o Pregrado, también tenemos beca del 75% para estudiantes antiguos que ya cuenten con dicho beneficio, recibe más información y consulta requisitos en: consulta los requisitos en: https://ucompensar.edu.co/becas-compensar/ ",
        ['becas', 'incentivos', 'beca', 'incentivo'],
        single_response=True
    )
    response(
        "Ingresa al campus virtual en: https://unipanamericanaeduco.sharepoint.com/Portal%20MiPana/SitePages/INICIOPORTAL.aspx",
        ['campus', 'virtual'],
        single_response=True
    )
    response(
        "Consulta el calendario académico en: https://unipanamericanaeduco.sharepoint.com/Portal%20MiPana/SitePages/Calendario-Academico-2024-Estudiantes-VF.aspx",
        ['calendario', 'académico', 'academico'],
        single_response=True
    )
    response(
        "Consulta información sobre el nuevo campus en: https://nuevocampus.ucompensar.edu.co",
        ['nuevo', 'campus'],
        single_response=True
    ) 
    response(
        "Gracias por tu visita. ¡Que tengas un gran día!",
        ['adios', 'gracias', 'nos vemos'],
        single_response=True
    )
    
    best_match = max(highest_prob, key=highest_prob.get)
    return best_match if highest_prob[best_match] > 0 else ""


def unknown():
    responses = ['¿Puedes decirlo de nuevo?', 'No estoy seguro de lo que quieres decir.', 
                 'Por favor, intenta ser más específico.']
    return responses[random.randrange(len(responses))]
