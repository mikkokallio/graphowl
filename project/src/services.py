def resolve_path(path, data, value=None):
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
