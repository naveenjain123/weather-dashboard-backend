
mkdir -p /var/log/gunicorn
touch /var/log/gunicorn/debug.log

#Run Gunicorn for this project
nohup gunicorn backend.wsgi:application --name cnext --timeout 300 --workers=2 --threads=4 --worker-class=gthread --bind=0.0.0.0:8080 --log-level=Info --error-logfile /var/log/gunicorn/debug.log --log-file /var/log/gunicorn/debug.log --capture-output  &
tail -f /var/log/gunicorn/*
