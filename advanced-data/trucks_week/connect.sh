# Connects to the database if .env is correctly set up
source .env
mysql -u $DB_USER -p$DB_PASSWORD -h $DB_HOST $DB_NAME -P $DB_PORT -D $DB_NAME