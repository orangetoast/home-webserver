FROM nginx:stable-alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY ./ssl/* /etc/nginx
EXPOSE 80
EXPOSE 443
CMD ["nginx", "-g", "daemon off;"]