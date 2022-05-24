import sys
import logging
from relay_sdk import Interface, Dynamic as D

relay = Interface()

name = relay.get(D.name)

params = None
param_sets = None

# if `parameters` is defined, `parameterSets` is ignored
try:
    param_sets = [relay.get(D.parameters)]
except OSError:
    try:
        param_sets = relay.get(D.parameterSets)
    except OSError:
        logging.error('Need to pass `parameters` or `parameterSets`')
        sys.exit(1)

if len(param_sets) > 1:
    logging.info(f'Iterating workflow {name} over params array {param_sets}')
else:
    logging.info(f'Running workflow {name} with params {param_sets[0]}')

for params in param_sets:
    run = relay.workflows.run(name, params)
    logging.info(run)
    relay.decorators.set_link(
        # add leading zeros for proper ordering in the UI
        f'{run.run_number:03d}',
        f'Run {run.run_number:03d}',
        run.app_url
    )
