-- Energy Trading SQL Data Analysis Project
-- Author: Data Analytics Portfolio

-- Sample Trade Table
CREATE TABLE trades (
    trade_id INT,
    trade_date DATE,
    commodity VARCHAR(50),
    volume INT,
    price DECIMAL(10,2),
    pnl DECIMAL(10,2)
);

-- Sample Data
INSERT INTO trades VALUES (1, '2024-01-01', 'Gas', 100, 3.25, 120.50);
INSERT INTO trades VALUES (2, '2024-01-02', 'Power', 200, 4.10, -50.00);
INSERT INTO trades VALUES (3, '2024-01-03', 'Gas', 150, 3.40, 200.75);
INSERT INTO trades VALUES (4, '2024-01-04', 'Oil', 80, 70.00, 500.00);

-- Total PnL by Commodity
SELECT commodity, SUM(pnl) AS total_pnl
FROM trades
GROUP BY commodity;

-- Total Volume by Commodity
SELECT commodity, SUM(volume) AS total_volume
FROM trades
GROUP BY commodity;

-- Top profitable trades
SELECT *
FROM trades
ORDER BY pnl DESC
LIMIT 3;
