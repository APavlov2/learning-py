# Vendor Build Stage
FROM python:3.11-slim as vendor

LABEL maintainer="APavlov2"
LABEL description="learnin-py"

WORKDIR /var/www

# install dependencies 
# RUN composer install \
#     --ignore-platform-reqs \
#     --no-interaction \
#     --no-plugins \
#     --no-scripts \
#     --prefer-dist

# Node Build Stage
# FROM node:20-alpine3.19 as frontend

# COPY package.json package-lock.json /var/www/html/
# COPY --from=vendor /var/www/vendor/ /var/www/vendor/

# WORKDIR /var/www/html

# RUN npm ci && npm run production

# App Build Image
FROM python:3.11-slim as AppImage

#set our application folder as an environment variable
ENV APP_HOME /var/www/html

# COPY --from=frontend /usr/local/lib/node_modules /usr/local/lib/node_modules
# COPY --from=frontend /usr/local/bin/node /usr/local/bin/node
# RUN ln -s /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm

# RUN npm i -g auth0-deploy-cli@7.24.1

COPY . /var/www/html

# Install system dependencies
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    pip install -r $APP_HOME/requirements.txt 

# COPY --from=vendor /var/www/vendor/ $APP_HOME/vendor/
# COPY --from=vendor /usr/bin/composer /usr/bin/composer
# COPY --from=frontend /var/www/html/public/css $APP_HOME/public/css
# COPY --from=frontend /var/www/html/public/js $APP_HOME/public/js
# COPY --from=frontend /var/www/html/public/mix-manifest.json $APP_HOME/public/mix-manifest.json

# Add a non-root user to prevent files being created with root permissions on host machine.
ENV USER=learningpy
ENV UID 1000
ENV GID 1000

RUN rm -rf /usr/local/lib/node_modules/npm/node_modules/opener \
    && addgroup --gid "$GID" "$USER" \
    && adduser \
    --disabled-password \
    --gecos "" \
    --home "$(pwd)" \
    --ingroup "$USER" \
    --no-create-home \
    --uid "$UID" \
    "$USER" \
    && chown -R $USER:$GID /var/www/html

# Set working directory
WORKDIR /var/www/html

USER $USER

CMD ["python", "server.py"]
