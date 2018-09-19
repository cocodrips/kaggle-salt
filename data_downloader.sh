#!/usr/bin/env bash
# Check kaggle command
kaggle competitions list -s health > /dev/null
if [ $? != 0 ]; then
    echo "Check kaggle command."
    exit
fi 

# Download
echo "---Download---"
kaggle competitions download -p input -c tgs-salt-identification-challenge

echo "---Unzip---"
unzip -qn input/train.zip -d input/train
unzip -qn input/test -d input/test
echo "Finish"

echo "---Delete .zip---"
rm input/train.zip
rm input/test.zip
echo "Finish"