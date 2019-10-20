# #!/bin/bash


# if [ "$1" = "--debug" ]
# then
# echo "Running in debug mode using waitress"
# waitress-serve --listen=localhost:8000 main:__hug_wsgi__

# else
# echo "Running production with gunicorn"
# gunicorn main:__hug_wsgi__
# fi