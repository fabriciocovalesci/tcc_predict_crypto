from app.blueprints.home_blueprint import home


def init_app(app):
    app.register_blueprint(home)

# @app .route("/katana-ml/api/v1.0/forecast/ironsteel", métodos=['POST']) 
# def predict(): 
#     horizon = int(request.json['horizon']) 
# https://towardsdatascience.com/serving-prophet-model-with-flask-predicting-future-1896986da05f
#     future2 = m2.make_future_dataframe(periods=horizon) 
#     forecast2 = m2.predict(future2) 
    
#     data = forecast2[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-horizon:] 
    
#     ret = data.to_json(orient ='records', date_format='iso') 
    
#     return ret