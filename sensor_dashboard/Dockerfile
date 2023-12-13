# Dockerfile for Angular web app
FROM node:14 AS builder

WORKDIR /app

COPY sensor-dashboard/package*.json ./
RUN npm install

COPY sensor-dashboard/ ./
RUN npm run build

FROM nginx:1.21

COPY --from=builder /app/dist/sensor-dashboard /usr/share/nginx/html

