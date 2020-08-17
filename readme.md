## Django + Celery Deployment


### FOUR TERMINALS

#### 1. Start Django Server
python manage.py runserver

<br> 

#### 2. Start Redis Server (version > 2.6)
redis-server

<br> 

### 3. Run Celery Schedule
celery -A news_scraper beat -l info 

<br> 

#### 3. Run Celery Worker
celery -A news_scraper worker -l info 

<br> 

#### 4. Flower Celery Monitoring
flower -A news_scraper --port=5555

<br> 



#### Windows 10 Celery 4.0 workaround
Add to Windows Env: <br>
Variable name: FORKED_BY_MULTIPROCESSING <br>
Variable value: 1



##### Redis CLI
redis-cli