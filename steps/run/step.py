import logging
from relay_sdk import Interface, Dynamic as D

relay = Interface()

name = relay.get(D.name)

params = None
param_sets = None

# if `parameters` is defined, `parameterSets` is ignored
try:
    params = relay.get(D.parameters)
except OSError:
    try:
        param_sets = relay.get(D.parameterSets)
    except OSError:
        params = {}

if param_sets:
    logging.debug(
        f'Iterating workflow {name} over params array {param_sets}')
    for params in param_sets:
        relay.workflows.run(name, params)
else:
    logging.debug(f'Running workflow {name} with params {params}')
    relay.workflows.run(name, params)
