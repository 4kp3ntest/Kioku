<html>

    <h2>MOOORTY</h2>
    <h4>MORTY C137</h4>

</html>


<?php

    echo "<p>Aah.. uuh Rick.. you think this is right?</p>";
    if (!empty($_POST["command"])) {
        echo "<p>I'm pretty sure I cannot ".$_POST["command"]."</p>";
    }
?>
