CREATE TABLE weather_history (
    id int NOT NULL,
    country varchar(100),
    temp int,
    feels_like int,
    temp_min int,
    temp_max int,
    pressure int,
    sea_level int,
    grnd_level int,
    humidity int,
    temp_kf int,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);
