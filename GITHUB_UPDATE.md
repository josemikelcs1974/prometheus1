# PROMETHEUS — Guía de Actualización de Repositorio (v2.0.0)

Este documento contiene los pasos para sincronizar tu repositorio de Github con la versión "Drástica y Contundente" desarrollada para garantizar operatividad total.

## ⚡ Cambios Críticos Realizados
1. **Migración Arquitectónica**: Sincronización de lógica Python/Streamlit a una arquitectura Full-Stack **React + Vite + Node.js**. Esto garantiza un rendimiento institucional y compatibilidad 100% con entornos de contenedores modernos.
2. **Estética Bloomberg v2**: Refinamiento total de la UI (Dark Mode Pro, Lucide Icons, Framer Motion).
3. **AEGIS Monitor**: Integración de un sistema de logs en tiempo real para auditoría de sistema.
4. **Universo ETF**: Configuración centralizada en `src/config.ts`.

## 📂 Estructura de Archivos a Actualizar
Asegúrate de que tu repositorio contenga:
- `/src/*`: Todos los archivos de la UI React (App.tsx, config.ts, componentes).
- `/package.json`: Configuración de dependencias y scripts.
- `/vite.config.ts`: Configuración del motor de construcción.
- `/server.ts`: (Opcional) Backend para futuras expansiones de datos.
- `/app.py` & `/config.py`: Los archivos originales se mantienen como referencia de lógica pero el motor principal es ahora React.

## 🚀 Cómo Ejecutar (Local)
1. Instalar dependencias: `npm install`
2. Iniciar sistema: `npm run dev`
3. Abrir en navegador: `http://localhost:3000`

## 🛠️ Próximos Pasos (Fase 2)
- Integración de API Yahoo Finance vía Proxy Node.js.
- Conexión real con agentes IA (Claude 3.5).
- Despliegue de Security Rules si se usa Firebase.

---
*⚡ PROMETHEUS — ETF Rotation Intelligence System*
