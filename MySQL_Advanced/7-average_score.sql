-- creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
-- An average score can be a decimal
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser (
    IN user_id INT
)
BEGIN
    DECLARE average_score_of_a_student FLOAT;
    SELECT AVG(score) 
    INTO average_score_of_a_student
    FROM corrections 
    WHERE user_id = user_id;
    
    UPDATE users 
        SET average_score = average_score_of_a_student
        WHERE id = user_id;
END $$

DELIMITER ;
