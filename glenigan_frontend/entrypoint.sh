#!/bin/sh

# Default to localhost if not provided
if [ -z "$BACKEND_URL" ]; then
  BACKEND_URL="http://localhost:8000"
fi

echo "Setting BACKEND_URL to $BACKEND_URL"

# Replace the placeholder in the compiled JS file
sed -i "s|__BACKEND_URL_PLACEHOLDER__|$BACKEND_URL|g" /usr/share/nginx/html/dist/app.js

# Start Nginx
exec nginx -g "daemon off;"
