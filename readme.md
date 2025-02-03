# ⚽ Football Top Scorer Data Pipeline

This project fetches top scorer data from a football API, processes it, and stores it in a MySQL database. It also provides a web interface using phpMyAdmin to view the data.

## 📋 Prerequisites

- 🐳 Docker
- 🐳 Docker Compose
- 🐍 Python 3.8+
- 📦 pip

## 🛠️ Setup

### 1. 📂 Clone the Repository

```sh
git clone https://github.com/yourusername/football-top-scorer.git
cd football-top-scorer
```

### 2. ⚙️ Create and Configure Environment Variables

Create a `.env` file in the root directory of the project and add the following variables:

```properties
RAPIDAPI_KEY='your_rapidapi_key'
URL="https://v3.football.api-sports.io/players/topscorers"

# MYSQL
HOST_NAME='localhost'
DOCKER_CONTAINER='football_mysql'
MYSQL_ROOT_PASSWORD='root'
MYSQL_DATABASE='football_stats'
MYSQL_USER='football_admin'
MYSQL_PASSWORD='football_pass'
HOST_PORT='3306'

# PHPMYADMIN
PHPMYADMIN_PORT='8080'
```

Replace `your_rapidapi_key` with your actual RapidAPI key.

### 3. 🐳 Build and Run Docker Containers

```sh
docker-compose up -d
```

This command will start MySQL and phpMyAdmin containers.

### 4. 📦 Install Python Dependencies

#### On macOS/Linux

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### On Windows

```sh
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 5. 🚀 Run the Data Pipeline

```sh
python main.py
```

This will fetch the top scorer data, process it, and insert it into the MySQL database.

## 🌐 Access phpMyAdmin

You can access phpMyAdmin to view the data at `http://localhost:8080`. Use the MySQL credentials specified in the `.env` file to log in.

## 🛑 Stopping the Containers

To stop the Docker containers, run:

```sh
docker-compose down
```

## 🐞 Troubleshooting

- Ensure Docker and Docker Compose are installed and running.
- Verify that the `.env` file is correctly configured.
- Check the logs for any errors using `docker-compose logs`.

## 📜 License

This project is licensed under the MIT License.

## 🙏 Acknowledgements

This project is inspired by [Stephen David Williams](https://stephendavidwilliams.com/rest-api-to-mysql-database-using-python#heading-preface). You can find his GitHub repository [here](https://github.com/sdw-online/code_examples_library/blob/7ac1366aefa3c551290a46291897e4fc7ba56261/python/articles/rest_api__to_mysql/demo.py).