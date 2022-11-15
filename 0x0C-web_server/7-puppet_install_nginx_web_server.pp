# This file install nginx on a new web server
exec {'update apt':
    command => 'sudo apt update',
    path    => '/usr/bin'
}

exec {'install nginx':
    command => 'sudo apt -y install nginx',
    path    => '/usr/bin'
}

exec {'update firewall settings':
    command => 'sudo ufw allow \'Nginx HTTP\'',
    path    => '/usr/bin'
}

exec {'custom home page':
    command => 'echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html',
    path    => '/usr/bin/'
}

exec {'redirection':
    command => 'sudo sed -i \'50i\\\t\trewrite ^/redirect_me https://iamprosper.github.io permanent;\' /etc/nginx/sites-available/default',
    path    => '/usr/bin'
}

exec {'restart the server':
    command => 'sudo service nginx restart',
    path    => '/usr/bin'
}

