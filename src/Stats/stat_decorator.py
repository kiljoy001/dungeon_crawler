class StatDecorator:
    @staticmethod
    def boost_stat(self, stat_name, boost_amount):
        def decorator(func):
            def wrapper(entity, *args, **kwargs):
                original_value = getattr(entity.stats, stat_name)
                boosted_value = original_value + boost_amount
                setattr(entity.stats, stat_name, boosted_value)
                try:
                    return func(entity, *args, **kwargs)
                finally:
                    setattr(entity.stats, stat_name, original_value)

            return wrapper

        return decorator

    @staticmethod
    def modify_damage_based_on_stat(stat_name, modifier_percentage):
        def decorator(func):
            def wrapper(entity, *args, **kwargs):
                stat_value = getattr(entity.stats, stat_name)
                additional_damage = stat_value * (modifier_percentage / 100)
                if 'damage' in kwargs:
                    original_damage = kwargs['damage']
                    updated_damage = original_damage + additional_damage
                    kwargs['damage'] = updated_damage
                    return func(entity, *args, **kwargs)
            return wrapper
        return decorator
