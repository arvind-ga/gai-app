FROM node:21.7.1-slim
FROM node:latest

WORKDIR /nextjs

## Set environment variables
ENV API_BASE_URL="http://localhost:8000/api/v1"
ENV NEXT_PUBLIC_API_KEY="bringthemhome"

RUN npm cache clean --force
COPY package*.json ./
RUN npm install js-cookie
RUN npm install axios
RUN npm install @mui/material @emotion/react @emotion/styled
RUN npm install @mui/icons-material
RUN npm install @mui/icons-material
RUN npm install react-hot-toast
RUN npm install react-query
RUN npm install tsparticles-slim
RUN npm install react-tsparticles
RUN npm install recharts
# RUN npm install --cache-dir /npm_cache
# RUN rm -rf node_modules package-lock.json

RUN npm install

## Copy the current directory contents into the container at /app
COPY . .

# Install any dependencies
# RUN npm install

# If you're building a static site or need to run a build script
RUN npm run build

# Expose the port your app runs on
EXPOSE 3000

# Define the command to run your app
CMD ["npm", "start"]


####### UPDATED ###############

# # Use a stable Node.js version
# FROM node:21.7.1-slim

# # Set the working directory in the container
# WORKDIR /nextjs

# # Copy package.json and package-lock.json into the container
# COPY package*.json ./

# # Install dependencies and clean the npm cache
# RUN npm install && npm cache clean --force

# # Copy the rest of the app's source code into the container
# COPY . .

# # Build the Next.js app (if building for production)
# RUN npm run build

# # Expose the port your app runs on
# EXPOSE 3000

# # Command to start the application
# CMD ["npm", "start"]


