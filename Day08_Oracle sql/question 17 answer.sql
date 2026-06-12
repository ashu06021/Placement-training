SET SERVEROUTPUT ON;

DECLARE
    v_name VARCHAR2(100);
    v_sal NUMBER(10,2) := 0;
    v_dept NUMBER := 60;

BEGIN
    -- Fetch employee details
    SELECT first_name, salary
    INTO v_name, v_sal
    FROM employees
    WHERE employee_id = 100;

    DBMS_OUTPUT.PUT_LINE('Name: ' || v_name);
    DBMS_OUTPUT.PUT_LINE('Salary: ' || v_sal);

    -- IF ELSE condition
    IF v_sal > 20000 THEN
        DBMS_OUTPUT.PUT_LINE('Top Earner');
    ELSIF v_sal > 10000 THEN
        DBMS_OUTPUT.PUT_LINE('Senior');
    ELSE
        DBMS_OUTPUT.PUT_LINE('Junior');
    END IF;

    -- FOR LOOP
    FOR emp IN (
        SELECT first_name, salary
        FROM employees
        WHERE department_id = v_dept
        ORDER BY salary DESC
    )
    LOOP
        DBMS_OUTPUT.PUT_LINE(emp.first_name || ': ' || emp.salary);
    END LOOP;

EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Employee Not Found!');

    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
END;
/