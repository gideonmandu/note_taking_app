FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install yarn -g
RUN npm install @vue/cli@4.5.13 -g

COPY package.json .
COPY yarn.lock .
RUN yarn install

CMD ["yarn", "serve"]