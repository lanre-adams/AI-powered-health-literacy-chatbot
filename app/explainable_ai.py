
import shap

def explain_prediction(model, input_data):
    explainer = shap.Explainer(model)
    shap_values = explainer(input_data)
    return shap_values
