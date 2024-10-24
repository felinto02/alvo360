<?php
// Conexão com o banco de dados (substitua com suas credenciais)
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "operacao";

$conn = new mysqli($servername, $username, $password, $dbname);

// Verificação de erros na conexão
if ($conn->connect_error) {
  die("Erro na conexão: " . $conn->connect_error);
}

// Consulta SQL para buscar as imagens (adapte à sua tabela)
$sql = "SELECT caminho_da_imagem FROM sua_tabela LIMIT 2";
$result = $conn->query($sql);

// Exibir as imagens
if ($result->num_rows > 0) {
  while($row = $result->fetch_assoc()) {
    echo '<div class="imagem"><img src="' . $row["caminho_da_imagem"] . '" alt="Imagem"></div>';
  }
} else {
  echo "Nenhuma imagem encontrada.";
}

$conn->close();
?>