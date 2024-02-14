# Fixing Apache is returning a 500 error using `strace`.

exec { 'fix_wordpress':
  command => 'sudo sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
