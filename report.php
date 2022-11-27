<?php
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


$sql = mysql_query($conn,"SELECT name, rating FROM table ORDER BY rating DESC LIMIT 5;");

$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "Provider: " . $row["name"]. " - Rating: " . $row["rating"]. "<br>";
    }
} else {
    echo "0 results";
}
$conn->close();

?>