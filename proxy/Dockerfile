# use official image of nginx
FROM nginx:alpine

# Remove the default Nginx config
RUN rm /etc/nginx/conf.d/default.conf

# copy your constum nginx config to container
COPY ./nginx.conf /etc/nginx/conf.d/

# Expose port 80 for outside world
EXPOSE 80

# ENTRYPOINT /bin/sh -c "command"
# Start nginx when container starts
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
# CMD ["nginx" "-g", "daemon off;"]
#CMD ["/bin/sh", "-c", "[\"nginx\", \"-g\", \"daemon\\ off;\"]"x