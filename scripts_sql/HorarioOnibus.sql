CREATE TABLE Viagens (
    id SERIAL PRIMARY KEY,
    horario_partida TIMESTAMP NOT NULL,
    ponto_saida VARCHAR(100) NOT NULL,
    tipo_onibus VARCHAR(50) NOT NULL,
    destino VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);