FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json .
COPY yarn.lock .

RUN npm install -g -f yarn
RUN yarn global add @vue/cli
RUN yarn install --prod

CMD ['yarn', 'serve']
