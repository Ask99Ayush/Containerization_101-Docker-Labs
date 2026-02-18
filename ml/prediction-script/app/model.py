def predict(value):
    value = float(value)

    if value > 50:
        return "High"
    elif value > 20:
        return "Medium"
    else:
        return "Low"