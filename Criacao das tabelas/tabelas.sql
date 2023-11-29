CREATE TABLE Clientes (
    ClienteID INT PRIMARY KEY,
    NomeCliente VARCHAR(255),
    Email VARCHAR(255)
);

CREATE TABLE Categorias (
    CategoriaID INT PRIMARY KEY,
    NomeCategoria VARCHAR(255)
);

CREATE TABLE Funcionarios (
    FuncionarioID INT PRIMARY KEY,
    NomeFuncionario VARCHAR(255),
    Cargo VARCHAR(255),
    Salario DECIMAL(10, 2)
);

CREATE TABLE Alunos (
    AlunoID INT PRIMARY KEY,
    NomeAluno VARCHAR(255)
);

CREATE TABLE Notas (
    AlunoID INT PRIMARY KEY,
    Disciplina VARCHAR(255),
    Nota DECIMAL(5, 2),
    FOREIGN KEY (AlunoID) REFERENCES Alunos(AlunoID)
);

CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY,
    NomeProduto VARCHAR(255),
    CategoriaID INT,
    FOREIGN KEY (CategoriaID) REFERENCES Categorias(CategoriaID)
);

CREATE TABLE Pedidos (
    PedidoID INT PRIMARY KEY,
    ClienteID INT,
    ProdutoID INT,
    DataPedido DATE,
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID),
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID)
);





