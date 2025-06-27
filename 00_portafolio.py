# -*- coding: utf-8 -*-
"""
Created on Tue May 13 12:12:51 2025

@author: Dell
"""

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Portafolio de Alejandro Villegas</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      line-height: 1.6;
      background-color: #f4f4f4;
      color: #333;
    }

    header {
      background-color: #222;
      color: white;
      padding: 60px 20px;
      text-align: center;
    }

    header h1 {
      font-size: 2.8em;
      margin-bottom: 10px;
    }

    .header-info {
      display: flex;
      justify-content: center;
      gap: 40px;
      margin-top: 20px;
      flex-wrap: wrap;
    }

    .section {
      padding: 40px 20px;
      max-width: 1000px;
      margin: 0 auto;
    }

    .section h2 {
      font-size: 2em;
      margin-bottom: 20px;
      color: #444;
      border-bottom: 2px solid #ddd;
      padding-bottom: 10px;
    }

    .contact-info p,
    .about p {
      margin-bottom: 10px;
    }

    .skills ul {
      display: flex;
      flex-wrap: wrap;
      list-style: none;
      gap: 15px;
      padding: 0;
    }

    .skills li {
      background-color: #eee;
      padding: 10px 15px;
      border-radius: 20px;
      font-weight: 500;
    }

    .projects {
      display: flex;
      flex-direction: column;
      gap: 30px;
    }

    .project {
      background-color: #fff;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }

    .project img {
      width: 90%;
      max-height: 250px;
      object-fit: contain;
      border-radius: 8px;
      margin: 0 auto 10px;
      display:block;
    }

    .project h3 {
      margin-bottom: 10px;
    }

    .project p {
      margin-bottom: 10px;
    }

    .project a {
      display: inline-block;
      color: #0066cc;
      text-decoration: none;
      font-weight: bold;
    }

    .project a:hover {
      text-decoration: underline;
    }

    footer {
      background-color: #222;
      color: white;
      text-align: center;
      padding: 20px;
    }
  </style>
</head>
<body>

  <!-- Sección 1: Encabezado -->
  <header>
    <h1>Portafolio de Proyectos</h1>
    <div class="header-info">
      <div><strong>Nombre:</strong> Alejandro Villegas</div>
      <div><strong>Rol:</strong> Consultor </div>
    </div>
  </header>

  <!-- Sección 2: Perfil -->
  <section class="section about">
    <h2>Perfil</h2>
    <p>Profesional con experiencia en la ciencia de datos, inteligencia artificial, políticas públicas y lagestión de proyectos. Me interesan las áreas donde se puedan aplicar las tecnologías emergentes a la solución de problemas públicos y organizacionales. He realizado investigaciones sobre el uso de tecnologías de inteligencia artificial en organizaciones gubernamentales, sobre la aplicaciónde Large Language Models (LLM’s) para análisis y clasificación de textos y automatización detareas. Sumado a ello, he participado en evaluaciónes de proyectos, tanto en la parte cualitativa,como cuantitativa.</p>
  </section>

  <!-- Sección 3: Tecnologías con las cuales tengo experiencia -->
  <section class="section skills">
    <h2>Tecnologías con las cuales tengo experiencia</h2>
    <ul>
      <li>Paquetería Office, especialmente, Word, Excel y Power Point</li>
      <li>R y R Studio</li>
      <li>Python</li>
      <li>Power Bi</li>
      <li>Qgis</li>
      <li>SQL</li>
      <li>Git y Git Hub</li>
      <li>LLM's</li>
      <li>Jupyter Notebook</li>
      <li>SQL</li>
    </ul>
  </section>

  <!-- Sección 4: Contacto -->
  <section class="section contact-info">
    <h2>Contacto</h2>
    <p><strong>Email:</strong> java.law.1993@gmail.com</p>
    <p><strong>Teléfono:</strong> +52 55 8449 4633</p>
    <p><strong> Lugar de residencia:</strong> Ciudad de México</p>
    
    <p><strong>Linkedin:</strong> <a href="https://www.linkedin.com/in/alejandro-villegas-alp%C3%ADzar-b65527216/" target="_blank"> www.linkedin.com/in/alejandro-villegas-alpízar-b65527216</a></p>
    
    <p><strong>GitHub:</strong> <a href="https://github.com/AleVillegas9" target="_blank">https://github.com/AleVillegas9</a></p>
  </section>

  <!-- Sección 5: Proyectos -->
  <section class="section">
    <h2>Proyectos</h2>
    <div class="projects">

      <!-- Proyecto 1 -->
      <div class="project">
        <h3>01. Uso de Qgis y R para conocer la población del Área de Influencia de un proyecto</h3>
        <img src="imagenes/01_imagen.png" alt="Proyecto 1">
        <p>Supongamos que se tiene georeferenciada polígono de un proyecto. Sin embargo, para evaluar la viabilidad y el imapacto social de dicho proyecto se requiere conocer ¿cuál es el Área de Influencia de dicho proyecto? y ¿ A cuantas personas potencialmente afectaría nuestro proyecto?</p>
        <a href="https://alevillegas9.github.io/01_poblacion_ai/01.html" target="_blank">Ver proyecto</a>
      </div>

      <!-- Proyecto 2 -->
      <div class="project">
        <h3>02. Llenado automático de archivos desde una base de datos con python</h3>
        <img src="imagenes/02_imagen.png" alt="Proyecto 2">
        <p>Demostración de cómo llenar de manera automática y masiva documentos desde una base de datos. De esta manera se pueden crear documentos personalizados de manera automática.</p>
        <a href="https://alevillegas9.github.io/02_Llenado_automatico_documentos/02.html" target="_blank">Ver proyecto</a>
      </div>

      <!-- Proyecto 3 -->
      <div class="project">
        <h3>03. Monitoreo semiautomático de noticias con IA.</h3>
        <img src="imagenes/03_imagen.png" alt="Proyecto 3">
        <p>Demostración de cómo se puede utilizar Python y la inteligencia artificial (LLM's) para semiautomatizar el flujo de trabajo de un monitor de noticias. Desde la recuperación de las noticias relevantes de un portal, hasta la clasificación, resumen y presentación de los resultados.</p>
        <a href="https://alevillegas9.github.io/04_monitoreo_noticias_con_IA/04.html" target="_blank">Ver proyecto</a>
      </div>
      
      <!-- Proyecto 4 -->
      <div class="project">
        <h3>04. Clasificación y chatbot con documentos jurídicos usando Retrieval Augmentend Generation (RAG).</h3>
        <img src="imagenes/04_imagen.png" alt="Proyecto 4">
        <p>Ejemplo de cómo se puede utilizar el poder la inteligencia artificial y de los LLM's en partícular para clasificar, resumir y explorar/chatear con diferentes tipos de textos. Para ello se hace el uso del Retrieval Agumented Generation (RAG), pues esta técnica permite la  optimización de consultas de documentos extensos.</p>
        <a href="https://alevillegas9.github.io/03_rag_clas_chat/03.html" target="_blank">Ver proyecto</a>
      </div>
      
      <!-- Otros -->
      
<div class="project">
  <h3>EXTRA: Antología de movimientos de apropiación de tecnologías de la información: caso del Laboratorio de Ciencia de Datos y Métodos Modernos de Producción de Información</h3>
  <img src="imagenes/extra_02_imagen.png" alt="Tesis maestría">
  <p>En el marco de la Maestría en Administración y Política Pública impartida por el Centro de Investigación y Docencia Economicas (CIDE), realicé una investigación cualitativa sobre sobre el uso y gobernanza de las herramientas de Inteligencia Artificial en el Laboratorio de Ciencia de Datos del INEGI. Esto me permitió observar cuáles son los dificultades organizacionales presentes en la adopción y uso de estas tecnologías, así como la manera en que la organización enfrenta estos problemas, o aprovecha las ventajas. </p>
  <a href="https://repositorio-digital.cide.edu//handle/11651/6205" target="_blank">Ver proyecto</a>
</div>

<div class="project">
  <h3>EXTRA: Análisis del Programa ADA en San Luis Potosí</h3>
  <img src="imagenes/extra_01_imagen.png" alt="Programa Ada - Proyecto">
  <p>En marco del Policy Lab organizado por la UNESCO en el año 2024 participé en la creación del análisis y propuestas de mejora del diseño e implementación del Programa ADA, orientado al fortalecimiento de habilidades STEM en mujeres adolescentes en San Luis Potosí, México.</p>
  <a href="https://unesdoc.unesco.org/ark:/48223/pf0000391226" target="_blank">Ver proyecto</a>
</div>


  <footer>
    © 2025 Alejandro Villegas. Todos los derechos reservados.
  </footer>

</body>
</html>

"""

#0909090909090909090
import os

# Ruta de la carpeta donde quieres guardar el archivo
carpeta_destino = r"C:\Users\javal\OneDrive\Desktop\Portafolio 9\00_portafolio"
archivo_html = r"C:\Users\javal\OneDrive\Desktop\Portafolio 9\00_portafolio\index.html"

# Crear la carpeta si no existe
os.makedirs(carpeta_destino, exist_ok=True)

# Ruta completa del archivo
ruta_completa = os.path.join(carpeta_destino, archivo_html)

# Escribir el archivo HTML
with open(ruta_completa, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"Archivo HTML creado exitosamente en: {ruta_completa}")