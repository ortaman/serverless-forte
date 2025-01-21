## Transactions challenge
This project is based in {Serverless Clean Architecture}(https://blog.serverlessadvocate.com/serverless-clean-architecture-code-with-domain-driven-design-852796846d28)
This is a sample template for the proyect - Below is a brief explanation of the struct:

```bash
.
├── forte-app               <-- Source code for a lambda function
│   └── forte-api           <-- Source code for based in Serverless Clean Architecture
│       ├── infra           <-- Infrastucture variables
│       ├── adapters        <-- Lambda function code
│       ├── usecases        <-- This layer holds the business logic of our application
│       ├── repository      <-- This layer is responsible for communicating with data sources, whether it is Database, another services, or external APIs
│       ├── utils           <-- Collection of small common functions, data and templates
│       └── serveless.yml   <-- Specifies the infrastructure components 
├── local-db                <-- Folder with file to inicialize mongod and folter to save mondodb volume data
├── .gitignore              <-- Ignore the files and directories which are unnecessary to project 
├── docker-compose.yml      <-- Configuration to run local Mongo database container
└── Readme.md               <-- Documentation file 
```


## Requirements

* [Docker installed](https://www.docker.com/get-started/)
* [Node.js](https://nodejs.org/en/download)
* [Serverless framework with AWS](https://www.serverless.com/framework/docs/getting-started#setting-up-serverless-framework-with-aws)
* AWS CLI already configured with Administrator permission (to deploy)
* You must have installed Python 3.12 to run in local


### Local development

Thanks to capabilities of `serverless-wsgi`, it is also possible to run your application locally, however, in order to do that, you will need to first install `werkzeug` dependency, as well as all other dependencies listed in `requirements.txt`. It is recommended to use a dedicated virtual environment for that purpose. You can install all needed dependencies with the following commands:

```
cd serverless-forte                       

pip install werkzeug
pip install -r forte-app/requirements.txt
```
 
Run the mongodb docker container:

```
cd serverless-forte
docker compose up
```


At this point, you can run your application locally with the following command:

```
cd serverless-forte/forte-app
serverless wsgi serve
```

Then you can run Mongo Express to check the local database in the next URL
```
http://localhost:8081/db/forte-db/transactions?skip=0&key=&value=&type=&query=&projection=
```

After successful run application locally, you can call the created application via CURL:

```
curl -X GET http://localhost:5000/transactions
curl -X GET http://localhost:5000/transactions/bd7b69fa-9207-4996-91cd-b7eec3fce21a

curl  -X POST http://localhost:5000/transaction -H "Content-Type: application/json" --DATA '{"transaction_id": "bd7b69fa-9207-4996-91cd-b7eec3fce11y", "customer_id": "bd7b69fa-9207-4996-91cd-b7eec3fce21z", "amount": 50.11,"category": "c1", "type": "income", "deactivated": false, "date": "2025-01-15T18:28:55Z"}'

curl  -X PUT http://localhost:5000/transaction/bd7b69fa-9207-4996-91cd-b7eec3fce11y -H "Content-Type: application/json" --DATA '{"amount":22.22,"category":"cat_update"}'
curl  -X DELETE http://localhost:5000/transaction/bd7b69fa-9207-4996-91cd-b7eec3fce11y


curl -X GET "http://localhost:5000/transactions/resume?start_date=2025-01-01&end_date=2025-01-31"
```

### Deployment

This example is made to work with the Serverless Framework dashboard, which includes advanced features such as CI/CD, monitoring, metrics, etc.

In order to deploy with dashboard, you need to first login with:

```
serverless login
```

install dependencies with:

```
npm install
```

and

```
pip install -r requirements.txt
```

and then perform deployment with:

```
serverless deploy
```

After running deploy, you should see output similar to:

```
Deploying "aws-python-flask-api" to stage "dev" (us-east-1)

Using Python specified in "runtime": python3.12

Packaging Python WSGI handler...

✔ Service deployed to stack aws-python-flask-api-dev (104s)

endpoints:
  GET - https://xxxxxxxxxe.execute-api.us-east-1.amazonaws.com/dev/
  ANY - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/{proxy+}
functions:
  api: aws-python-flask-api-dev-api (41 MB)

```

_Note_: In current form, after deployment, your API is public and can be invoked by anyone. For production deployments, you might want to configure an authorizer. For details on how to do that, refer to [http event docs](https://www.serverless.com/framework/docs/providers/aws/events/apigateway/).

### Invocation

After successful deployment, you can call the created application via HTTP:

```
curl https://xxxxxxx.execute-api.us-east-1.amazonaws.com/dev/
```

Which should result in the following response:

```json
{ "message": "¡Hello FORTE!" }
```
