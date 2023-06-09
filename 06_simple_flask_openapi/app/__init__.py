import connexion
from .flask_request_intercepts import flask_intercepts

# Create the application instance
app = connexion.FlaskApp(__name__, specification_dir='./openapi')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yaml', validate_responses=False)
handlers = flask_intercepts(app)

