CREATE TABLE IF NOT EXISTS roles (
    role_id INT PRIMARY KEY,
    role_name VARCHAR(255) NOT NULL
)  ENGINE=INNODB;

insert into roles VALUES (0, 'Admin'), (1, 'Professor'), (2, 'Student')

CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_number CHAR(10) UNIQUE,
    user_name VARCHAR(255) NOT NULL,
    password CHAR(20) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    user_role int,
    FOREIGN KEY (user_role)
        REFERENCES roles (role_id)
        ON UPDATE RESTRICT ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS courses (
    course_number INT PRIMARY KEY,
    course_name VARCHAR(255) NOT NULL,
    semester VARCHAR(20) NOT NULL,
    term int(2) NOT NULL,
)  ENGINE=INNODB;


CREATE TABLE IF NOT EXISTS grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id int not null,
    professor_id int not null,
    course_number int not null,
    course_grade double not null,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id)
        REFERENCES users (user_id)
        ON UPDATE RESTRICT ON DELETE CASCADE,
    FOREIGN KEY (professor_id)
        REFERENCES users (user_id)
        ON UPDATE RESTRICT ON DELETE CASCADE,
    FOREIGN KEY (course_number)
        REFERENCES courses (course_number)
        ON UPDATE RESTRICT ON DELETE CASCADE
);





