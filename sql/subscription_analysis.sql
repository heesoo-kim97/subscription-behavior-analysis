CREATE DATABASE IF NOT EXISTS subscription_analysis;
USE subscription_analysis;

CREATE TABLE client_details (
    client_id BIGINT PRIMARY KEY,
    company_size VARCHAR(20),
    industry VARCHAR(50),
    location VARCHAR(100)
);

CREATE TABLE subscription_records (
   client_id BIGINT,
   subscription_type VARCHAR(20),
   start_date DATE,
    end_date DATE,
    renewed BOOLEAN,
    PRIMARY KEY (client_id, start_date),
    FOREIGN KEY (client_id)
         REFERENCES client_details(client_id)
);

CREATE TABLE economic_indicators (
   start_date DATE,
   end_date DATE,
   inflation_rate DECIMAL(5,2),
   gdp_growth_rate DECIMAL(5,2),
   PRIMARY KEY (start_date, end_date)
);