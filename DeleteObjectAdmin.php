<?php

$antNum = $_POST['antNum'];
$antRate = $_POST['antRate'];

$con=mysqli_connect("localhost","root","pass","login");

mysqli_query($con,"UPDATE userdata SET `antNum`='$antNum' , `antRate`='$antRate' WHERE `player`='bob'");

?>