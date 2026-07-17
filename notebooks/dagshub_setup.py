import dagshub
import mlflow

mlflow.set_tracking_uri("https://dagshub.com/jaymavani16/mini_project_mlflow.mlflow")
dagshub.init(repo_owner='jaymavani16', repo_name='mini_project_mlflow', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)