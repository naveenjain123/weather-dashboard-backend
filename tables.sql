CREATE TABLE weather_history (
    id int NOT NULL AUTO_INCREMENT,
    country varchar(100),
    temp int default 0,
    feels_like int default 0,
    temp_min int default 0,
    temp_max int default 0,
    pressure int default 0,
    sea_level int default 0,
    grnd_level int default 0,
    humidity int default 0,
    temp_kf int default 0,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);
