#Pre-Entrega de Proyecto — Automatización Web con Selenium y Pytest

Este proyecto corresponde a la **pre-entrega** del curso de *Automatización de Pruebas con Selenium y Python*.  
El objetivo es demostrar el uso de **Selenium WebDriver** junto con **Pytest** para automatizar flujos básicos del sitio web [saucedemo.com](https://www.saucedemo.com).

---

##Objetivo General

Automatizar interacciones y validaciones dentro de la aplicación web **SauceDemo**, aplicando los conceptos aprendidos hasta la Clase 8:
- Manejo de **localizadores**.
- **Esperas explícitas**.
- Validaciones de contenido y estado de página.
- **Estructura modular de código** usando Page Object Model (POM).
- Generación de reportes y evidencia de ejecución.

---

##Tecnologías Utilizadas

- **Python 3.10+**
- **Selenium 4**
- **Pytest**
- **Pytest-HTML** (para generar reporte HTML)
- **Git & GitHub** (para control de versiones)

---

## 📂Estructura del Proyecto
pre-entrega-automation-testing-Giuli
│
├── 📂 pages/              
│   ├── base_page.py          → Clase base con métodos reutilizables (esperas, navegación, etc.)
│   ├── login_page.py         → Page Object del login (campos, botones, flujo de acceso)
│   ├── inventory_page.py     → Page Object del catálogo (productos, menú, filtros)
│   └── cart_page.py          → Page Object del carrito (items agregados, validaciones)
│
├── 📂 tests/
│   ├── test_login.py         → Caso de prueba: Login exitoso
│   ├── test_catalog.py       → Caso de prueba: Verificación del catálogo
│   └── test_cart.py          → Caso de prueba: Interacción con el carrito
│
├── 📂 utils/                 
│   └── (vacío o utilidades futuras) → Funciones auxiliares o datos compartidos
│
├── 📂 datos/                 
│   └── (vacío o futuros CSV/JSON) → Datos externos para pruebas parametrizadas
│
├── 📂 reports/               
│   ├── reporte.html          → Reporte HTML generado por Pytest
│   ├── *.png                 → Capturas automáticas en caso de fallos
│   └── *.html                → HTMLs de las páginas en el momento del error
│
├── ⚙️ conftest.py             → Configuración general de Pytest, fixture del WebDriver y hooks
├── 📄 requirements.txt        → Dependencias necesarias del entorno
├── 🧩 pytest.ini              → Configuración global para ejecución y marcadores de pruebas
└── 📘 README.md               → Documentación completa del proyecto


