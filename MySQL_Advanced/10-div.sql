-- creates a function SafeDiv that divides (and returns) the first by the second number
-- returns 0 if the second number is equal to 0.
DELIMITER $$

CREATE FUNCTION SafeDiv (
    input_a INT,
    input_b INT
)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    IF input_b = 0 THEN
        RETURN 0;
    ELSE
        RETURN input_a /input_b;
    END IF;

END $$

DELIMITER ;
