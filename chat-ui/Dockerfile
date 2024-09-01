# Use the node:20-alpine base image
FROM node:20-alpine
# Install curl
RUN apk --no-cache add curl
WORKDIR /usr/src
COPY . .
RUN npm install && npm run build
EXPOSE 3000
CMD ["npm", "start"]