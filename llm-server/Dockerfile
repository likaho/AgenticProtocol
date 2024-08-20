# Use the node:20-alpine base image
FROM node:20-alpine
ENV NODE_TLS_REJECT_UNAUTHORIZED=0
WORKDIR /usr/src
COPY . .
RUN npm install
EXPOSE 3001
CMD ["npm", "start"]
