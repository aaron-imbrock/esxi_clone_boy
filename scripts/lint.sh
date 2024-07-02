#!/usr/bin/env bash
#
set -e
set -x

ruff check esxi-clone-boy
ruff format esxi-clone-boy --check
