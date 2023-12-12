FROM nginx:alpine
COPY /front/index.html /etc/nginx/html/index.html
COPY /front/styles.css /etc/nginx/html/styles.css
COPY /front/init-chart.js /etc/nginx/html/init-chart.js
COPY /front/nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-c", "/etc/nginx/nginx.conf"]