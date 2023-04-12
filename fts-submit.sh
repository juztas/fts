#!/bin/sh


transferID=`fts-rest-transfer-submit -o -s https://fts3-pilot.cern.ch:8446 -f bulk-out-$1.json | grep 'Job id' | awk '{print $3}'`

while true;
do
  transferStatus=`fts-rest-transfer-status -s https://fts3-pilot.cern.ch:8446 $transferID | grep Status | awk '{print $2}'`
  echo "TRANSFER Status $transferID $transferStatus"
  if [[ $transferStatus == "FINISHED" || $transferStatus == "FAILED" || $transferStatus == "FINISHEDDIRTY" ]] 
  then
    transferID=`fts-rest-transfer-submit -o -s https://fts3-pilot.cern.ch:8446 -f bulk-out-$1.json | grep 'Job id' | awk '{print $3}'`
  fi
  sleep 1
done


