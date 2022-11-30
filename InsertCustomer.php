<?php

$ID = rand(100000,999999);
$name = $_POST['name'];
$email = $_POST['email'];
$phone = $_POST['phone'];
$addr = $_POST['addr'];
$city = $_POST['city'];
$zip = $_POST['zip'];
$state = $_POST['state'];
$card_name = $_POST['card_name'];
$card_num = $_POST['card_num'];
$Exp_month = $_POST['Exp_month'];
$Exp_year = $_POST['Exp_year'];
$cvv = $_POST['cvv'];



$servername = "localhost";
$username = "jsphardw_admin";
$password = "pz-;Ry,ePd%W";
$dbname = "jsphardw_idkwhattoputhere";

$conn = new mysqli($servername, $username, $password, $dbname);

$stmt = $conn->prepare("INSERT INTO Customer (Customer_ID , Customer_Name , Customer_Email, Customer_Phone, Customer_Address, Customer_City, Customer_Zip, Customer_State, Card_Name, Credit_Card_Number, Exp_Month, Exp_Year, CVV) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)");

$stmt->bind_param("isssssisssiii", $ID, $name ,$email ,$phone,$addr ,$city ,$zip ,$state,$card_name ,$card_num ,$Exp_month, $Exp_year ,$cvv );

try {  
        $stmt->execute();  
        echo "success";
        echo "<br>";
        echo $ID;
        echo "<br>";
        echo $name;
        echo "<br>";
        echo $email ;
        echo "<br>";
        echo $phone;
        echo "<br>";
        echo $addr ;
        echo "<br>";
        echo $city;
        echo "<br>";
        echo $zip ;
        echo "<br>";
        echo $state ;
        echo "<br>";
        echo $card_name ;
        echo "<br>";
        echo $card_num ;
        echo "<br>";
        echo $Exp_month;
        echo "<br>";
        echo $Exp_year; 
        echo "<br>";
        echo $cvv;


    }  
catch (Exception $e) {  
        echo $e;
    }  


$stmt->close();
$conn->close();

?>

