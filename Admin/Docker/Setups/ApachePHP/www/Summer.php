<h2>SUUUMER</h2>

<h4>SUMMER C137</h4>

<?PHP
    if(!empty($_FILES['uploaded_file']))
    {
        $name = $_FILES['uploaded_file']['name'];
        echo "<p>".$name."</p>";
  }
?>




