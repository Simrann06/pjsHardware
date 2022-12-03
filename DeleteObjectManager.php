<?php



// Jake 




$attMan = $_POST['attMan'];
$valMan = $_POST['valMan'];


$servername = "localhost";
$username = "jsphardw_admin";
$password = "pz-;Ry,ePd%W";
$dbname = "jsphardw_idkwhattoputhere";

$conn = new mysqli($servername, $username, $password, $dbname);

$con=mysqli_connect("ns1.byethost7.org","jsphardw_manager","zl4.N@_rF@Qe","jsphardw_idkwhattoputhere");

mysqli_query($con,"DELETE FROM Product WHERE $attMan = $valMan;");

?>