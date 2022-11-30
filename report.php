<?php

$val = $_POST['val'];

$servername = "localhost";
$username = "jsphardw_admin";
$password = "pz-;Ry,ePd%W";
$dbname = "jsphardw_idkwhattoputhere";

$conn = new mysqli($servername, $username, $password, $dbname);

$sql =("SELECT * FROM Product");

$result = $conn->query($sql);
if ($result->num_rows > 0) {
      while($row = $result->fetch_assoc()) {
        echo "id: " . $row["id"]. " - Name: " 
            . $row["firstname"]. " " . $row["lastname"]. "<br>";
      }
} 
else {
      echo "Error";
}
$conn->close();

?>