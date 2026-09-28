from flask import Flask,jsonify
from config import config
from routes import demo_routes,items_routes

app=Flask(__name__)
app.config.from_object(config)

@app.route("/")
def home():
    return jsonify ({"msg": "welcome"})

app.register_blueprint(demo_routes.demo_routes,url_prefix="/api/v1")
app.register_blueprint(items_routes.items_routes,url_prefix="/api/v2")

if __name__=="__main__":
    app.run()