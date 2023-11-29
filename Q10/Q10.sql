-- Considere as tabelas "Clientes", "Pedidos" e "Produtos". Escreva uma consulta SQL que
-- retorne o nome do cliente, o número do pedido e a quantidade total de itens em cada pedido.
-- Utilize junções múltiplas e funções agregadas.

SELECT c.NomeCliente, p.PedidoID, COUNT(*) AS QuantidadeTotal
FROM Clientes c
JOIN Pedidos p ON c.ClienteID = p.ClienteID
JOIN Produtos pr ON p.ProdutoID = pr.ProdutoID
GROUP BY c.NomeCliente, p.PedidoID;
    