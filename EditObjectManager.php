<?php

$attribute1 = $_POST['attribute1'];
$value1 = $_POST['value1'];
$attribute2 = $_POST['attribute2'];
$value2 = $_POST['value2'];



$con=mysqli_connect("ns1.byethost7.org","jsphardw_manager","zl4.N@_rF@Qe","jsphardw_idkwhattoputhere");

mysqli_query($con,"UPDATE Product SET $attribute1 = $value1 WHERE $attribute2 = $value2;");

?>