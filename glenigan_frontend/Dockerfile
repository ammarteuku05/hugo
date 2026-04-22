# ==============================
# Stage 1: Build TypeScript
# ==============================
FROM node:18-alpine AS build-stage

WORKDIR /app

COPY package*.json ./
# Only install dev dependencies needed to compile; they won't go to production
RUN npm ci --include=dev

COPY tsconfig.json ./
COPY src/ ./src/
RUN npm run build

# ==============================
# Stage 2: Serve with Nginx
# ==============================
FROM nginx:alpine

# Only copy the essential static files – no node_modules, no source TS
COPY index.html styles.css /usr/share/nginx/html/
COPY src/templates/ /usr/share/nginx/html/src/templates/
COPY --from=build-stage /app/dist/ /usr/share/nginx/html/dist/

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
