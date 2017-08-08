# projectcars

Requirements:
- Python 2.7.13
- git
- mysql-connector-c (brew install mysql-connector-c) (see if errors later check: https://stackoverflow.com/questions/43543483/pip-install-mysql-python-fails-with-indexerror)

Instructions:
1. Clone https://github.com/merialc/projectcars and navigate to root
2. pip install -r requirements.txt
3. MYSQL_HOST=test-aws-db.cz4w5vyskqrw.eu-west-1.rds.amazonaws.com MYSQL_USER=admin MYSQL_PASSWORD=lake-ARMS-soil-SEEDS python mysql.py
