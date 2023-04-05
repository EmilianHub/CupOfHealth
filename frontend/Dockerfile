FROM node:16.13.0
WORKDIR /api
COPY package*.json ./
RUN npm install
EXPOSE 3000
CMD ["npm", "start"]