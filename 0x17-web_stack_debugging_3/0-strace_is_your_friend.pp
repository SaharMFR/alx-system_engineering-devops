# Fixing Apache is returning a 500 error using `strace`.

exec { 'fix_wordpress':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
