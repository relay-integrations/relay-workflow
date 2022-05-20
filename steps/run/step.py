import logging
import json
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
    logging.info(
        f'Iterating workflow {name} over params array {param_sets}')
    for params in param_sets:
        resp = relay.workflows.run(name, params)
        logging.info(json.dumps(resp, indent=2))
        run = resp['workflow_run']
        relay.decorators.set_link(
            f'{run["run_number"]:03d}', # add leading zeros for proper ordering in the UI # noqa E501
            f'Run {run["run_number"]:03d}',
            run['app_url']
        )

else:
    logging.info(f'Running workflow {name} with params {params}')
    resp = relay.workflows.run(name, params)
    logging.info(json.dumps(resp, indent=2))
    run = resp['workflow_run']
    relay.decorators.set_link(
        f'{run["run_number"]:03d}', # add leading zeros for proper ordering in the UI # noqa E501
        f'Run {run["run_number"]:03d}',
        run['app_url']
        )
