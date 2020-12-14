DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS activities;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    venue VARCHAR(255),
    category VARCHAR(255),
    capacity INT,
    finished BOOLEAN
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    activity_id INT REFERENCES activities(id) ON DELETE CASCADE
);