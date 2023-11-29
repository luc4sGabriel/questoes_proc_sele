-- Considere a tabela "Funcionarios". Escreva uma consulta SQL que retorne o nome, cargo e
-- salário de todos os funcionários que têm um salário superior a 50000.

SELECT NomeFuncionario, Cargo, Salario
FROM Funcionarios
WHERE Salario > 50000;