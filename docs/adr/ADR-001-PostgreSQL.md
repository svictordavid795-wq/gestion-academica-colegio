# ADR-001 Uso de PostgreSQL

## Estado

Aceptada

## Fecha

2026-09-19

## Contexto

La institución educativa presenta problemas de pérdida de información debido a conflictos de concurrencia cuando múltiples docentes modifican archivos Excel compartidos.

## Decisión

Se utilizará PostgreSQL como base de datos principal para almacenar notas y asistencia.

## Consecuencias Positivas

- Evita pérdida de datos.
- Permite trabajo simultáneo de docentes.
- Garantiza integridad de la información.
- Facilita respaldos y recuperación.

## Consecuencias Negativas

- Requiere instalación y administración básica.
- Necesita migración inicial desde Excel.