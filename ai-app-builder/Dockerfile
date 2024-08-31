# Build local monorepo image
# docker build --no-cache -t  flowise .

# Run image
# docker run -d -p 3000:3000 flowise

FROM node:20-alpine
# ENV NODE_TLS_REJECT_UNAUTHORIZED=0
# RUN apk add --update libc6-compat python3 make g++
# needed for pdfjs-dist
# RUN apk add --no-cache build-base cairo-dev pango-dev

# Install Chromium
# RUN apk add --no-cache chromium

#install PNPM globaly
RUN apk --no-cache add curl
RUN npm install -g pnpm@9.4.0

ENV PUPPETEER_SKIP_DOWNLOAD=true
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser

ENV NODE_OPTIONS=--max-old-space-size=8192

WORKDIR /usr/src

# Copy app source
COPY . .

RUN pnpm install

RUN pnpm build

EXPOSE 3031

CMD [ "pnpm", "start" ]