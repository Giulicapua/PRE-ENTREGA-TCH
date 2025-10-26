<<<<<<< HEAD
# Pre-Entrega de Proyecto — Automatización Web con Selenium y Pytest

Este proyecto corresponde a la **pre-entrega** del curso de *Automatización de Pruebas con Selenium y Python*.  
El objetivo es demostrar el uso de **Selenium WebDriver** junto con **Pytest** para automatizar flujos básicos del sitio web [saucedemo.com](https://www.saucedemo.com).

---

## Objetivo General

Automatizar interacciones y validaciones dentro de la aplicación web **SauceDemo**, aplicando los conceptos aprendidos hasta la Clase 8:
- Manejo de **localizadores**.
- **Esperas explícitas**.
- Validaciones de contenido y estado de página.
- **Estructura modular de código** usando Page Object Model (POM).
- Generación de reportes y evidencia de ejecución.

---

## Tecnologías Utilizadas

- **Python 3.10+**
- **Selenium 4**
- **Pytest**
- **Pytest-HTML** (para generar reporte HTML)
- **Git & GitHub** (para control de versiones)

---


=======
# Pre-Entrega: Automatización Web (Selenium + Pytest) — saucedemo.com

Proyecto de práctica para automatizar flujos básicos en **https://www.saucedemo.com** usando **Selenium WebDriver** y **Pytest**.

## 🎯 Objetivo
Aplicar los conocimientos vistos hasta la Clase 8 del curso:
- Automatizar el login.
- Verificar la navegación y elementos del catálogo.
- Interactuar con productos y validar el carrito.

## 🧰 Tecnologías
- Python 3.10+
- Selenium 4
- Pytest
- pytest-html (para generar reporte HTML)

## 📁 Estructura
```text
pre-entrega-automation-testing-Giuli-ES/
├─ pages/          # Clases de las páginas (Page Object Model)
├─ tests/          # Casos de prueba
├─ utils/          # Funciones auxiliares
├─ datos/          # Archivos externos (si aplica)
├─ reports/        # Reportes HTML y capturas automáticas
├─ conftest.py     # Configuración de pytest y fixture del driver
├─ requirements.txt
├─ pytest.ini
└─ README.md
```

## ⚙️ Instalación y configuración
1. Crear entorno virtual e instalar dependencias:
```bash
python -m venv .venv
source .venv/bin/activate      # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2. Verificar que el entorno esté listo ejecutando:
```bash
pytest -v --html=reports/reporte.html --self-contained-html
```

3. Si querés ver el navegador (modo con interfaz):
```bash
pytest -v --html=reports/reporte.html --self-contained-html --headed
```

## 🧪 Casos de prueba incluidos
- **Login**: verifica acceso exitoso y redirección a `/inventory.html`.
- **Catálogo**: valida título, productos visibles y datos del primer ítem.
- **Carrito**: agrega un producto, verifica el contador y presencia en el carrito.

## 📸 Evidencias automáticas
En caso de fallo, se generan:
- Captura de pantalla (`.png`)
- HTML de la página
Ambos se guardan en `reports/` y se incluyen en el reporte HTML.

## 🧾 Comandos útiles
```bash
pytest -v --html=reports/reporte.html --self-contained-html
pytest -v --html=reports/reporte.html --self-contained-html --headed
```

## 💡 Consejos
- Asegurate de tener **Google Chrome** instalado.
- Si necesitás cambiar la URL base:
  ```bash
  pytest --base_url=https://www.saucedemo.com
  ```

## 🌐 Subir a GitHub
1. Crear repo en GitHub: `pre-entrega-automation-testing-[nombre-apellido]`
2. Ejecutar:
```bash
git init
git add .
git commit -m "feat: pre-entrega Selenium + Pytest con comentarios en español"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/pre-entrega-automation-testing-[nombre-apellido].git
git push -u origin main
```

## 🏁 Generar reporte HTML
```bash
pytest -v --html=reports/reporte.html --self-contained-html
```

---
💬 Este proyecto cumple con todos los requisitos de la pre-entrega:
- Estructura profesional.
- Código limpio y documentado.
- Casos independientes y automatizados.
>>>>>>> ba78d20 (Proyecto base Selenium + Pytest oara Saucedemo)
