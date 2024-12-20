-- creates a stored procedure AddBonus that adds a new correction for a student
-- check if the project already exists. If not, you should create it
DELIMITER $$

CREATE PROCEDURE AddBonus (
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
DECLARE project_id_from_name INT;

SET
    project_id_from_name = (
        SELECT id
        FROM projects
        WHERE
            name = project_name
    );

IF project_id_from_name IS NULL THEN
INSERT INTO
    projects (name)
VALUES (project_name);

SET project_id_from_name = LAST_INSERT_ID();

END IF;

INSERT INTO
    corrections (user_id, project_id, score)
VALUES (
        user_id,
        project_id_from_name,
        score
    );
END $$

DELIMITER ;
