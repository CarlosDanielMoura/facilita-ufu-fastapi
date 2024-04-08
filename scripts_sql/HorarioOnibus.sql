CREATE TABLE horario_onibus (
    id SERIAL PRIMARY KEY,
    horario_partida VARCHAR(20) NOT NULL,
    ponto_saida VARCHAR(100) NOT NULL,
    tipo_onibus VARCHAR(50) NOT NULL,
    destino VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);