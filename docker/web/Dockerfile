FROM nginx:alpine

COPY conf/nginx/conf.d/ /etc/nginx/conf.d/

COPY /public /usr/share/nginx/html/

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]