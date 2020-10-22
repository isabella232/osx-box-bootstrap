#!/bin/bash

py.test --ansible-inventory=inventory_test --connection=ansible testinfra/baseOS/test_baseos.py -vvvv
