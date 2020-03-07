#!/bin/bash

telnet localhost 6379 || docker run --name local-redis -p 6379:6379 -d redis
