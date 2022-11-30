<?php

// Connect to the MySQL database
$connect = mysqli_connect('localhost', 'jsphardw_manager', 'zl4.N@_rF@Qe', 'jsphardw_idkwhattoputhere');

// If the connection did not work, display an error message
if (!$connect) 
{
    echo 'Error Code: ' . mysqli_connect_errno() . '<br>';
    echo 'Error Message: ' . mysqli_connect_error() . '<br>';
    exit;
}

?>
<!doctype html>
<html>
    <head>
        <title>PHP amd MySQL</title>
    </head>
    <body>

        <h1>PHP and MySQL</h1>

        <?php

        // Create a query
        $query = 'SELECT * FROM Product WHERE Department_Name = "GPU"';

        // Execute the query
        $result = mysqli_query($connect, $query);

        // If there is no result, display an error message
        if (!$result)
        {
            echo 'Error Message: ' . mysqli_error($connect) . '<br>';
            exit;
        }

        // Loop through the records found
        while ($record = mysqli_fetch_assoc($result))
        {

            // Output the record using if statements and echo
            echo '<h2>';

            if ($record['Product_Name'])
            {
                echo '<p>' . $record['Product_Name'] . '</p>';
            }

            if ($record['Product_Description'])
            {
                echo '<p>' . $record['Product_Description'] . '</p>';
            }

            if ($record['Product_Price'])
            {
                echo '<p>' . $record['Product_Price'] . '</p>';
            }

            if ($record['Department_Name'])
            {
                echo '<p>' . $record['Department_Name'] . '</p>';
            }
            echo '<h2>';        

        }

        ?>
    </body>
</html>