<html>

    <h2>SUMMER</h2>
    <h4>SUMMER C137</h4>

</html>

<?PHP

    $uploaddir = '/var/www/uploads/';

    if (!empty($_FILES['uploaded_file']))
    {

        $fname = $_FILES['uploaded_file']['name'];
        $ftype = $_FILES['uploaded_file']['type']; #MIME type
        $fsize = $_FILES['uploaded_file']['size']; #The size of the file in bytes
        $ftmp_name = $_FILES['uploaded_file']['tmp_name']; # The temporary filename in which the uploaded file was stored on the 

        $uploadfile = $uploaddir . basename($fname);
        

        if ($ftype != 'image/png') { 
            echo "<p>File '".$fname."' is not an image/png MIME type!!!</p>Your so lucky I don't care grandpa"; }
        }


        if (move_uploaded_file($ftmp_name, $uploadfile)) {
            echo "I guess this was some sort of Virus. Great grandpa - thanks!\n";
        } else {
            echo "<p>Something went wrong -.-</p>";
            echo 'Weitere Debugging Informationen: '; print_r($_FILES);
        }

?>




