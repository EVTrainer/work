FROM node:12
WORKDIR /usr/src/beetroot
COPY ./server/package*.json ./
RUN npm install
COPY ./server .
ENV PORT=8080
EXPOSE 8080
CMD [ "node", "." ]
