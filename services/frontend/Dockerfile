FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli -g

COPY package.json .
COPY yarn.lock .

RUN npm install

CMD [ "npm", "run", "serve" ]
# RUN npm install -g -f yarn
# RUN yarn global add @vue/cli
# RUN yarn install --prod

# CMD ['yarn', 'serve']
