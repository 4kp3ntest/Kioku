# Setup & Tools
## Composer as equivalent to pip
use download_composer.sh to download
## Psysh as equivalent to Ipython
Does not work via Git
    - git clone https://github.com/bobthecow/psysh.git
    - in psysh: composer install
Works:
composer require psy/psysh:@stable
composer g require psy/psysh:@stable #for global

# MISC
.phar - php archive
.php simply use html in it
.html PHP in it -> .htaccess file
print & echo write to php://output not to php://stdout

$_GET
$_POST -> has to load a new page to provide input to PHP function (without AJAX/JavaScript)


Superglobals
