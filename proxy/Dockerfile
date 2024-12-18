# use official image of nginx
FROM nginx:alpine

# Remove the default Nginx config
RUN rm /etc/nginx/conf.d/default.conf

# Create the directory for SSL certificates
RUN mkdir -p /etc/nginx/ssl

# copy your constum nginx config to container
COPY ./nginx.conf /etc/nginx/conf.d/
COPY ./ssl/mycert.cert /etc/nginx/ssl/mycert.cert
COPY ./ssl/mycert.prv /etc/nginx/ssl/mycert.prv

# Set appropriate permissions for SSL files (security best practice)
RUN chmod 600 /etc/nginx/ssl/mycert.cert /etc/nginx/ssl/mycert.prv
RUN test -f /etc/nginx/ssl/mycert.cert && test -f /etc/nginx/ssl/mycert.prv


# Expose port 80 for outside world
EXPOSE 80 443

# ENTRYPOINT /bin/sh -c "command"
# Start nginx when container starts
# CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
CMD ["nginx", "-c", "/etc/nginx/conf.d/nginx.conf", "-g", "daemon off;"]