# Use the node:20-alpine base image
FROM node:20-alpine
WORKDIR /usr/src
COPY . .
RUN npm install
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
