FROM node:latest as build
WORKDIR /app
COPY ./ /app
RUN npm install
EXPOSE 3000
CMD ["npm", "run", "dev"]