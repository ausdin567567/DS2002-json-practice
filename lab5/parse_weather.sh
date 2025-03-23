#!/bin/bash

# Step 2
curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85" > aviation.json

# Step 3 and 4
jq -r '.[].receiptTime' aviation.json | head -n 6

# Step 5 and 6
avg_temp=$(jq -r '[.[].temp] | add / length' aviation.json)
printf "Average Temperature:%.1f\n" "$avg_temp"

#Step 7 and 8
jq -r 'map([.clouds[].cover != "CLR"] | map(if . then 1 else 0 end) | add > 6) | if any then "Mostly Cloudy: true" else "Mostly Cloudy: false" end' aviation.json






