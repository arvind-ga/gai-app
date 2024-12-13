FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1  
ENV PYTHONUNBUFFERED=1         
# ENV TZ=UTC                    
# ENV ALLOWED_ORIGINS="http://4.240.79.122:3000,http://localhost:3000"

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt 
    # && \
    # ln -sf /usr/share/zoneinfo/$TZ /etc/localtime && \
    # echo $TZ > /etc/timezone

# Copy only necessary application files
COPY . /app/

# Expose necessary ports
EXPOSE 3000  
EXPOSE 8000  
EXPOSE 6379 6380
EXPOSE 587 
EXPOSE 27017

# Run the container with multiple workers
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]







# # Use an official Python runtime as a parent image
# FROM python:3.11-slim

# # Set environment variables
# # Don't write byte code files to disk
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV TZ=UTC

#  # Unbuffered output for easier container logging
# ENV PYTHONUNBUFFERED 1

# ENV ALLOWED_ORIGINS="http://4.240.79.122:3000,http://localhost:3000"

# # Set the working directory in the container
# WORKDIR /app

# # Install dependencies
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir --upgrade pip && \
#     pip install --no-cache-dir -r requirements.txt \
#     && ln -sf /usr/share/zoneinfo/$TZ /etc/localtime \
#     && echo $TZ > /etc/timezonexx

# # Copy the current directory contents into the container at /app
# COPY .. /app


# ## Copy the entrypoint script into the container
# #COPY entrypoint.sh /usr/local/bin/
# #
# ## Make sure the script is executable
# #RUN chmod +x /usr/local/bin/entrypoint.sh
# #
# #ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# ## Command to run the application
# #CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
# EXPOSE 80
# EXPOSE 80/tcp
# EXPOSE 587
# EXPOSE 3000
# EXPOSE 6379
# EXPOSE 6380
# EXPOSE 8000
# EXPOSE 10255
# EXPOSE 27017



# ## Run the container with multiple workers instead if needed.
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]