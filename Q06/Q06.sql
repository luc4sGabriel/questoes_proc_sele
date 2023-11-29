-- Escreva uma consulta SQL que retorne o nome do cliente, o número do pedido e a data do
-- pedido, ordenados pela data do pedido em ordem decrescente.

SELECT c.NomeCliente, p.PedidoID, p.DataPedido
FROM Clientes c
JOIN Pedidos p ON c.ClienteID = p.ClienteID
ORDER BY p.DataPedido DESC;