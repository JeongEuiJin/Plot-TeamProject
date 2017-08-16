FROM        hehar1020/eb_ubuntu
MAINTAINER  hehar1020@gmail.com

# 현재경로의 모든 파일들을 /srv/Deploy-PlotTP 폴더로 복사
COPY        . /srv/Deploy-PlotTP

# cd /srv/Deploy-PlotTP 같은 효과
WORKDIR     /srv/Deploy-PlotTP

# requirements 설치
RUN         /root/.pyenv/versions/Deploy-PlotTP/bin/pip install -r .requirements/deploy.txt

# supervisor 파일 복사
COPY        .config/supervisor/uwsgi.conf /etc/supervisor/conf.d
COPY        .config/supervisor/nginx.conf /etc/supervisor/conf.d

# nginx 파일 복사
COPY        .config/nginx/nginx.conf /etc/nginx/nginx.conf
COPY        .config/nginx/nginx-app.conf /etc/nginx/sites-available/nginx-app.conf
RUN         rm -rf /etc/nginx/sites-enabled/default
RUN         ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx-app.conf

# static 파일 복사
RUN         /root/.pyenv/versions/Deploy-PlotTP/bin/python /srv/Deploy-PlotTP/django-app/manage.py collectstatic --settings=config.settings.deploy --noinput


CMD         supervisord -n

EXPOSE      80 8000 8080