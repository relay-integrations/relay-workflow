#!/bin/bash
set -eou pipefail

ni="ni"
jq="jq"
name="$( ${ni} get -p {.name} )"

declare -a parameters="( $( ${ni} get | ${jq} -r 'try .parameters | to_entries[] | "--parameter=\( .key )=\( .value )" | @sh' ) )"

echo "Running workflow: ${name}"
result="$( ${ni} workflow run -o json -n "${name}" "${parameters[@]}" )"

read name run_number url < <(echo ${result} | jq -r '[.[]] | @tsv')

${ni} decorator set link -n "workflow-run-link" --value="description=${name} #${run_number}" --value="uri=${url}"
