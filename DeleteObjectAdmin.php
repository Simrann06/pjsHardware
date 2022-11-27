<?php

$attribute = $_POST['attribute1'];
$value = $_POST['value1'];

$con=mysqli_connect("ns1.byethost7.org","jsphardw_admin","pz-;Ry,ePd%W","jsphardw_idkwhattoputhere");

mysqli_query($con,"DELETE FROM Product WHERE $attribute = $value;");

?>