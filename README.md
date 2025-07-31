# Evil_Api_GreenX
---
#  MyHacking Station - Simulación de Exfiltración vía API

Este proyecto forma parte del entorno de pruebas de seguridad del sistema GreenX. Simula un ataque de tipo **man-in-the-middle (MITM)** y exfiltración de datos mediante una **API maliciosa** diseñada para interceptar formularios de pago y almacenar datos sensibles, todo sin alertar al usuario final.

---

##  ¿Qué hace esta aplicación?

- Expone un endpoint `/transaccion` que **simula una API legítima** de pagos.
- Recibe datos en formato JSON con información sensible de tarjetas.
- Almacena esos datos en una base de datos (PostgreSQL).
- Escribe simultáneamente un log plano (`transacciones_log.csv`) para trazabilidad.
- Responde con una plantilla `return.html` como si todo fuera normal.
- Permite visualizar las transacciones robadas desde `/dashboard` en un panel llamado **"MyHacking Station"**.

---

##  Tecnologías usadas

- **Flask** (Python 3.10+)
- **SQLAlchemy + PostgreSQL**
- **Marshmallow** para validación de datos
- **HTML (Jinja2)** para templates
- **Archivos planos (`.csv`)** como respaldo manual

---

## Cómo correrlo

1. **Clona este repositorio o descarga los archivos ZIP.**

```
git clone https://github.com/tunombre/myhackingstation.git
cd myhackingstation
```
Crea un entorno virtual
```
python3 -m venv env 
```
Instala dependencias.
```
pip install -r requirements.txt
```
Crea una base de datos PostgreSQL:

```
CREATE DATABASE transacciones;
CREATE USER flaskuser WITH PASSWORD 'flaskpass';
GRANT ALL PRIVILEGES ON DATABASE transacciones TO flaskuser;
```
Corre la aplicación:
```
python app.py
```
Haz un POST al endpoint:

```
curl -X POST http://localhost:5000/transaccion \
  -H "Content-Type: application/json" \
  -d '{
    "monto": 299.99,
    "titular": "Laura González",
    "pan": "4539457593812738",
    "ultimos_4_digitos": "2738",
    "marca_tarjeta": "VISA",
    "direccion": "Calle 123 #45-67",
    "ciudad": "Medellín",
    "departamento": "Antioquia",
    "codigo_postal": "050001"
}'
```
Ver el panel de captura:

Abre tu navegador y visita:
```
http://localhost:5000/dashboard
```
---
# ¿Qué simula exactamente?
Un endpoint de pasarela falsa que redirige datos hacia un sistema de terceros sin que el cliente lo note.

Una mala práctica común: recibir datos sensibles sin validación de origen, sin cifrado y sin medidas de protección de contenido.

Violación directa de estándares como PCI-DSS y OWASP.
---
# ¿Cómo mitigar estos ataques en sistemas reales?
Evitar intermediarios no autenticados en flujos críticos (pasarelas, APIs de pago).

Implementar validación de origen, tokens de autenticación y firmas digitales.

Cifrar todo tráfico sensible (TLS/HTTPS obligatorio).

Auditar todos los endpoints internos y externos.

Aplicar el principio de confianza cero (Zero Trust).
---
# Disclaimer
Este proyecto fue desarrollado únicamente con fines académicos y de simulación dentro de un entorno controlado. No debe ser utilizado en sistemas productivos ni con información real.
---
### Créditos
Proyecto académico de ciberseguridad – Grupo GreenX
Autor: Santiago Potes
Licencia: MIT 
