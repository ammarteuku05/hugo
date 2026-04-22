FROM nginx:alpine

# Copy static files to nginx directory
COPY . /usr/share/nginx/html/

# Copy entrypoint script and make it executable
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Remove the node_modules and other dev files if they were copied
RUN rm -rf /usr/share/nginx/html/node_modules \
    /usr/share/nginx/html/package.json \
    /usr/share/nginx/html/tsconfig.json

EXPOSE 80

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
