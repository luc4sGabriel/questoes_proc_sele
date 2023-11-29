-- Utilizando as tabelas "Alunos" e "Notas", escreva uma consulta SQL que retorne o nome do
-- aluno e a média de suas notas.

SELECT a.NomeAluno, AVG(n.Nota) AS MediaNotas
FROM Alunos a
JOIN Notas n ON a.AlunoID = n.AlunoID
GROUP BY a.NomeAluno;