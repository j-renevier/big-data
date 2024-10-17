# Development

FROM node:18-alpine AS development

RUN echo Base image: node:18-alpine
RUN echo NODE_ENV: development

# Install nginx and supervisor
RUN apk update
RUN apk add nginx 

# Add nginx conf
RUN rm -f /etc/nginx/nginx.conf
ADD /conf/nginx/nginx.conf /etc/nginx/nginx.conf
RUN rm -f /etc/nginx/http.d/default.conf
ADD /conf/nginx/default.conf /etc/nginx/http.d/default.conf

# Add SSL certificates
RUN mkdir /etc/nginx/ssl
COPY /conf/ssl/nginx-selfsigned.crt /etc/nginx/ssl/nginx-selfsigned.crt
COPY /conf/ssl/nginx-selfsigned.key /etc/nginx/ssl/nginx-selfsigned.key

# Create necessary directories and set permissions
RUN mkdir -p /var/lib/nginx/logs /var/lib/nginx/tmp/client_body var/log/node var/log/nginx
RUN chown -R node:node /var/lib/nginx /var/log/nginx /var/lib/nginx/logs /run/nginx var/log/node


WORKDIR /var/www

COPY --chown=node:node package*.json ./
RUN npm ci

COPY --chown=node:node . .

# Copy the start script and make it executable
COPY /conf/start.sh /start.sh
RUN chmod +x /start.sh

ENTRYPOINT ["/start.sh"]


# Build

FROM node:18-alpine AS build

RUN echo Base image: node:18-alpine
RUN echo NODE_ENV: build

WORKDIR /var/www

COPY --chown=node:node package*.json ./
COPY --chown=node:node --from=dev /var/www/node_modules ./node_modules
COPY --chown=node:node . .

RUN npm run build

ENV NODE_ENV production

RUN npm ci --only=production && npm cache clean --force

USER node


# Production

FROM node:18-alpine AS production

RUN echo Base image: node:18-alpine
RUN echo NODE_ENV: production

# Install nginx and supervisor
RUN apk update
RUN apk add nginx 
RUN apk add supervisor

# Add nginx conf
RUN rm -f /etc/nginx/nginx.conf
ADD /conf/nginx/nginx.conf /etc/nginx/nginx.conf
RUN rm -f /etc/nginx/http.d/default.conf
ADD /conf/nginx/default.conf /etc/nginx/http.d/default.conf

# Add SSL certificates
RUN mkdir /etc/nginx/ssl
COPY /conf/ssl/nginx-selfsigned.crt /etc/nginx/ssl/nginx-selfsigned.crt
COPY /conf/ssl/nginx-selfsigned.key /etc/nginx/ssl/nginx-selfsigned.key


# Add supervisord conf
COPY /conf/supervisor/supervisord.conf /etc/supervisor/supervisord.conf
COPY /conf/supervisor/supervisor.conf /etc/supervisor/conf.d/supervisor.conf

# Create necessary directories and set permissions
RUN mkdir -p /var/log/supervisor /var/run/supervisor /var/lib/nginx/logs /var/lib/nginx/tmp/client_body var/log/node var/log/nginx
RUN chown -R node:node /var/log/supervisor /var/run/supervisor /var/lib/nginx /var/log/nginx /var/lib/nginx/logs /run/nginx var/log/node var/log/nginx

# Copy built files
WORKDIR /var/www
COPY --chown=node:node --from=build /var/www/node_modules ./node_modules
COPY --chown=node:node --from=build /var/www/dist ./dist

USER node

CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]