# Azure Deployment

To deploy a flask app on Azure cloud.

1. Get data through SQL query in Azure SQL database
2. Plot graph using this data
3. Show it through Azure App Service.


## User Manual

### Docker
Open Dockerfile 
1. Change Git a/c information with yours (line 18, 19)
2. **Optional:** Replace the volume directory path `/app` that needs to be mounted with yours (line 42) <br>

#### In your work directory terminal:

1. Type `docker image build -t image_name .` to build the image
2. Use `docker images` to check if the image is successfully built
3. To create a container, type the command below and modify accordingly the `-v` tag arguments in the format of `host_path:container_path` <br>
   `docker container run -it --name container_name -p 5000:5-000 -v ~/workspace/docker:/app -d image_name`
4. You can type `docker ps` to check if the container is successfuly created
5. Now you are inside the container
<br>

### Install ODBC driver in Docker container and pyodbc librairy
#### In your container terminal:
1. [Install Microsoft ODBC Driver for SQL Server on Ubuntu]
2. Install the pyodbc librairy by typing `pip3 install pyodbc`
<br>

### Display in local
1. Make changes to your web app, if needed
2. Type `flask run --host=0.0.0.0` to run the application
3. Open your broswer and go to <http://127.0.0.1:5000> to see the web app page. If neccessary, replace `127.0.0.1` with your localhost IP address.
<br>

### Deploy in Azure
**Note**: Before pushing to Azure App Service, make sure `pyodbc` is in the `requirements.txt` file. You can also type
          `pip freeze > requirements.txt` in your work directory terminal where you flask app is (either in local or Docker container) to update the `requirements.txt`
  
[Setup Azure App Service and deploy in Azure App Service]


### Note 1
#### If your container is stopped
1. Type `docker start container_name` to restart it
2. To execute the container, type `docker exec -it container_name bash`

#### Once you are inside the docker container
3. Type `flask run --host=0.0.0.0` to run the application

### Note 2
You can use [gitignore.io] to generate your own .gitignore file

[gitignore.io]: https://gitignore.io/
[Setup Azure App Service and deploy in Azure App Service]: https://medium.com/@nikovrdoljak/deploy-your-flask-app-on-azure-in-3-easy-steps-b2fe388a589e
[Install Microsoft ODBC Driver for SQL Server on Ubuntu]: https://docs.microsoft.com/fr-fr/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15
