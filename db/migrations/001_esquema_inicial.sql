-- ==================================================
-- Sistema de Gestión Académica
-- Migración Inicial
-- ==================================================

CREATE TABLE docentes (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre          VARCHAR(100) NOT NULL,
    correo          VARCHAR(150) NOT NULL UNIQUE,
    activo          BOOLEAN NOT NULL DEFAULT 1
);

CREATE TABLE estudiantes (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre          VARCHAR(100) NOT NULL,
    grado           VARCHAR(20) NOT NULL,
    activo          BOOLEAN NOT NULL DEFAULT 1
);

CREATE TABLE notas (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,

    estudiante_id   INTEGER NOT NULL,
    docente_id      INTEGER NOT NULL,

    asignatura      VARCHAR(100) NOT NULL,
    periodo         VARCHAR(20) NOT NULL,

    calificacion    DECIMAL(3,2)
                    NOT NULL
                    CHECK (calificacion >= 0 AND calificacion <= 5),

    activo          BOOLEAN NOT NULL DEFAULT 1,

    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (estudiante_id)
        REFERENCES estudiantes(id),

    FOREIGN KEY (docente_id)
        REFERENCES docentes(id),

    CONSTRAINT uq_nota_estudiante
        UNIQUE(estudiante_id, asignatura, periodo)
);

CREATE INDEX idx_notas_estudiante
ON notas(estudiante_id);

CREATE INDEX idx_notas_docente
ON notas(docente_id);