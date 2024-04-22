CREATE TABLE atividade_academica (
    id_atividade_academica SERIAL PRIMARY KEY,
    semestre_vigente VARCHAR NOT NULL,
    desc_atividade VARCHAR NOT NULL,
    data_fim VARCHAR NOT NULL,
    data_inicio VARCHAR NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
