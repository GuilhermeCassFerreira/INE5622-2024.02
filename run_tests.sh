#!/usr/bin/env bash
GREEN='\033[0;32m'
NC='\033[0m'

test_sources_dir="./test-sources"
parser_script="./parser.py"

if [ ! -f "$parser_script" ]; then
    echo "Script do parser não foi encontrado. Você configurou o projeto corretamente?"
    exit 1;
fi

for test_file in "$test_sources_dir"/*.lsi;
do
  printf "\n\n=========================================\n\n${GREEN}Executando arquivo de teste '$test_file'${NC}:\n"
  grep '^\s*/\?\*' $test_file | tr -d '*/'
  python3 $parser_script "$test_file"
done