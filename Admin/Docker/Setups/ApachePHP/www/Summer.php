<html>

    <h2>SUUUMER</h2>
    <h4>SUMMER C137</h4>

</html>

<?PHP
    if (!empty($_FILES['uploaded_file']))
    {
        $fname = $_FILES['uploaded_file']['name'];
        $ftype = $_FILES['uploaded_file']['type']; #MIME type
        $fsize = $_FILES['uploadedfile']['size']; #The size of the file in bytes
        $ftmp_name = $_FILES['uploadedfile']['tmp_name']; # The temporary filename in which the uploaded file was stored on the 

        echo "<p>".$fname."</p>";
        if ($ftype != 'image/png') { echo "File Type '".$ftype."' not valid!!!"; }
        echo "<p>".$ftmp_name."</p>";
  }
?>




