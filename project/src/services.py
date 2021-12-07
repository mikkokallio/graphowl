def resolve_path(path, data, value=None):
    pointer = data
    for step in path[:-1]:
        pointer = pointer[step]
    if value:
        pointer[path[-1]] = value
    else:
        return pointer[path[-1]]
