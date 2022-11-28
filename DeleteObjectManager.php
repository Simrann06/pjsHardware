<?php

$attMan = $_POST['attMan'];
$valMan = $_POST['valMan'];

$con=mysqli_connect("ns1.byethost7.org","jsphardw_manager","zl4.N@_rF@Qe","jsphardw_idkwhattoputhere");

mysqli_query($con,"DELETE FROM Product WHERE $attMan = $valMan;");

?>