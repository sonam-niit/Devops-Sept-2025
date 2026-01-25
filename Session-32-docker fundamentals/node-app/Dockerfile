# Base Image
FROM node:22-alpine 
# Set working directory
WORKDIR /app
# copy package.json
COPY package.json .
# install dependencies
RUN npm install
# Copy other files and folders
COPY . .
# EXPOSE port
EXPOSE 3000

# RUN app
CMD [ "node" , "index.js" ]
