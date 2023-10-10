from apiflask import APIFlask

app = APIFlask(__name__, spec_path='/index.yaml')
app.config['SPEC_FORMAT'] = 'yaml'


