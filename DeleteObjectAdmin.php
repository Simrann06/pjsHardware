<?php

$att = $_POST['att'];
$val = $_POST['val'];

$con=mysqli_connect("ns1.byethost7.org","jsphardw_admin","pz-;Ry,ePd%W","jsphardw_idkwhattoputhere");

mysqli_query($con,"DELETE FROM Product WHERE $att = $val;");

?>