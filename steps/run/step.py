import logging
from relay_sdk import Interface, Dynamic as D

relay = Interface()

name = relay.get(D.name)

params = None
params_array = None

# if `parameters` is defined, `parameters_array` is ignored
try:
  params = relay.get(D.parameters)
except:
  try:
    params_array = relay.get(D.parameters_array)
  except:
    params = {}

if params_array:
  logging.debug(f'Iterating workflow {name} over params array {params_array}')
  #TODO some throttling or limitation
  for params in params_array:
    relay.workflows.run(name, params)
else:
    logging.debug(f'Running workflow {name} with params {params}')
    relay.workflows.run(name, params)
