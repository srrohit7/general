#! /bin/bash

### ! Replace `script_template.sh` with the actual name of the script.

usage() {
  ### ! Function to print the help box setup below. Lines starting with ## will be printed.
  echo
  script_loc="$(
    cd "$(dirname "$0")" >/dev/null 2>&1
    pwd -P
  )/script_template.sh"
  [ "$*" ] && echo "$script_loc: $*"
  sed -n '/^##/,/^$/s/^## \{0,1\}//p' "$script_loc"
  echo
  exit
}

# ================================================== #

## Title        : script_template.sh
## Description  : Description of your script.
## Author       : Your Name (youremail@iciq.es)
## Date         :
## Version      :
## Notes        :
## Todos        :
##
## Usage: ./script_template.sh [-a|h]
##
## Options:
##
## -a|--argument: Description of command line argument.
## -h|--help: Show this help-box and exit.

# ================================================== #

# Default values
default_variable='Default'
commandline_argument='Empty'

# Command line arguments
while [ $# -gt 0 ]; do
  case $1 in

  ### ! Adding command line arguments with short and long options.
  -a | --argument)
    commandline_argument=$2
    shift
    ;;

  ### ! Add additional command line arguments here in the same way as above.
  -h | --help)
    usage
    ;;

  *)
    :
    ;;
  esac
  shift
done

# ================================================== #

# Main program
echo "$default_variable"
echo "$commandline_argument"
