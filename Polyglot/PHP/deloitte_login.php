<!-- We are sick and tired of these ninjas coming to perform pentests and picking apart our admin authentication system!!
First they complained we were using plaintext, then they complained about using MD5, next we needed to use salts, then we were giving away usernames in our error messages.. the list goes on!! Now they tell us usernames can be enumerated because the hash check takes more time when a user exists in the system vs when they do not, but we are only using these hashes because they made us!! I just finished updating the code so we compare against a dummy hash even when the admin user is incorrect, that way an attacker can not decipher the admin username. They better not come back to me again...
-->

<link rel="stylesheet" href="bootstrap.min.css">
<title>New login system test portal</title>
<div class="container" style="width:460px; margin-top:10px;">
<h2>New login system test portal</h2>
<hr>
<?php
    $admin_username = 'admin_42cebf16513c1898783d939b0afed141';
    // $6$ = CRYPT_SHA512
    $admin_password = '$6$rounds=10240$b2cdda324a52328c$30ZTp7tdJnmWC13wcF1OMCBKeA5Jk0ZILr9jIYdDUSudCGg20ktl3na72.9YSw19zoy56QcXlCmnJFJUDNzS1.';
    
    if(isset($_POST['user'],$_POST['pass'])){
        if (check_user_login_new(trim($_POST['user']),trim($_POST['pass']))){
            echo "<div class='alert alert-success' role='alert'><b>BAM:</b>" . $flag . "</div>";
        }
    }
    
    function generate_password($password){
        return crypt($password, '$6$rounds=10240$'.bin2hex(openssl_random_pseudo_bytes(32)));
    }
    
    function check_user_login_new($posted_username,$posted_password){
        global $admin_username, $admin_password;
        $logged_in = false;
        if ($posted_username === $admin_username){
            if (crypt($posted_password, $admin_password) === $admin_password){
                $logged_in = true;
            }
        } else { 
            $tmp_pass = generate_password(time()); // copied code to prevent against timing attacks on username
            if (crypt($posted_password, $tmp_pass) === $tmp_pass){ // prevent brute forcing admin password from login form
                $logged_in = true;
            }
        }
        return $logged_in;
    }
    
    function check_user_login_old($posted_username,$posted_password){
        global $admin_username, $admin_password;
        $logged_in = false;
        if ($posted_username === $admin_username){
            if (crypt($posted_password, $admin_password) === $admin_password){
                $logged_in = true;
            }
        }
        return $logged_in;
    }  
?>
<div class="well">
 <form role="form" method="post">
  <div class="form-group">
    <label for="user">Username</label>
    <input name="user" class="form-control" id="user">
    <br/>
    <label for="pass">Password</label>
    <input name="pass" class="form-control" id="pass" type="password">
  </div>
  <button type="submit" class="btn btn-default">Submit</button>
</form>
</div>
</div>
