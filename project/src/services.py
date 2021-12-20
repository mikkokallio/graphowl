def resolve_path(path, data, value=None):
    """Fetch or set value from nested structure"""
    if path is None or len(path) == 0:
        if value is not None:
            data = value
        else:
            return data
    else:
        pointer = data
        for step in path[:-1]:
            if step in pointer or isinstance(step, int):
                pointer = pointer[step]
            elif value is not None:
                pointer[step] = {}
                pointer = pointer[step]
            else:
                return None
        if value is not None:
            pointer[path[-1]] = value
        else:
            return pointer[path[-1]]
