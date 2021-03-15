class Utils:

    @staticmethod
    def compare_data_types(dict_object, key, data_type):
        if isinstance(dict_object[key], data_type):
            print('\033[92m Key "{}" with "{}" value is of {} type \033[0m'.format(key, dict_object[key], data_type))
        else:
            print('\033[91m Key "{}" with "{}" value is of {} instead of {} expected type \033[0m'.format(
                key, dict_object[key], type(dict_object[key]), data_type))
