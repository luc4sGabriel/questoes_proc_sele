-- Utilizando a tabela "Produtos" e "Categorias", escreva uma consulta SQL que retorne o
-- número de produtos em cada categoria, mostrando também o nome da categoria.

SELECT c.NomeCategoria, COUNT(p.ProdutoID) AS NumeroDeProdutos
FROM Categorias c
JOIN Produtos p ON c.CategoriaID = p.CategoriaID
GROUP BY c.NomeCategoria;