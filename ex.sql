SELECT *
FROM your_table
WHERE REGEXP_LIKE(your_column, '(^|\s)(1[0-9]{3,}|[2-9][0-9]{3,})(\s|$)record in abc$');
