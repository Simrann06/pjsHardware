<?php

$ID = $_POST['ID'];
$name = $_POST['name'];
$desc = $_POST['desc'];
$price = $_POST['price'];
$dept = $_POST['dept'];

$con=mysqli_connect("ns1.byethost7.org","jsphardw_admin","pz-;Ry,ePd%W","jsphardw_idkwhattoputhere");

mysqli_query($con,"INSERT INTO Product (Product_ID , Product_Name , Product_Description, Product_Price, Department_Name) VALUES ($ID, $name, $desc,$price, $dept);");

?>