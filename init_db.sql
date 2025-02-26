CREATE DATABASE IF NOT EXISTS jobboard;
USE jobboard;

DROP TABLE IF EXISTS jobs;
CREATE TABLE jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    company VARCHAR(255) NOT NULL,
    link VARCHAR(255) NOT NULL,
    post_date DATE NOT NULL
);

-- insert test data
INSERT INTO jobs (title, company, link, post_date) VALUES
('Software Development Intern', 'Xerox', 'https://xerox.avature.net/en_US/careers/JobDetail/Software-Development-Intern/45959', '2025-02-25'),
('Software Engineer - Intern', 'KLA Corporation', 'https://kla.wd1.myworkdayjobs.com/en-US/Search/job/Milpitas-CA/Software-Engineer---Intern_2527845-1?Country=bc33aa3152ec42d4995f4791a106ed09', '2025-02-24');
