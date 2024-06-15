# create virtual environment
python3 -m venv project2-buidling-cicd/venv
source project2-buidling-cicd/venv/bin/activate

cd project2-buidling-cicd

# script to install dependencies & run test
make all

# deploy to webapp (using ypthon 3.9 to avoid version conflicts of dependencies)
az webapp up --name udacity-project2-cicd --resource-group tungtt44-project2-cicd --location eastus --runtime "PYTHON|3.9" --sku B3

# making prediction in azure webapp
source make_predict_azure_app.sh