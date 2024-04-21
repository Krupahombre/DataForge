def get_field_type(model_cls, field_name):
    return model_cls.__annotations__.get(field_name)